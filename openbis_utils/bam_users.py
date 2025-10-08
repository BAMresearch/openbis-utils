# openbis_utils/bam_users.py

import re
from openbis_utils.connection import connect_openbis

def get_userid_from_names(firstname, lastname, openbis=None):
    """
    Return the userId matching the given first and last name (case-insensitive).
    
    Parameters:
        firstname (str): First name
        lastname (str): Last name
        openbis (Openbis, optional): Connected Openbis object. If None, connect automatically.
    
    Returns:
        str or None: Matching userId or None if not found
    """
    o, _, _ = openbis if openbis else connect_openbis()
    users = o.get_users()
    for u in users:
        if u.firstName.lower() == firstname.lower() and u.lastName.lower() == lastname.lower():
            print(f"First name: {firstname}, Last name: {lastname} → userId: {u.userId}")
            return u.userId
    print("No match found")
    return None


def split_name(name):
    """
    Split a full name into firstname and lastname using comma ',' or space ' ' as separator.
    """
    parts = re.split(r',|\s+', name.strip())
    parts = [p for p in parts if p]
    if len(parts) >= 2:
        return parts[0], parts[1]
    return parts[0], ''  # if only one name


def get_userid_from_fullname(name, openbis=None):
    """
    Return the userId matching the given fullname (case-insensitive).
    Uses the split_name function.
    """
    firstname, lastname = split_name(name)
    o, _, _ = openbis if openbis else connect_openbis()
    users = o.get_users()
    for u in users:
        if (u.firstName.lower(), u.lastName.lower()) == (firstname.lower(), lastname.lower()) \
        or (u.firstName.lower(), u.lastName.lower()) == (lastname.lower(), firstname.lower()):
            print(f"Match found: {u.firstName} {u.lastName} → userId: {u.userId}")
            return u.userId
    print("No match found")
    return None


def get_info_from_userid(userId, openbis=None):
    """
    Print detailed information about a BAM user given their userId.
    
    Parameters:
        userId (str): BAM userId
        openbis (Openbis, optional): Connected Openbis object. If None, connect automatically.
    """
    o, _, _ = openbis if openbis else connect_openbis()
    user = o.get_user(userId)
    print("userId:", user.userId)
    print("firstName:", user.firstName)
    print("lastName:", user.lastName)
    print("email:", user.email)
    print("active:", user.active)
    print("registrator:", user.registrator)
    print("registrationDate:", user.registrationDate)
