import sys, os

from util import build_drive_service
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.dependencies import *

def find_log(service: Any, id: int) -> list[dict[str, str]]:
  
  query = "sharedWithMe and name contains 'log' and '" + str(id) + "@psdschools.org' in writers"
  result = []
  
  page_token = None
  count = 0
  while True:
    response = service.files().list(q=query,
                                    spaces="drive",
                                    fields="nextPageToken, files(id, name)",
                                    pageToken=page_token).execute()
    result = response.get("files", [])
    for file in result:
      count = count + 1
      print("Found file: %s (%s)" % (file.get("name"), file.get("id")))
      
    page_token = response.get("nextPageToken", None)
    if page_token is None:
        break
  print("Count: " + str(count))
  
  return result


if __name__ == "__main__":
  service = util.build_drive_service()
  print(find_log(service=service, id=91212))