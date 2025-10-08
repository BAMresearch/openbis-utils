# openbis-utils

A small Python utility package for interacting with BAM's openBIS instance.  
It provides tools to connect, retrieve user information, and manage vocabularies.

## Installation

Clone the repo and install locally:

```bash
git clone https://github.com/TomCharlesRousseau/openbis-utils.git
cd openbis-utils
pip install .

Quick Start
Connect to openBIS

from openbis_utils.connection import connect_openbis

o, userid, space = connect_openbis()
print(f"Connected as {userid} in space {space}")
