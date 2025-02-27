import os
import logging
from src.config import get_config
from src.utils import fetch_submissions, process_submissions, append_submissions_to_sheet, get_existing_submission_ids

def main():
    config = get_config()
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting ODK-FinSync sync process...")
    
    # 1. Fetch submissions from ODK Central
    submissions = fetch_submissions(config)
    if not submissions:
        logging.info("No new submissions found.")
        return

    # 2. Get existing submission IDs from the sheet
    existing_ids = get_existing_submission_ids(config)
    
    # 3. Process the submissions
    processed_rows = process_submissions(submissions)
    
    # 4. Filter out duplicates
    new_rows = [row for row in processed_rows if row[0] not in existing_ids]
    
    # 5. Append new rows to Google Sheets
    if new_rows:
        append_submissions_to_sheet(new_rows, config)
        logging.info(f"Appended {len(new_rows)} new rows.")
    else:
        logging.info("No new rows to append.")

if __name__ == "__main__":
    main()
