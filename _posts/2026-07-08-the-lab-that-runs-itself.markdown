---
layout: post
title: "The lab that runs itself (almost)"
date: 2026-07-08 12:05:00 -0500
tags: [paper]
paper:
 title: "Autonomous chemical research with large language models (Coscientist)"
 authors: "Boiko, MacKnight, Kline & Gomes"
 venue: "Nature, 2023"
 link: "https://doi.org/10.1038/s41586-023-06792-0"
 verdict: "The closest published analogue to an agentic lab assistant, a GPT-4 planner that reads docs, writes code, and drives robots."
---

**The problem.** LLMs can *talk* about experiments; can they *run* them, plan a protocol, write the instrument code, execute on real hardware, read the result, and iterate, without a human in every loop?

**The idea.** Coscientist is a GPT-4-driven agent built from cooperating modules: a **Planner** that decomposes a goal, a **web-search** tool, a **documentation-search** tool for reading hardware/API manuals, a **code-execution** sandbox, and an **automation** interface to physical liquid handlers and cloud labs. The headline demonstration is real chemistry: it planned and optimized palladium-catalyzed cross-couplings (Suzuki/Sonogashira), *reading the robot's own documentation* to write the control code, then executing on the hardware and using the results to steer the next round.

**Why it matters.** This is the published system that most resembles where an agentic Bench could go, the "Learn/act" step of DBTL made autonomous. Architecturally it's a tool-augmented LLM loop: planner + retrieval + code + actuators, which is exactly the RAG-plus-tools pattern I work in, only with the "tools" reaching into physical space. It's a concrete template for how much orchestration an LLM can actually own.

**Verdict.** Exciting and real, but the honest framing matters: it *optimizes well-posed, known reactions* rather than discovering new science, runs under human oversight, and the paper is upfront about safety guardrails (it declined some dangerous requests, but not all, a genuine caution). Read it as a proof-of-architecture, not a proof-of-autonomy, and map its module diagram onto your own agent work. Where it's real: retrieval + code + hardware control. Where it's hype: "AI scientist."
