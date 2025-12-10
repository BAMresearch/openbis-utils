from os import environ
from pybis import Openbis
from getpass import getpass, getuser

_cached_password = None

def connect_openbis(url='https://main.datastore.bam.de/', pat=None, userid=None, space=None):
    """
    Connect to OpenBIS using PAT if available; fallback to password only once per session.
    Returns: (Openbis object, userid, space)
    """
    global _cached_password

    # Lire le PAT si pas passé en argument
    if not pat:
        pat_file = environ.get('OPENBIS_PAT_FILE', 'OPENBIS_PAT.txt')
        try:
            with open(pat_file, 'r') as f:
                pat = f.read().strip()
        except FileNotFoundError:
            pat = None

    if pat:
        # Connexion via token
        o = Openbis(url, token=pat)
        resolved_userid = userid or getuser()
    else:
        # Connexion fallback mot de passe
        o = Openbis(url)
        resolved_userid = userid or getuser()
        if not _cached_password:
            _cached_password = getpass(f"Enter password for user {resolved_userid} at {url}: ")
        o.login(resolved_userid, _cached_password)

    return o, resolved_userid, space
