import pytest
from unittest.mock import MagicMock
from openbis_utils.vocabularies import (
    list_vocabularies,
    get_vocabulary_terms,
    get_vocabulary_dict,
)

def test_vocabularies_functions():
    """
    Unit test for vocabularies.py using mocked Openbis object.
    """

    # Create mock Openbis instance
    dummy_openbis = MagicMock()

    # --- Mock property types ---
    class DummyPropertyType:
        def __init__(self, code, vocabulary):
            self.code = code
            self.vocabulary = vocabulary

    property_types = [
        DummyPropertyType("PROP_A", "VOCAB_A"),
        DummyPropertyType("PROP_B", None),
        DummyPropertyType("PROP_C", "VOCAB_C"),
    ]
    dummy_openbis.get_property_types.return_value = property_types

    # --- Mock vocabulary terms ---
    import pandas as pd
    df_mock = pd.DataFrame({
        "code": ["LOC_1", "LOC_2"],
        "label": ["Location One", "Location Two"],
    })

    dummy_openbis.get_terms.return_value.df = df_mock

    # Pack Openbis tuple as expected
    openbis_mock = (dummy_openbis, "dummy_url", "DUMMY_SPACE")

    # --- Test list_vocabularies ---
    vocabs = list_vocabularies(openbis=openbis_mock)
    assert ("PROP_A", "VOCAB_A") in vocabs
    assert ("PROP_C", "VOCAB_C") in vocabs
    assert len(vocabs) == 2

    # --- Test list_vocabularies with filter ---
    filtered = list_vocabularies(openbis=openbis_mock, filter_str="A")
    assert all("A" in vocab for _, vocab in filtered)

    # --- Test get_vocabulary_terms ---
    df = get_vocabulary_terms("VOCAB_A", openbis=openbis_mock)
    assert len(df) == 2
    assert "LOC_1" in df["code"].tolist()

    # --- Test get_vocabulary_dict ---
    vocab_dict = get_vocabulary_dict("VOCAB_A", openbis=openbis_mock)
    assert vocab_dict == {"LOC_1": "Location One", "LOC_2": "Location Two"}
