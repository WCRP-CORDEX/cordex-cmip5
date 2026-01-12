import os
import json
import pandas as pd
from pathlib import Path

import esgvoc.api as ev

save_dir = "domain"
os.makedirs(save_dir, exist_ok=True)

data = pd.read_csv('_scripts/CORDEX.csv.gz', compression='gzip')

known_regions_in_universe = ev.get_all_terms_in_data_descriptor("region")

domains = data.domain.unique()

for item in domains:
    found_item = None
    for domain in known_regions_in_universe:
        if domain.drs_name == item:
            found_item = domain
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
