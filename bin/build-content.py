#!/usr/bin/env python3
"""Derive the site's public data file from the private master content.yml.

    bin/build-content.py            # content.yml -> _data/profile.yml
    bin/build-content.py --check    # verify _data/profile.yml is up to date

content.yml is the single source of truth for professional history,
publications, projects, skills, and education. It is NOT committed: it carries
job-search strategy, reference contact emails, interview answers, and personal
disclosure decisions alongside the public facts. This script derives the public
subset and writes _data/profile.yml, which IS committed and is what Liquid
reads.

The rule is allow-nothing-by-default for the keys named in PRIVATE_TOP_LEVEL and
PRIVATE_ANYWHERE: they are stripped, and the result is then re-scanned to prove
none survived. If the scan fails the script exits non-zero and writes nothing.

Standard library only. Requires PyYAML, which the repo already needs for nothing
else -- see the FALLBACK note below if you'd rather not install it.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit(
        "PyYAML is required: pip install --user pyyaml\n"
        "(Only this build step needs it; the Jekyll build does not.)"
    )

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "content.yml"
DERIVED = ROOT / "_data" / "profile.yml"

# --------------------------------------------------------------------------
# The private set. Everything here is stripped before anything is written.
# --------------------------------------------------------------------------

# Whole top-level sections that never reach the site.
PRIVATE_TOP_LEVEL = {
    "role_families",          # which bullets to fire at which job family
    "keyword_policy",         # ATS keyword-injection strategy + honest-gaps list
    "logistics",              # reference contact emails, comp, EEO disclosures
    "interview_prep",         # rehearsed answers
    "answer_bank",            # rehearsed free-text answers
    "tracker",                # application tracker schema
    "bridge_bullets",         # downshifted bullets for bridge/interim roles
    "education_display_policy",  # applied at build time (below), never shipped
    "exam_scores",            # suppression policy note (holds no scores)
    "coursework_nameable",    # per-posting coursework selection
    "summaries",              # role-targeted summary variants; see SITE_SUMMARY_ID
    "selection_policy",       # how many bullets to fire per resume, and pairing rules
}

# Keys stripped at any depth, in any section.
PRIVATE_ANYWHERE = {
    "note",       # strategy annotations ("cut this for platform roles")
    "verify",     # unconfirmed-claim marker; see UNVERIFIED_BUT_PUBLIC
    "context",    # interview framing ("expect 'who are your users'")
    # Contact details and internal-only qualifiers. Not in the brief's list, but
    # they are personal data with no business being in a committed data file:
    "phone",              # identity.phone
    "email",              # identity.email -- the site uses Formspree instead
    "gpa_note",           # education.*.gpa_note ("omit unless required")
    "field_ats_alias",    # education.*.field_ats_alias (ATS keyword alias)
    "employer_of_record", # experience.*.employer_of_record (HJF payroll detail)
    "hours",              # experience.*.hours (application-form detail)
    "author_position",    # publications.*.author_position
    "variant_of",         # alternate phrasing marker; see strip() below
    "priority_note",      # per-family bullet-ordering rationale (resume strategy)
    "max_bullets",        # per-family render cap (resume strategy)
}

# Bullets carrying `verify: true` are unconfirmed and are dropped by default.
# The exception: claims already published on the live site, which this list
# re-admits explicitly so the modernization does not silently retract them.
#   ph_3 -- containerized Nextflow on Cloud Run + API ingestion layer; already
#           stated in the home About section and the CV Bench entry.
UNVERIFIED_BUT_PUBLIC = {"ph_3"}

# Which summary variant the site uses. The others are job-application framings.
SITE_SUMMARY_ID = "sum_general"

# Display order and headings for the skills block. Keys absent from content.yml
# are skipped; keys present but unlisted here are appended with a title-cased
# label, so adding a skills group upstream never silently drops it.
SKILL_GROUPS = (
    ("languages", "Languages"),
    ("frameworks", "Frameworks"),
    ("workflow", "Workflow &amp; reproducibility"),
    ("cloud", "Cloud &amp; infrastructure"),
    ("genomics", "Genomics &amp; sequencing"),
    ("singlecell", "Single-cell &amp; spatial"),
    ("ml", "ML &amp; AI"),
    ("stats", "Statistics &amp; analysis"),
    ("wetlab", "Laboratory"),
    ("clinical_research", "Clinical research"),
    ("domain", "Domain"),
)


def strip(node):
    """Recursively remove PRIVATE_ANYWHERE keys and verify-gated bullets."""
    if isinstance(node, dict):
        out = {}
        for key, value in node.items():
            if key in PRIVATE_ANYWHERE:
                continue
            out[key] = strip(value)
        return out
    if isinstance(node, list):
        kept = []
        for item in node:
            if isinstance(item, dict):
                # Unconfirmed claims: dropped unless already published.
                if item.get("verify") is True and item.get("id") not in UNVERIFIED_BUT_PUBLIC:
                    continue
                # `variant_of: <id>` marks an alternate phrasing of another
                # bullet, kept upstream so a targeted resume can pick either.
                # The site renders one, so the variant is dropped here.
                if item.get("variant_of"):
                    continue
            kept.append(strip(item))
        return kept
    return node


def scan_for_private(node, path="") -> list[str]:
    """Return paths of any private key that survived. Must come back empty."""
    found = []
    if isinstance(node, dict):
        for key, value in node.items():
            here = f"{path}.{key}" if path else key
            if key in PRIVATE_ANYWHERE or key in PRIVATE_TOP_LEVEL:
                found.append(here)
            found += scan_for_private(value, here)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            found += scan_for_private(item, f"{path}[{i}]")
    return found


MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def human_date(value) -> str:
    """'2026-03' -> 'Mar 2026'; date(2025,10,2) -> 'Oct 2025'; 'present' -> 'Present'."""
    if value is None:
        return ""
    if isinstance(value, date):
        return f"{MONTHS[value.month - 1]} {value.year}"
    text = str(value).strip()
    if text.lower() in ("present", "current"):
        return "Present"
    parts = text.split("-")
    if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
        month = int(parts[1])
        if 1 <= month <= 12:
            return f"{MONTHS[month - 1]} {parts[0]}"
    return text


def add_display_dates(entry: dict) -> None:
    """Attach a rendered `dates` range plus ISO values for <time datetime=...>."""
    start, end, year = entry.get("start"), entry.get("end"), entry.get("year")
    if start:
        left, right = human_date(start), human_date(end)
        entry["dates"] = f"{left} - {right}" if right else left
        entry["start_iso"] = str(start)
        if end and str(end).lower() != "present":
            entry["end_iso"] = str(end)
    elif year:
        entry["dates"] = str(year)
        entry["start_iso"] = str(year)


def build(master: dict) -> dict:
    public = {k: v for k, v in master.items() if k not in PRIVATE_TOP_LEVEL}
    public = strip(public)

    # The site summary, chosen here so the variants never ship.
    for summary in master.get("summaries", []):
        if summary.get("id") == SITE_SUMMARY_ID:
            public["summary"] = " ".join(summary["text"].split())
            break

    # Apply education_display_policy at build time: the credential line reads the
    # registrar field (Bioengineering). The policy text itself stays private.
    for entry in public.get("education", []):
        field = entry.get("field")
        if field:
            entry["degree_line"] = f"{entry['degree']}, {field}"

    # Render dates once here so no template has to parse them.
    for section in ("education", "experience", "projects"):
        for entry in public.get(section, []):
            add_display_dates(entry)
    for pub in public.get("publications", []):
        pub["published_display"] = human_date(pub.get("published"))
        pub["published_iso"] = str(pub.get("published", ""))
        # Collapse the folded citation block into one clean line.
        if pub.get("citation"):
            pub["citation"] = " ".join(pub["citation"].split())
    # Flatten skills into an ordered, labelled list so the template just loops.
    skills = public.pop("skills", {}) or {}
    ordered, seen = [], set()
    for key, label in SKILL_GROUPS:
        if skills.get(key):
            ordered.append({"key": key, "label": label, "items": skills[key]})
            seen.add(key)
    for key, items in skills.items():
        if key not in seen and items:
            ordered.append(
                {"key": key, "label": key.replace("_", " ").capitalize(), "items": items}
            )
    public["skills"] = ordered

    for cert in public.get("certifications", []):
        if cert.get("issued"):
            cert["issued_display"] = human_date(cert["issued"])
        if cert.get("expires"):
            cert["expires_display"] = human_date(cert["expires"])

    return public


HEADER = """\
# GENERATED FILE -- DO NOT EDIT BY HAND.
#
# Derived from the private master content.yml by bin/build-content.py.
# Edit content.yml, then run:
#
#     python3 bin/build-content.py
#
# content.yml is gitignored: it holds job-search strategy, reference contact
# details, and personal disclosure decisions. This file is the public subset and
# is what Liquid reads as site.data.profile.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero if _data/profile.yml is stale, instead of writing",
    )
    args = parser.parse_args()

    if not MASTER.exists():
        # The master is gitignored, so a fresh clone or CI will not have it.
        # That is fine: the derived file is committed. Nothing to do.
        print(f"{MASTER.name} not present; keeping committed {DERIVED.name} as is.")
        return 0

    master = yaml.safe_load(MASTER.read_text())

    public = build(master)

    leaks = scan_for_private(public)
    if leaks:
        print("REFUSING TO WRITE -- private keys survived the strip:", file=sys.stderr)
        for leak in leaks:
            print(f"  {leak}", file=sys.stderr)
        return 1

    body = yaml.safe_dump(public, sort_keys=False, allow_unicode=True, width=100)
    rendered = HEADER + "\n" + body

    # Belt and braces: no reference contact address or phone number in the bytes.
    for needle in ("@usuhs.edu", "@illinois.edu", "630) 725", "6307258464"):
        if needle in rendered:
            print(f"REFUSING TO WRITE -- found {needle!r} in output.", file=sys.stderr)
            return 1

    if args.check:
        current = DERIVED.read_text() if DERIVED.exists() else ""
        if current != rendered:
            print(f"{DERIVED.relative_to(ROOT)} is stale; run bin/build-content.py")
            return 1
        print(f"{DERIVED.relative_to(ROOT)} is up to date.")
        return 0

    DERIVED.parent.mkdir(exist_ok=True)
    DERIVED.write_text(rendered)
    kept = ", ".join(public.keys())
    print(f"Wrote {DERIVED.relative_to(ROOT)}\n  sections: {kept}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
