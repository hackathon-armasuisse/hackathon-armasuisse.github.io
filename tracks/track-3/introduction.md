---
title: Introduction
parent: "Track 3: Air monitoring thread"
nav_order: 1
layout: home
permalink: /tracks/track-3/introduction/
---

# Introduction

{: .summary }
> **In short:** Build an agent that parses several air threat monitoring
> chanells and issues warnings to teh end user. The user must be warned for 
> as fast and for as little as reasonably possible, so that they can accomplish
> their tasks, while making sure that they are warned at least 5 minutes before 
> a strike on or neir their position occurs. Threat monitoring channels provide
> near-real time updates as text messages intended for humans.

## Scenario

An expert in demining is sent by Confederation to Kyiv in order to exchange experience in dealing
with the latest generations of IEDs and UXO. Due to the frequency of air raid alerts, to accomplish their mission, they need to have a fine-grained advisory of air risk for their location, given the current threats and air defense capabilities.

A conversation with locals suggest that to achieve similar tasks, they use air threat monitoring, which are in part alimented by the national or local units of air defense, and in part by algorithmic aggregators.

- Ingest the different threat monitor threads
- Analyze the patterns in threat do identify the predictors of imminent air hits on specific locations
- Monitor user's location
- Tell the user when they are safe, should be alert, and need to head to shelter immediately (at least 5 minutes leeway)
- Always quantify the risk of your evaluation being incorrect, ensuring the user is aware of 

## Task

Build an assistant that ingests the provided threat monitoring threads, develops a heuristic to predict imminent air hits on user's location, while maximizing the user's ability to move around to accomplish their tasks.

It must:

- Tell the user when they are safe, at risk, and need to shelter immediately
- Provide the confidence on the judgement to the user
- Maintain a 5-minute lead on the status change to allow the user to shelter
- Make sure the risk is linked to user's location


{: .important }
> The assistant must balance two pressures: **ensure the user is safe**, while maximizing
> the time user can move freely around to accomplish their tasks.


---

Next: [Data]({% link tracks/track-3/data.md %}) →
