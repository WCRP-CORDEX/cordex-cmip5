CORDEX-CMIP5 coordination files
======

This repository contains coordination files for CORDEX-CMIP5, originally maintained under https://github.com/IS-ENES-Data/cordex. Here you can find **model registers** for CORDEX-CMIP5 ([CORDEX_register.xlsx](./CORDEX_register.xlsx)) and CORDEX-Adjust ([CORDEX_adjust_register.json](./CORDEX_adjust_register.json)), **archive specifications** for CORDEX-CMIP5 ([cordex_archive_specifications.docx](./cordex_archive_specifications.docx)) and CORDEX-Adjust ([CORDEX_adjust_drs.docx](./CORDEX_adjust_drs.docx)), and the **CORDEX-CMIP5 data request** in 2 different formats ([CORDEX_variables_requirement_table.xlsx](./CORDEX_variables_requirement_table.xlsx) and [CORDEX_standard_output.xls](./CORDEX_standard_output.xls)).

docs
----

The `docs` folder contains a set of machine readable register files, including the terms of use (ToU) and CORDEX-CMIP5 RCM info, along with PDF and HTML versions of different technical documentation, which is published under https://wcrp-cordex.github.io/cordex-cmip5. This folder was maintained as a separate repository in https://github.com/IS-ENES-Data/IS-ENES-Data.github.io

ESGF data loss (2025)
---------------------

In early 2025, a major data loss at DKRZ significantly impacted the availability of CORDEX-CMIP5 data through the ESGF, as many datasets—without existing replicas—were stored exclusively at that node.
Despite the hard work to recover as many data sets as possible, the loss still affects approximately 20,000 datasets (over 200 TB), spanning multiple CORDEX domains, variables, and output frequencies.
A full list of the missing datasets can be found at: [esgf-data-loss/Missing_CORDEX_Data.txt](./esgf-data-loss/Missing_CORDEX_Data.txt).

All CORDEX users are encouraged to check their local CORDEX-CMIP5 data archives (downloaded from ESGF) to help mitigate the impact of this data loss.
A simple script is available in the [esgf-data-loss/](./esgf-data-loss/) directory to assist in identifying whether your system contains any of the missing data.

```
bash locate_available_data.sh /path/to/your/CORDEX/data/following/ESGF/directory/structure
```

If you discover that you hold any of the affected datasets, please open an issue in [this repository](https://github.com/WCRP-CORDEX/cordex-cmip5/issues) or contact: datasupport@cordex.org.

Some of the most commonly used variables from the CORDEX-CMIP5 archive remain accessible via the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/datasets/projections-cordex-domains-single-levels?tab=overview) ([Diez-Sierra et al. 2024](https://doi.org/10.1175/BAMS-D-22-0111.1)).
