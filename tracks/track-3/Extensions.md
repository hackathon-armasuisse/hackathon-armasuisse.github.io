---
title: Extensions
parent: "Track 3: Air Threat Advisor"
nav_order: 6
layout: home
permalink: /tracks/track-3/extensions/
---

# Extensions

{: .summary }
> **Optional.** Once your core advisor works, these are directions to take it further. They are pointers, not requirements: pick any, all, or none.

Your baseline is the advisor from [Building your Application]({% link tracks/track-3/building-application.md %}).

---

## 1. Add a user interface

A person under an alert wants a colour and a sentence, not JSON. A map with the last hour of reports plotted, and a single line telling them what to do, demos far better than a transcript.

{: .tip }
> [Open WebUI](https://openwebui.com) speaks the OpenAI chat format, so a thin adapter in front of `/advise` gets you a chat UI quickly.

---

## 2. Track objects, not messages

The feed describes the same drone repeatedly as it crosses the country. Link those reports into tracks with a heading and a rough speed, and you can warn places that nobody has named yet. This is the single biggest capability jump available in this track, and it is also where confident nonsense is easiest to produce, so measure it.

---

## 3. Confidence and source weighting

Add a confidence to each answer, and let it depend on where the evidence came from: a siren record, a corroborated report, or a single unverified post do not deserve equal weight.

---

## 4. Push instead of pull

Invert the interface: a user registers a location once, and the advisor notifies them when something turns towards it. This turns the task from question-answering into monitoring, and it makes false positives expensive in a way the request/response form hides.

---

## 5. Your own extension

Free choice. A few directions:

- **geocoding** the place names so distance and bearing become real quantities rather than string matching;
- **normalising the Ukrainian**: inflection, transliteration, and the abbreviations the channels use;
- **structured event extraction**: turn each message into `{count, weapon, origin, destination, verb}` and reason over that instead of prose.
