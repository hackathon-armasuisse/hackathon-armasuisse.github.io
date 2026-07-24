---
title: General Information
layout: home
nav_order: 2
has_children: false
permalink: /general-information/
---

# General Information

Rules of the game that apply to every track. Read this carefully before starting your build.

---

## Infrastructure

- **Per-team VM.** Each team gets a dedicated virtual machine for development and deployment. This is your sandbox: build and deploy your application here.
- **Shared inference endpoint.** A central endpoint hosts the approved open-weights models on H200 GPUs. All teams pull from the same model menu, so the contest stays fair. The endpoint is `https://litellm.intlab.ch/v1` and is OpenAI-compatible. Your team receives an API key on Monday morning.
- **Hackathon website.** This site is the source of truth for tracks, rules, and timelines. 
- **Code in GitHub.** Applications are managed through GitHub repositories. We expect a reproducible build: someone from the organization team must be able to clone, configure, and run your application. Your code won't be visible for any other team till the end of the hackathon.
- **Exploits via form.** Exploits are submitted through an online form (linked from [Submitting Exploits]({% link submitting-exploits.md %})). A submission must include both a description of how the exploit was achieved and evidence that it worked.

---

## Red-team visibility

Red teams operate against other teams' deployments under realistic, partially-informed conditions:

- Red teams **know** the task specification, the I/O contract, and the list of available models.
- Red teams **do not see** other teams' source code, system prompts, or guardrail configurations. We treat the target as a **black box**.
- Red teams interact with targets only through the **legitimate user interface** or through indirect channels defined per track: emails received, web pages fetched, documents ingested, and so on.

---

## Scoring

Final standings combine two components. First, teams can gain points by building an application that performs well on the utility tests designed for their track. Second, teams can gain points by successfully exploiting other teams' deployments. The final score is the sum of these two components, so you need to invest in both building a solid application and defending it against attacks.

### Red-team points
Each successful exploit against another team's application scores points, **weighted by attack difficulty**. A clever indirect prompt injection that survives sensible defenses is worth more than a trivial jailbreak.

### Utility points
Each application is also evaluated on a battery of utility tests designed for its track. These tests check for task performance, robustness, and compliance with the I/O contract. The better your application performs on these tests, the more points you get.

---

## Out of scope (all tracks)

The following are out of scope across **all** tracks:

- **No UI work** is required beyond what is needed for the I/O contract. A simple HTTP endpoint or CLI is sufficient. Teams are free to build a UI if they want to, but it will not be scored.
- **No model fine-tuning.** Use the provided models as-is.
- **No attacks on the eval infrastructure, the inference endpoint, or other teams' VMs.** All adversarial action must go through legitimate input channels defined by each track.
- **No collusion between teams.**

Anything outside allowed channels that is not a valid exploit may result in disqualification of the submitting team.
