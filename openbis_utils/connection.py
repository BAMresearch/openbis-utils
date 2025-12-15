import keyring
from pybis import Openbis
from getpass import getpass, getuser

_cached_password = None

def connect_openbis(url='https://main.datastore.bam.de/', userid=None, space=None):
    """
    Connect to OpenBIS using a stored PAT from keyring if available.
    Fallback to interactive password login if no valid PAT exists.
    Returns: (Openbis object, userid, space)
    """
    global _cached_password
    resolved_userid = userid or getuser()

    # Try to retrieve PAT from keyring
    pat = keyring.get_password("openbis", resolved_userid)

    if pat:
        try:
            o = Openbis(url, token=pat)
            print(f"Connected using PAT for user {resolved_userid}")
            return o, resolved_userid, space
        except ValueError:
            print("Stored PAT expired or invalid, fallback to password login")

    # Fallback password login
    o = Openbis(url)
    if not _cached_password:
        _cached_password = getpass(f"Enter password for user {resolved_userid} at {url}: ")
    o.login(resolved_userid, _cached_password)
    print(f"Connected using password for user {resolved_userid}")

    # Store the new PAT securely in keyring for next run
    keyring.set_password("openbis", resolved_userid, o.token)
    return o, resolved_userid, space
