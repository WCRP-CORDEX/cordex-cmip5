import os
import json
import pandas as pd
from pathlib import Path

import esgvoc.api as ev

save_dir = "institute"
os.makedirs(save_dir, exist_ok=True)

data = pd.read_csv('_scripts/CORDEX.csv.gz', compression='gzip')

known_institutions_in_universe = ev.get_all_terms_in_data_descriptor("institution")

intitutes = data.institute.unique()

for item in intitutes:
    found_inst = None
    for inst in known_institutions_in_universe:
        if inst.drs_name == item:
            found_inst = inst
            break
    if found_inst is None:
        for consor in ev.get_all_terms_in_data_descriptor("consortium"):
            if consor.drs_name == item.upper():
                found_inst = consor
                break
    if found_inst is None:
        for orga in ev.get_all_terms_in_data_descriptor("organisation"):
            if orga.drs_name == item:
                found_inst = orga
                found_inst.id = found_inst.id.replace("consortium/", "")
                break

    if found_inst is None:
        print(item, "not found in universe")
    else:
        dict_to_save = {
            "@context": "000_context.jsonld",
            "id": found_inst.id,
            "type": found_inst.type,
        }

        with open(Path(save_dir) / f"{found_inst.id}.json", "w") as f:
            json.dump(dict_to_save, f, indent=4)
