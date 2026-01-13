from openbis_utils.connection import connect_openbis
from openbis_utils.sample_properties import (
    get_all_properties,
    get_single_property,
    get_nonempty_properties,
    extract_tables_as_list
)

# --- Tutorial test ---
if __name__ == "__main__":
    sample_id = "20250818171845267-17582"

    # Connect to OpenBIS (will use PAT if available, else ask for password)
    o, userid, space = connect_openbis()

    # Test single property
    print("Single property 'alias':")
    print(get_single_property(sample_id, "alias", o))

    # Test all properties
    print("\nAll properties:")
    all_props = get_all_properties(sample_id, o)
    print(all_props)

    # Test non-empty properties
    print("\nNon-empty properties:")
    ne_props = get_nonempty_properties(sample_id, o)
    print(ne_props)

    # Test HTML table extraction
    print("\nExtract tables from 'notes' property:")
    tables_flat = extract_tables_as_list(
        sample_id,
        property_name="notes",
        o=o,
        column_names=None,
        flatten=True
    )
    print(tables_flat)
