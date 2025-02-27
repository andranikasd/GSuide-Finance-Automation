# ODK-FinSync 🚀

**ODK-FinSync** is an open source tool that synchronizes finance transaction submissions from your self-hosted [ODK Central](https://odkcentral.docs.opendatakit.org/) server to a designated [Google Sheets](https://www.google.com/sheets/about/) table.

> **Tagline:**  
> *Synchronize your ODK finance submissions automatically!*

## Overview

ODK-FinSync performs the following tasks:
- **Polling ODK Central:**  
  It periodically fetches new finance transaction submissions via the ODK Central REST API.
- **Data Processing:**  
  It extracts key fields (Submission ID, Timestamp, Type, Category, Amount, Description) and formats them for Google Sheets.
- **Google Sheets Update:**  
  It uses the Google Sheets API to append new rows to your sheet, ensuring no duplicates.
- **Kubernetes Ready:**  
  The project is containerized and includes Kubernetes manifests for easy deployment in your homelab.

## Features

- **Automated Sync:**  
  Polls and processes data on a configurable schedule.
- **Duplicate Avoidance:**  
  Checks existing entries in your sheet to prevent duplicate data.
- **Containerized & Scalable:**  
  Deploy via Docker and Kubernetes (CronJob or Deployment).
- **Open Source:**  
  Fully open source with community contributions welcome.

## Setup Instructions

### Prerequisites

- A self-hosted ODK Central instance with finance forms deployed.
- A Google Cloud project with the Google Sheets API enabled.
- A Google Sheets table with the following header row:
