import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.dependencies import *

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.metadata", "https://www.googleapis.com/auth/drive.metadata.readonly", "https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file"]


def main():
  util.build_sheets_service()
  # service = util.build_sheets_service()
  # results = service.files().list(
  #     pageSize=10, fields="nextPageToken, files(id, name)").execute()
  # items = results.get("files", [])

  # if not items:
  #     print("No files found.")
  #     return
  # print("Files:")
  # for item in items:
  #     print(u"{0} ({1})".format(item["name"], item["id"]))
  
  
  
#     """Shows basic usage of the Drive v3 API.
#     Prints the names and ids of the first 10 files the user has access to.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists("auth/drive_token.json"):
#         creds = Credentials.from_authorized_user_file("auth/drive_token.json", SCOPES)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 "auth/credentials.json", SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open("auth/drive_token.json", "w") as token:
#             token.write(creds.to_json())

#     try:
#         service = build("drive", "v3", credentials=creds)

#         # Call the Drive v3 API
#         results = service.files().list(
#             pageSize=10, fields="nextPageToken, files(id, name)").execute()
#         items = results.get("files", [])

#         if not items:
#             print("No files found.")
#             return
#         print("Files:")
#         for item in items:
#             print(u"{0} ({1})".format(item["name"], item["id"]))
#     except HttpError as error:
#       print(error)
#       quit()


if __name__ == "__main__":
    main()