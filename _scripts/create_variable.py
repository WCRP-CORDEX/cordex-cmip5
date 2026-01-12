import os
import json
import pandas as pd
from pathlib import Path

import esgvoc.api as ev

save_dir = "variable"
os.makedirs(save_dir, exist_ok=True)

data = pd.read_csv('_scripts/CORDEX.csv.gz', compression='gzip')

known_variables_in_universe = ev.get_all_terms_in_data_descriptor("variable")

variables = data.variable.unique()

for item in variables:
    found_item = None
    for variable in known_variables_in_universe:
        if variable.drs_name == item:
            found_item = variable
            break

    if found_item is None:
        print(item, "not found in universe")
    else:
        dict_to_save = {
            "@context": "000_context.jsonld",
            "id": found_item.id,
            "type": found_item.type,
        }

        with open(Path(save_dir) / f"{found_item.id}.json", "w") as f:
            json.dump(dict_to_save, f, indent=4)
