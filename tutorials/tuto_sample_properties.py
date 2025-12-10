from openbis_utils.connection import connect_openbis
from openbis_utils.sample_properties import get_all_properties, get_single_property

if __name__ == "__main__":
    # OpenBIS login
    o, userid, space = connect_openbis() 
    print(f"Connected as user: {userid}\n")

    # permID or sample_ident
    sample_id = "20250818171845267-17123"

    # All properties
    #all_props = get_all_properties(sample_id)
    #print("All properties:", all_props)

    # Specific property
    description = get_single_property(sample_id, "description")
    notes = get_single_property(sample_id, "notes")
    alias = get_single_property(sample_id, "alias")
    product_category = get_single_property(sample_id, "product_category")
    responsible = get_single_property(sample_id, "responsible_person")
    #print("\nDescription:", description)
    #print("\nNotes:", notes)
    #print("\nAlias:", alias)
    print("\nProduct category:", product_category)
    print("\nResponsible id:", responsible)
    print("\nResponsible person all:", get_all_properties(responsible))
    print(
    f"\nResponsible person"
    f"\nfirstname: {get_single_property(responsible, 'given_name')}"
    f"\nfamilyname: {get_single_property(responsible, 'family_name')}"
)
