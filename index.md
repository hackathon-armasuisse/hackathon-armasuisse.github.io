---
title: Welcome
layout: home
nav_order: 1
description: Welcome to the armasuisse Hackathon.
permalink: /
---

# Welcome to the armasuisse Hackathon
{: .fs-9 }

A week of building, breaking, and defending LLM applications.
{: .fs-6 .fw-300 }

---

## What this hackathon is about

You will spend a week designing and shipping a real LLM-powered application against a realistic threat model, then trying to break the applications that other teams build. Every team is both a **blue team** (building and defending its own application) and a **red team** (probing other teams' deployments for exploits).

The contest is deliberately set up so that raw model power is *not* the deciding factor. All teams use the same open-weights models on the same shared inference endpoint. What you control is the **scaffolding, the prompting, the tool design, and the guardrails**. 

At the end of the week, we will score each team based on three criteria:

- Capability of your application to perform its intended tasks,
- Defensive resilience against exploits aimed at you,
- Successful exploitation of other teams' applications.

---

## Schedule

**14-18 September 2026**, GHH, Feuerwerkerstrasse 36, Thun. Lunch is 12:00-13:30 every day, dinner from 17:00.

### Monday 14.09: Start Building your Application

| Time | Content |
|---|---|
| 09:00 - 10:00 | Introduction |
| 10:00 - 12:00 | Initial build phase |
| 13:30 - 17:00 | First version of the LLM application |

### Tuesday 15.09: Finalize your Build

| Time | Content |
|---|---|
| 09:00 - 12:00 | Continuation of the build phase. Refinements and possible voluntary extensions / initial guardrails. |
| 13:30 - 14:30 | Presentations (10 min + 5 min Q&A per team) |
| 14:30 - 17:00 | Feedback integration |

### Wednesday 16.09: Freeze and Attack

| Time | Content |
|---|---|
| 09:00 - 12:00 | Freeze and deploy. Red-teaming. |
| 13:30 - 17:00 | Red-teaming |

### Thursday 17.09: Patch and Attack

| Time | Content |
|---|---|
| 09:00 - 12:00 | Blue-teaming, implement additional guardrails |
| 13:30 - 17:00 | Red-teaming |

### Friday 18.09: Results

| Time | Content |
|---|---|
| 09:00 - 10:00 | Presentation of the leaderboard and key findings/lessons |
| 10:00 - 12:00 | Open discussion and presentation preparation |
| 13:30 - 15:30 | Final presentations (20 min + 5 min Q&A per team) |
| 15:30 - 16:00 | De-briefing and round table |

---

## Where to go from here

- Start with [General Information]({% link general-information.md %}) for the rules of the game: infrastructure, scoring, attack submissions, and what is out of scope.
- Open the page for your assigned **track** (e.g. [Track 1: Documentation Assistant]({% link tracks/track-1/index.md %})) for the scenario, data, application criteria, and submission instructions.
- Once attacks are open, see [Submitting Exploits]({% link submitting-exploits.md %}) for the instructions on how to submit your red-team findings.
- [Infrastructure]({% link infrastructure.md %}) covers your team VM, how to deploy on it, and the shared inference endpoint.
