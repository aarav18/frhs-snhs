from lib.dependencies import *

MEMBERSHIP_SHEET_ID = "17p_QT9geS-OjS_jJnG5d6-PlOxaycaKZDbhYI_vAtKk"
MEMBERSHIP_RANGE_NAME = "'First Semester Applicants'!C2:C137"

def get_members_ids(service: Any) -> list[int]:
    member_ids = util.read_cells(service=service, sheet_id=MEMBERSHIP_SHEET_ID, sheet_range=MEMBERSHIP_RANGE_NAME)
    
    if not member_ids: raise Exception("No membership data found.")

    member_ids = [int(id[0]) for id in member_ids]
    return member_ids


if __name__ == "__main__": 
    service = util.build_service()
    print(get_members_ids(service=service))
    