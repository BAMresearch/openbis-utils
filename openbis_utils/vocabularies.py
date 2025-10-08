from openbis_utils.connection import connect_openbis

def list_vocabularies(openbis=None, filter_str=None):
    """
    List all PropertyTypes using a vocabulary, optionally filtering by keyword.
    """
    o, _, _ = openbis if openbis else connect_openbis()
    property_types = o.get_property_types()
    results = []

    for pt in property_types:
        if pt.vocabulary and (not filter_str or filter_str.lower() in pt.vocabulary.lower()):
            results.append((pt.code, pt.vocabulary))

    return results


def get_vocabulary_terms(vocab_code, openbis=None):
    """
    Retrieve all terms of a specific controlled vocabulary.
    """
    o, _, _ = openbis if openbis else connect_openbis()
    terms = o.get_terms(vocabulary=vocab_code)
    df_terms = terms.df

    print(f"Vocabulary '{vocab_code}' contains {len(df_terms)} terms:")
    print(df_terms["code"].tolist())

    return df_terms


def get_vocabulary_dict(vocab_code, openbis=None):
    """
    Return the terms of a vocabulary as a Python dictionary {code: label}.
    """
    df = get_vocabulary_terms(vocab_code, openbis=openbis)
    vocab_dict = dict(zip(df["code"], df.get("label", df["code"])))
    return vocab_dict
