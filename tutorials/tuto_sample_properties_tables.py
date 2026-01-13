import keyring
from pybis import Openbis
from openbis_utils.connection import connect_openbis
from openbis_utils.sample_properties import extract_tables_as_list
from bs4 import BeautifulSoup

# ------------------------------------------------------------------
# 1. Connect to openBIS
# ------------------------------------------------------------------

USER = ""  # optional: keyring lookup handled in connect_openbis
URL = "https://main.datastore.bam.de"

o, userid, space = connect_openbis(
    url=URL,
    userid=USER
)

sample_id = "20250818171845267-17582"
s = extract_tables_as_list(sample_id, "notes", o, column_names=None, flatten=True)
print(s)