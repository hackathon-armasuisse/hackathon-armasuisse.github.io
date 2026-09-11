---
title: Infrastructure
nav_order: 8
layout: home
permalink: /infrastructure/
---

# Infrastructure

## Your team VM

A dedicated **Ubuntu 24.04 LTS** machine: **2 vCPUs**, **8 GB RAM**, **95 GB disk**. Docker and Docker Compose are installed and your `vmadmin` user is in the `docker` group, so no `sudo` is needed for `docker` commands.

| | |
|---|---|
| **Hostname** | `llmhack-team-N.hackathon.intlab.ch` |
| **Connect** | `ssh vmadmin@<your IP>` |
| **Credentials** | handed to your team separately, with your hostname and IP |

The VM is your sandbox for development **and** the machine your application runs on during the contest. You deploy and keep it running yourself; we never build or run your code for you.

{: .warning }
> Do not reinstall or reconfigure the reverse proxy, the TLS certificates, or the compose file. They are provisioned per machine.

---

## Inference endpoint

All teams pull from the same model menu on the same hardware, so the contest turns on your scaffolding rather than on who picked the bigger model.

| | |
|---|---|
| **Endpoint** | `https://litellm.hackathon.intlab.ch/v1` (OpenAI-compatible, LiteLLM proxy) |
| **API key** | issued to your team on **Monday morning** |

Read `OPENAI_BASE_URL`, `OPENAI_API_KEY` and `MODEL` from the environment. Do not hard-code them, and do not commit the key. Because the endpoint is OpenAI-compatible, the `openai` SDK picks the first two up on its own.

---

## AI Usage

The usage of LLMs for coding assistance is encouraged, but make sure that you own your codebase. During your presentations, we may ask you questions on your code and your design decisions. 

You can use any of the models hosted on the inference endpoint, but can also use your own subscriptions. For the hosted models, we recommend using an existing framework, such as [OpenCode](https://opencode.ai/) or [omp](https://github.com/can1357/oh-my-pi).

For effective use of the models, we recommend you to first compose a plan of your application, and then use the models to implement it. Models are generally effective at implementing a plan, but drop the ball when it comes to devising an approach. 