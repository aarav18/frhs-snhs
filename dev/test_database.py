from lib.dependencies import *

TEST_SHEET_ID = "1mmn6L7R7jdkp8S8vSaxr1rasAxH2hatPnSSZluyoMCU"
TEST_RANGE_NAME = "'Sheet1'!Q1:R1"

def getAttendanceIDs(service: Any) -> list[int]:
  util.write_cells(service=service, sheet_id=TEST_SHEET_ID, sheet_range=TEST_RANGE_NAME, sheet_values=[["dsfo", "dsfd"]])
        

if __name__ == "__main__": 
  service = util.build_service()
  getAttendanceIDs(service)
  # print(getAttendanceIDs(service))