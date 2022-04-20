import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.dependencies import *

from membership import get_members_ids

ATTENDANCE_SHEET_ID = "1iXbgQ3Rrt5FMPBdwkaBai0uF5Ntgm0jHCu9e4niVhIU"
ATTENDANCE_RANGE_NAME = "'Form Responses 1'!B2:B200"

TEST_SHEET_ID = "1mmn6L7R7jdkp8S8vSaxr1rasAxH2hatPnSSZluyoMCU"
TEST_RANGE_NAME = "'Sheet1'!L2:L200"

def get_attendance_ids(service: Any) -> list[int]:
    attendance_ids = util.read_cells(service=service, sheet_id=ATTENDANCE_SHEET_ID, sheet_range=ATTENDANCE_RANGE_NAME)

    if not attendance_ids: raise Exception("No attendance data found.")    
    
    attendance_ids = [int(id[0].split("@psdschools.org", 1)[0]) for id in attendance_ids]
    return attendance_ids

def get_attendance_status() -> list[bool]:
    
    attendance_status = []
    
    member_ids = get_members_ids(service=service)
    attendance_ids = get_attendance_ids(service=service)
    
    for member_id in member_ids: attendance_status.append(member_id in attendance_ids)
    
    attendance_status = [["P"] if status == True else ["A"] for status in attendance_status]
    return attendance_status
        

if __name__ == "__main__": 
    
    service = util.build_sheets_service()
    member_ids = get_members_ids(service=service)
    attendance_ids = get_attendance_ids(service=service)
    attendance_status = get_attendance_status()
    
    util.write_cells(service=service, sheet_id=TEST_SHEET_ID, sheet_range=TEST_RANGE_NAME, sheet_values=attendance_status)