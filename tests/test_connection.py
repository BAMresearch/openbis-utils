# tests/test_connection.py

import pytest
from unittest.mock import MagicMock, patch
from openbis_utils.connection import connect_openbis

def test_connect_openbis_returns_tuple():
    """
    Minimal test of the connect_openbis function without actually connecting to openBIS.
    Verifies that the function returns a tuple (Openbis, userid, space)
    and that the token split works correctly.
    """

    # Mock object Openbis
    dummy_openbis = MagicMock()
    dummy_openbis.token = "abc-dummy-xyz"  # <- dummy value to test split
    dummy_person = MagicMock()
    dummy_person.space = "DUMMY_SPACE"

    # Patcher Openbis and getuser
    with patch('openbis_utils.connection.Openbis', return_value=dummy_openbis):
        with patch('openbis_utils.connection.getuser', return_value='dummyuser'):
            with patch.object(dummy_openbis, 'get_person', return_value=dummy_person):
                o, userid, space = connect_openbis(url='dummy_url', pat='dummy')

                # Assertions
                assert o == dummy_openbis
                assert userid == 'dummy'          # split("abc-dummy-xyz")[1] == 'dummy'
                assert space == "DUMMY_SPACE"
