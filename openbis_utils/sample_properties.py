def get_all_properties(sample_id, o):
    sample = o.get_sample(sample_id)
    if sample is None:
        raise ValueError(f"No sample found: {sample_id}")
    props_dict = {attr: getattr(sample.props, attr) for attr in dir(sample.props)
                  if not attr.startswith('$')}
    return props_dict

def get_single_property(sample_id, property_name, o):
    sample = o.get_sample(sample_id)
    if sample is None:
        raise ValueError(f"No sample found: {sample_id}")
    if not hasattr(sample.props, property_name):
        raise ValueError(f"Property '{property_name}' does not exist in sample {sample_id}")
    return getattr(sample.props, property_name)

def get_nonempty_properties(sample_id, o):
    """
    Return all properties of a sample that are not empty (None, empty string, or empty list).
    
    Parameters:
        sample_id (str): permID or sample identifier of the sample
        o (Openbis): OpenBIS connection object

    Returns:
        dict: dictionary of property_name -> value for non-empty properties
    """
    all_props = get_all_properties(sample_id, o)
    nonempty_props = {
        k: v
        for k, v in all_props.items()
        if v not in (None, "", [])  # filter out empty values
    }
    return nonempty_props