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

{: .note }
> **Both files are in UTC.** The chat export arrives in the exporting device's timezone; it has been shifted to UTC so that the two sources share one clock.

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

`messages.csv`, **1793 messages, 22 August to 2 September 2026**, from two monitoring groups.

| Column | Meaning |
|---|---|
| `message_id`, `group`, `sender` | provenance |
| `timestamp`, `date`, `time` | when posted, **UTC** |
| `text` | the message, verbatim |

The challenge here is to extract meaningful information from unprocessed Ukranian text. 

{: .warning }
> **The chat feed is private.** Among the drone reports the channel carries ordinary local traffic: evacuation requests, someone checking on a neighbour, a coordination note. Those messages name people and give addresses, phone numbers, medical details, vehicles and shelter locations. The advisor should answer *from* the feed, but nothing that identifies a person may appear in a response.

{: .note }
> There is no pattern that separates the sensitive messages from the rest. Phone numbers are written in words, names sit in ordinary sentences, and no message carries an email address or a handle. A regular expression will strip nothing and leak everything. The workable defence is not to reproduce feed content at all.

{: .note }
> **The siren record is authoritative.** If an alert is still present in the siren record, the advisor must not clear the area. If the chat feed indicates that the threat has passed, the advisor may mention that, but must also note that the siren record still indicates an alert. 

---

## How to obtain the data

Distributed as an **encrypted zip** in this [Google Drive](https://drive.google.com/drive/folders/1aG4Pwh3fFE5MgRJYsjKr1iRAYOTPeQGq?usp=sharing).

```
track3_data/
  sirens.csv      4241 official alert records 
  messages.csv    1793 monitoring messages
```

{: .note }
> Your zip password is provided to your team on **Monday morning**.

---
Next: [Building your Application]({% link tracks/track-3/building-application.md %}) →
