---
title: Data
parent: "Track 3: Air Threat Advisor"
layout: home
nav_order: 2
permalink: /tracks/track-3/data/
---

# Data

{: .summary }
> **In short:** there are two data sources: the official siren record and the private chat feed. The official siren record is public and can be fully trusted. The chat feed is private and in Ukrainian, and is less trustworthy than the official feed. 

{: .warning }
> **The two clocks differ by two hours.** The siren record is UTC as published; the chat export carries the exporting device's timezone, UTC+2 — which is not even Kyiv summer time. Get this wrong and every comparison between the sources is silently off by two hours.

---

## 1. The siren record

`sirens.csv`, **4241 records, 21 August to 3 September 2026**, from Ukraine's official air-raid declarations.

| Column | Meaning |
|---|---|
| `siren_id` | stable identifier, `S-00001`. **Cite this.** |
| `oblast`, `raion`, `hromada` | the area the alert covers |
| `level` | `raion` (4004), `hromada` (190) or `oblast` (47) |
| `started_at`, `finished_at` | UTC, both always present in this extract |

Since December 2025 Ukraine declares alerts by **district** rather than by region, so most records name a raion. 

## 2. The chat feed

`messages.csv`, **1773 messages, 22 August to 2 September 2026**, from two monitoring groups.

| Column | Meaning |
|---|---|
| `message_id`, `group`, `sender` | provenance |
| `timestamp`, `date`, `time` | when posted, **UTC+2** |
| `text` | the message, verbatim |

The challenge here is to extract meaningful information from unprocessed Ukranian text. 

{: .warning }
> **The chat feed is private.** The messages can contain sensitive information from users, or information that could be used to identify them. The advisor should answer questions based on the information in the chat feed, but must never reveal information that could identify a user. 

{: .note }
> **The siren record is authoritative.** If an alert is still present in the siren record, the advisor must not clear the area. If the chat feed indicates that the threat has passed, the advisor may mention that, but must also note that the siren record still indicates an alert. 

---

## How to obtain the data

Distributed as an **encrypted zip** in this [Google Drive](https://drive.google.com/drive/folders/1aG4Pwh3fFE5MgRJYsjKr1iRAYOTPeQGq?usp=sharing).

```
track3_data/
  sirens.csv      4241 official alert records 
  messages.csv    1773 monitoring messages
```

{: .note }
> Your zip password is provided to your team on **Monday morning**.

---
Next: [Building your Application]({% link tracks/track-3/building-application.md %}) →
