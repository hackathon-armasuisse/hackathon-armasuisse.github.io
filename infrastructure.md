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

### Available models

Three chat models and three embedding models, the same menu for every team. Use the **exact** ids below as the `model` value; a typo returns an error rather than a fallback.

**Chat models**, called on `/chat/completions`:

| Model id | Context window | temperature | top_p | top_k |
|---|---|---|---|---|
| `google/gemma-4-31B-it` | 262,144 tokens | 1.0 | 0.95 | 64 |
| `Qwen/Qwen3.8-Flash-Next` | 262,144 tokens | 1.0 | 0.95 | 20 |
| `mistralai/Mistral-Medium-3.5-128B` | 262,144 tokens | 1.0 | 1 | -1 |

Those are the sampling defaults applied when you do not set the parameter yourself; all three take the usual OpenAI parameters, so you can override any of them per request. `top_k = -1` means no top-k filtering at all. For grounded, extractive answers you will usually want a temperature well below the default of 1.0.

{: .note }
> `Qwen/Qwen3.8-Flash-Next` is a reasoning model: its responses carry a `reasoning_content` field alongside `content`. Read the answer from `content`, and do not show `reasoning_content` to a user or feed it back as context without thinking about what is in it.

**Embedding models**, called on `/embeddings`:

| Model id | Dimensions | Notes |
|---|---|---|
| `bge-m3:latest` | 1024 | multilingual |
| `zylonai/multilingual-e5-large:latest` | 1024 | multilingual; the E5 family expects `query: ` and `passage: ` prefixes |
| `qwen3-embedding:8b` | 4096 | largest of the three |

You can list the menu yourself at any time:

```bash
curl -H "Authorization: Bearer $OPENAI_API_KEY" https://litellm.hackathon.intlab.ch/v1/models
```

---

## AI Usage

The usage of LLMs for coding assistance is encouraged, but make sure that you own your codebase. During your presentations, we may ask you questions on your code and your design decisions. 

You can use any of the models hosted on the inference endpoint, but can also use your own subscriptions. For the hosted models, we recommend using an existing framework, such as [OpenCode](https://opencode.ai/) or [omp](https://github.com/can1357/oh-my-pi).

For effective use of the models, we recommend you to first compose a plan of your application, and then use the models to implement it. Models are generally effective at implementing a plan, but drop the ball when it comes to devising an approach. 
