import os

def get_config():
    return {
        "odk_central_api_url": os.environ.get("ODK_CENTRAL_API_URL"),
        "odk_api_token": os.environ.get("ODK_API_TOKEN"),
        "sheet_id": os.environ.get("SHEET_ID"),
        "google_service_account_file": os.environ.get("GOOGLE_SERVICE_ACCOUNT_FILE"),
        # Add more configuration items as needed
    }
