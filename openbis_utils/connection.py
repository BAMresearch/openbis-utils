from pybis import Openbis
from os import environ
from getpass import getuser, getpass

def connect_openbis(url='https://main.datastore.bam.de/', pat='', userid='', space=''):
    """
    Connect to openBIS and return the Openbis object, resolved userid, and space.
    
    Parameters:
        url (str): URL of the openBIS instance
        pat (str): Personal Access Token (optional)
        userid (str): BAM user ID (optional)
        space (str): Space to use (optional)
    
    Returns:
        tuple: (Openbis object, resolved userid, resolved space)
    """
    try:
        # Attempt to read PAT from argument or environment/file
        pat = pat or open(environ.get('OPENBIS_PAT_FILE', 'OPENBIS_PAT.txt'), 'r').read().strip()
        o = Openbis(url, token=pat)
        userid = o.token.split('-')[1]
    except Exception:
        # Fallback: authenticate using username/password
        o = Openbis(url)
        userid = userid.lower() or getuser()
        password = getpass(f'Enter password for user {userid} at {url}: ')
        o.login(userid, password)

    # Retrieve person info to resolve default space
    person = o.get_person(userid)
    space = space.upper() or person.space

    return o, userid, space
