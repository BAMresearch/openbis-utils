from openbis_utils.connection import connect_openbis

def get_all_properties(sample_id):
    """
    Return all properties of a sample given a permID or sample_ident.
    """
    o, userid, space = connect_openbis()
    sample = o.get_sample(sample_id)
    if sample is None:
        raise ValueError(f"No sample found: {sample_id}")

    # Return as dict: property name -> value
    props_dict = {attr: getattr(sample.props, attr) for attr in dir(sample.props)
                  if not attr.startswith('$')}
    return props_dict


def get_single_property(sample_id, property_name):
    """
    Return a single property value of a sample.
    """
    o, userid, space = connect_openbis()
    sample = o.get_sample(sample_id)
    if sample is None:
        raise ValueError(f"No sample found: {sample_id}")

    if not hasattr(sample.props, property_name):
        raise ValueError(f"Property '{property_name}' does not exist in sample {sample_id}")

    return getattr(sample.props, property_name)
