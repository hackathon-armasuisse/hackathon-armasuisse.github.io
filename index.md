---
title: Welcome
layout: home
nav_order: 1
description: Welcome to the Armasuisse Hackathon.
permalink: /
---

# Welcome to the Armasuisse Hackathon
{: .fs-9 }

A week of building, breaking, and defending LLM applications.
{: .fs-6 .fw-300 }

---

## What this hackathon is about

You will spend a week designing and shipping a real LLM-powered application against a realistic threat model, then trying to break the applications that other teams build. Every team is both a **blue team** (building and defending its own application) and a **red team** (probing other teams' deployments for exploits).

The contest is deliberately set up so that raw model power is *not* the deciding factor. All teams use the same approved open-weights models on the same shared inference endpoint. What you control is the **scaffolding, the prompting, the tool design, and the guardrails** &mdash; in other words, the things that determine whether an LLM application is safe enough to deploy.

The week culminates in a leaderboard that combines:

- successful exploits scored against other teams,
- defensive resilience against exploits aimed at you,
- and acceptance-test performance on legitimate user tasks.

The goal is for each team to leave with a concrete, hands-on understanding of where LLM applications are fragile, which mitigations actually work, and which ones look good on paper but fail in adversarial settings.

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
- Once attacks are open, see [Submitting Exploits]({% link submitting-exploits.md %}) for the form and what we expect in a report.
