
# Automated Financial Tracker 💰📊

This project automates your financial tracking using **Google Forms**, **Google Sheets**, and **Google Calendar**. Every time you submit your spending or income via a form, your transaction is recorded, organized by month, and a color-coded calendar event is created!

---

## Table of Contents

- [Overview](#overview)
- [Components](#components)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview 🚀

This automated workflow does the following:

1. **User Submission**:  
   - You fill out a Google Form with:
     - **Type** ("Spend" or "Receive")
     - **Category**
     - **Amount**
     - **Description**

2. **Data Recording**:  
   - A **Timestamp** is automatically added.
   - A new row is appended to the **Transactions** sheet with the columns:
     ```
     Timestamp | Category | Description | Amount | Type | Google Calendar Event ID
     ```
   - A separate monthly sheet (named `yyyy-MM`) is created or updated with the transaction.

3. **Calendar Event Creation**:  
   - An all-day event is created on your dedicated **Google Calendar**.
   - The event is **green** if it's "Receive" (income) and **red** if it's "Spend" (expense).

---

## Components 🛠️

- **Google Form**:  
  Collects transaction details:
  - Type (Spend/Receive)
  - Category
  - Amount
  - Description

- **Google Spreadsheet**:  
  Stores your transactions and organizes them:
  - **Main Sheet**: "Transactions"
  - **Monthly Sheets**: Named in the format `yyyy-MM` (e.g., `2025-02`)

- **Google Calendar**:  
  A dedicated calendar where each transaction becomes a color-coded all-day event.

---

## Setup Instructions 🔧

### 1. Create the Google Form
- **Questions (in order)**:
  1. **Type** (e.g., "Spend" or "Receive")
  2. **Category**
  3. **Amount**
  4. **Description**

> **Note:** Do **not** link the form directly to a spreadsheet; the script will handle data insertion.

### 2. Create the Google Spreadsheet
- Create a new spreadsheet (e.g., "Financial Tracker").
- **Main Sheet ("Transactions")** should have these columns:
  ```
  Timestamp | Category | Description | Amount | Type | Google Calendar Event ID
  ```

### 3. Create a Dedicated Google Calendar
- In [Google Calendar](https://calendar.google.com), create a new calendar (e.g., "Financial Transactions").
- Copy its **Calendar ID** from the settings.

### 4. Configure the Apps Script
- Open the Apps Script editor (via **Extensions > Apps Script**) in your spreadsheet or as a standalone project.
- **Enable the Advanced Calendar API**:
  - Go to **Services** (or **Resources > Advanced Google Services**) and enable **Calendar API**.
- **Paste the code from automation.js** (update the placeholders with your IDs)

- **Replace**:
  - `"YOUR_SPREADSHEET_ID"` with your spreadsheet's ID.
  - `"YOUR_CALENDAR_ID"` with your dedicated calendar's ID.

### 5. Set Up the Trigger
- In the Apps Script editor, go to the **Triggers** (clock icon) and add a new trigger:
  - **Function**: `onFormSubmit`
  - **Event Source**: "From form" or "From spreadsheet"
  - **Event Type**: "On form submit"
- Authorize the script if prompted.

---

## Usage 📝

1. **Fill Out the Form**  
   - Each time you spend or receive money, submit the Google Form with the details.
   
2. **View Your Spreadsheet**  
   - Check the **Transactions** sheet for the new row:
     - **Timestamp | Category | Description | Amount | Type | Google Calendar Event ID**
   - A monthly sheet (e.g., `2025-02`) will be automatically created/updated.

3. **Check Your Calendar**  
   - A new all-day event is created:
     - **Green** for "Receive"
     - **Red** for "Spend"

---

## Troubleshooting 🔍

- **No Calendar Event?**  
  - Ensure the Advanced Calendar API is enabled.
  - Check the logs via **View > Logs** for errors.

- **Duplicate Rows?**  
  - Make sure the form isn’t linked to a spreadsheet directly if the script is handling data insertion.

- **Wrong Column Order?**  
  - Confirm your **Transactions** sheet headers match:
    ```
    Timestamp | Category | Description | Amount | Type | Google Calendar Event ID
    ```

- **Missing Monthly Sheet?**  
  - The script automatically creates monthly sheets based on the timestamp. Verify your timestamp format and time zone.

---

## License 📄

This project is open source and available under the [MIT License](LICENSE).

---

Enjoy your automated financial tracking system! 🎉 If you have any questions or suggestions, feel free to open an issue or submit a pull request.

---