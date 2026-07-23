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

| Day       | Content                                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------------------|
| Monday    | Introduction and initial build phase. First version of the LLM application.                                   |
| Tuesday   | Continuation of the build phase. Refinements and possible voluntary extensions / initial guardrails.          |
| Wednesday | Freeze and deploy. Whole day of red-teaming.                                                                  |
| Thursday  | Morning session of blue-teaming, with the option to implement additional guardrails. Afternoon of red-teaming. |
| Friday    | Presentation of the leaderboard and key findings/lessons in the morning. Then de-briefing and round tables.    |

---

## Where to go from here

- Start with [General Information]({% link general-information.md %}) for the rules of the game: infrastructure, scoring, attack submissions, and what is out of scope.
- Open the page for your assigned **track** (e.g. [Track 1: Documentation Assistant]({% link tracks/track-1/index.md %})) for the scenario, data, application criteria, and submission instructions.
- Once attacks are open, see [Submitting Exploits]({% link submitting-exploits.md %}) for the instructions on how to submit your red-team findings.
