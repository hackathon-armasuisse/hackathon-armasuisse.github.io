---
title: Data
parent: "Track 1: Air Monitoring Threads"
layout: home
nav_order: 2
permalink: /tracks/track-3/data/
---

# Data

{: .summary }
> **In short:** your assistant has access to [???] different air threat monitrong threads. 
> You will need to understand the structure of the messages, identify the indicators 
> of ground hits, and robust, geographically dependent predictors of them occurring, and
> process them as fast as possible to provide the user sufficiently advance warning.


## Air Threat Monitoring Threads

You have [???] **csv files** containing replays of several channels used by the locals to monitor air threat alerts. Some of them are country-wide, whereas some of them are local to the city. All of them are in Ukrainian, and contain abbreviations, locations names, and pictograms that are common knowledge amongst locals, but are not explicitely defined. 

It's up to you to infer what they mean and how to best use them.

## On-device

Your processing will need to be happening on-device, given the disruptions to internet connectivity due to the jamming. Your model must work on device, and your final package has to be below 1GB, including any eventual LLMs or static data.

## Online Processing

You are not allowed to modify the source threads. Any modification to the data must be occurring on-the-fly. The time to process an incoming message needs to be sub-10 seconds; ideally sub-1 second.


## How to obtain the corpus

The corpus is distributed as an **encrypted zip** in this [TODO Google Drive](https://drive.google.com/drive/folders/TODO).

{: .note }
> Your zip password is provided to your team on **Monday morning**.

### What a record looks like

Eeach CSV file contains the timestamp of the message delivered by a thread, and the contents. For instance:

```cvs
08:05, 9/2/2026, Повітряні Сили | UA Air Force: 🏍️ Реактивний БпЛА на Миколаїв.
08:08, 9/2/2026, Повітряні Сили | UA Air Force: 🚀КАБи на Донеччину.
08:15, 9/2/2026, Повітряні Сили | UA Air Force: 🏍️ Київщина - реактивний БпЛА повз Велику Димерку курсом на Бровари.
08:22, 9/2/2026, Повітряні Сили | UA Air Force: 🏍️ Реактивні БпЛА  на півночі Чернігівщини на/повз Городню у західному напрямку.
08:27, 9/2/2026, Повітряні Сили | UA Air Force: 🏍️ Реактивний БпЛА на сході Дніпропетровщини - 
```

Next: [Building your Application]({% link tracks/track-3/building-application.md %}) →
