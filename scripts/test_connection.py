from openbis_utils.connection import connect_openbis

if __name__ == "__main__":
    o, userid, space = connect_openbis()
    print(f"Connected as {userid} in space {space}")
