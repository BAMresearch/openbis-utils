# openbis-utils

A Python utility package for interacting with BAM's openBIS instance.  
It provides tools to connect, retrieve user information, and manage vocabularies.

---

## Folder Structure

openbis-utils/
│
├─ README.md
├─ pyproject.toml
├─ requirements.txt
├─ .gitignore
│
├─ openbis_utils/ # Main package
│ ├─ init.py
│ ├─ connection.py # Handles openBIS connection
│ ├─ bam_users.py # Functions to get BAM user IDs and info
│ ├─ vocabularies.py # Functions to list vocabularies and terms
│ └─ utils.py # Common helper functions
│
├─ scripts/ # Example scripts for users
│ └─ example_bam_users.py
│
└─ tests/ # Unit tests
├─ test_connection.py
├─ test_bam_users.py
└─ test_vocabularies.py


---

## Installation

Clone the repository and install locally:

```bash
git clone https://github.com/TomCharlesRousseau/openbis-utils.git
cd openbis-utils
pip install .
Quick Start
Connect to openBIS
python
Copy code
from openbis_utils.connection import connect_openbis

o, userid, space = connect_openbis()
print(f"Connected as {userid} in space {space}")
BAM User Utilities
python
Copy code
from openbis_utils.bam_users import get_userid_from_fullname, get_info_from_userid

# Get a userId from full name
uid = get_userid_from_fullname("Tom Rousseau", openbis=(o, userid, space))
print("UserId:", uid)

# Print detailed info for that user
get_info_from_userid(uid, openbis=(o, userid, space))
Vocabulary Utilities

from openbis_utils.vocabularies import list_vocabularies, get_vocabulary_terms

# List all PropertyTypes with controlled vocabularies
vocab_list = list_vocabularies(openbis=(o, userid, space))
print(vocab_list)

# Get terms for a specific vocabulary
df_terms = get_vocabulary_terms("BAM_LOCATION_COMPLETE", openbis=(o, userid, space))
Scripts
The scripts/ folder contains example scripts for easy testing:

example_bam_users.py — demonstrates usage of connection and bam_users.

Run scripts from the terminal:

python scripts/example_bam_users.py
Tests
Unit tests are available in the tests/ folder. Run them using:

pytest tests
Notes
The package automatically handles authentication via PAT or username/password.

Designed for internal BAM use; requires access to BAM's openBIS instance.

Recommended workflow: clone repo → install → use scripts or import modules in Jupyter/VSCode.

Contact / Contribution
Current maintainer: Tom Rousseau

For early collaboration, add your GitHub account as a collaborator on this private repo.

Future plan: transfer repo to BAMresearch organization.


---

Once you paste it in `README.md`, run:

```bash
git add README.md
git commit -m "Fully update README with structure, modules, examples, scripts, and tests"
git push origin main
