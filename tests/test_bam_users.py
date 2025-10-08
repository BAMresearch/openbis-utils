# tests/test_bam_users.py

import pytest
from unittest.mock import MagicMock
from openbis_utils.bam_users import get_userid_from_names, get_userid_from_fullname, get_info_from_userid



def test_get_userid_functions():
    from unittest.mock import MagicMock
    
    # Dummy user class
    class DummyUser:
        def __init__(self, firstname, lastname, userId):
            self.firstName = firstname
            self.lastName = lastname
            self.userId = userId
            self.email = f"{firstname.lower()}.{lastname.lower()}@bam.de"
            self.active = True
            self.registrator = "admin"
            self.registrationDate = "2025-01-01"

    # Create example users inside the function
    user1 = DummyUser("Tom", "Rousseau", "troussea")
    user2 = DummyUser("Alice", "Smith", "asmith")

    # Mock Openbis
    dummy_openbis = MagicMock()
    dummy_openbis.get_users.return_value = [user1, user2]
    dummy_openbis.get_user.return_value = user1

    openbis_mock = (dummy_openbis, "dummy", "DUMMY_SPACE")

    # Test functions
    assert get_userid_from_names("Tom", "Rousseau", openbis=openbis_mock) == "troussea"
    assert get_userid_from_names("Alice", "Smith", openbis=openbis_mock) == "asmith"
    assert get_userid_from_fullname("Tom Rousseau", openbis=openbis_mock) == "troussea"
    assert get_userid_from_fullname("Rousseau, Tom", openbis=openbis_mock) == "troussea"

    # Test info function (just ensure it runs)
    get_info_from_userid("troussea", openbis=openbis_mock)
