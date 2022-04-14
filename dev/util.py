from __future__ import print_function

import os.path
from typing import Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly", "https://www.googleapis.com/auth/spreadsheets"]

def build_service() -> Any:
  creds = None
    
  if os.path.exists("auth/token.json"):
      creds = Credentials.from_authorized_user_file("auth/token.json", SCOPES)
      
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              "auth/credentials.json", SCOPES)
          creds = flow.run_local_server(port=0)
          
      with open("auth/token.json", "w") as token:
          token.write(creds.to_json())

  try:
      service = build("sheets", "v4", credentials=creds)
      return service
  except HttpError as err:
    print(err)
    quit()

def read_cells(service: Any, sheet_id: str, sheet_range: str) -> list[Any]:
  return service.spreadsheets().values().get(spreadsheetId=sheet_id, range=sheet_range).execute().get("values")

def write_cells(service: Any, sheet_id: str, sheet_range: str, sheet_values: list[list[Any]]) -> None:

  body = {
    "valueInputOption": "RAW",
    "data": [
              {
                "range": sheet_range,
                "values": sheet_values
              }
            ]
  }
  
  service.spreadsheets().values().batchUpdate(spreadsheetId=sheet_id, body=body).execute()