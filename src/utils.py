import requests
import json
import logging
from google.oauth2 import service_account
from googleapiclient.discovery import build

def fetch_submissions(config):
    headers = {
        "Authorization": f"Bearer {config['odk_api_token']}",
        "Accept": "application/json"
    }
    response = requests.get(config["odk_central_api_url"], headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('items', [])
    else:
        logging.error("Error fetching submissions: %s", response.text)
        return []

def get_existing_submission_ids(config):
    # Set up Google Sheets API client using the service account file.
    creds = service_account.Credentials.from_service_account_file(
        config["google_service_account_file"],
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    sheets_service = build('sheets', 'v4', credentials=creds)
    try:
        result = sheets_service.spreadsheets().values().get(
            spreadsheetId=config["sheet_id"], range="Submissions!A:A").execute()
        values = result.get('values', [])
        existing_ids = {row[0] for row in values[1:]} if len(values) > 1 else set()
        return existing_ids
    except Exception as e:
        logging.error("Error reading sheet: %s", e)
        return set()

def process_submissions(submissions):
    rows = []
    for sub in submissions:
        submission_id = sub.get("instanceId")
        timestamp = sub.get("createdAt")
        answers = sub.get("answers", {})
        type_val = answers.get("type", {}).get("value", "")
        category = answers.get("category", {}).get("value", "")
        amount = answers.get("amount", {}).get("value", "")
        description = answers.get("description", {}).get("value", "")
        row = [submission_id, timestamp, type_val, category, amount, description]
        rows.append(row)
    return rows

def append_submissions_to_sheet(new_rows, config):
    creds = service_account.Credentials.from_service_account_file(
        config["google_service_account_file"],
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    sheets_service = build('sheets', 'v4', credentials=creds)
    body = {"values": new_rows}
    try:
        result = sheets_service.spreadsheets().values().append(
            spreadsheetId=config["sheet_id"],
            range="Submissions!A:F",
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()
        logging.info("Updated cells: %s", result.get('updates', {}).get('updatedCells', 0))
    except Exception as e:
        logging.error("Error appending to sheet: %s", e)
