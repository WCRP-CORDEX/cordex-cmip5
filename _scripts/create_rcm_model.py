import os
import json
import pandas as pd
from pathlib import Path

import esgvoc.api as ev

save_dir = "rcm_model"
os.makedirs(save_dir, exist_ok=True)

data = pd.read_csv('_scripts/CORDEX.csv.gz', compression='gzip')

known_sources_in_universe = ev.get_all_terms_in_data_descriptor("source")

rcm_models = data.rcm_model.unique()

for item in rcm_models:
    found_item = None
    for source in known_sources_in_universe:
        if source.drs_name == item:
            found_item = source
            break

    if found_item is None:
        print(item, "not found in universe")
    else:
        dict_to_save = {
            "@context": "000_context.jsonld",
            "id": found_item.id,
            "type": found_item.type,
            "rcm_name": ""
        }

        with open(Path(save_dir) / f"{found_item.id}.json", "w") as f:
            json.dump(dict_to_save, f, indent=4)
