from openbis_utils.connection import connect_openbis
from openbis_utils.bam_users import get_userid_from_fullname, get_info_from_userid

# Connect to openBIS
o, userid, space = connect_openbis()
print(f"Connected as {userid} in space {space}")

# Get a userId from a full name
uid = get_userid_from_fullname("Tom Rousseau", openbis=(o, userid, space))
print("UserId for Tom Rousseau:", uid)

# Print detailed info for that user
get_info_from_userid(uid, openbis=(o, userid, space))
