from openbis_utils.connection import connect_openbis
from openbis_utils.bam_users import get_userid_from_fullname

if __name__ == "__main__":
    # Connect to OpenBIS
    o, userid, space = connect_openbis()
    print(f"Connected as user: {userid} in space: {space}\n")

    # List of test full names
    test_names = [
        "Tom Rousseau",
        "Tom Rosj",
        "Müller-Elmau, Johanna"
    ]

    # Resolve each BAM user ID
    for name in test_names:
        uid = get_userid_from_fullname(name, openbis=(o, userid, space))
