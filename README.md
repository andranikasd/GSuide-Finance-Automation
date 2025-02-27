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
  ```
  Submission ID | Timestamp | Type | Category | Amount | Description
  ```
- Python 3, Docker, and Kubernetes (if deploying on your cluster).

### Configuration

Configure the following environment variables (or a config file):

- `ODK_CENTRAL_API_URL` – The base URL of your ODK Central server.
- `ODK_PROJECT_ID` – Your ODK Central project ID.
- `ODK_FORM_ID` – The identifier of your finance form.
- `ODK_API_TOKEN` – Your ODK API token for authentication.
- `SHEET_ID` – The ID of the target Google Sheets document.
- `GOOGLE_SERVICE_ACCOUNT_FILE` – Path to your Google service account JSON file.
- `SYNC_INTERVAL` – (Optional) The sync schedule interval (if using CronJob).

### Installation & Deployment

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ODK-FinSync.git
   cd ODK-FinSync
   ```

2. **Build the Docker Image:**

   ```bash
   docker build -t odk-finsync .
   ```

3. **Deploy to Kubernetes:**

   Edit the manifests in the `k8s/` directory with your environment variables and then deploy:

   ```bash
   kubectl apply -f k8s/finsync-cronjob.yaml
   ```

   (Or use `finsync-deployment.yaml` for a continuously running service.)

4. **Monitor Logs:**

   Use `kubectl logs` to monitor the sync process and troubleshoot if needed.

## Usage

- **Automatic Sync:**  
  Once deployed, ODK-FinSync will poll ODK Central at the configured interval, process any new submissions, and update your Google Sheets automatically.
- **Customization:**  
  The sync logic can be customized in the `src/` folder. Contributions and feature requests are welcome!

## TODO / Roadmap

- [ ] **Improve Error Handling:** Enhance retry mechanisms and error reporting.
- [ ] **Unit & Integration Tests:** Add comprehensive tests for each module.
- [ ] **Configuration UI:** Consider a web UI for managing settings.
- [ ] **Monitoring & Metrics:** Integrate with Prometheus/Grafana for real-time monitoring.
- [ ] **Documentation:** Expand usage examples and developer docs.
- [ ] **CI/CD Pipeline:** Set up automated testing and deployment pipelines.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Next Steps

1. **Create the Repository:**  
   - Log into GitHub and create a new repository named `ODK-FinSync`.
2. **Populate the Repository:**  
   - Add the README.md, Dockerfile, Kubernetes manifests, and initial source code (as per your chosen language, e.g., Python).
3. **Iterate & Improve:**  
   - Use the TODO list as your project roadmap and update it as you progress.
