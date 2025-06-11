# PROTRIDER Setup

This repository contains scripts and configurations to prepare proteomics quantification data (from MaxQuant output) as input for [PROTRIDER](https://github.com/gagneurlab/PROTRIDER), a tool for detecting protein expression outliers.

## 🔍 Workflow Overview

1. **Input files**:
   - `proteinGroups.txt` (from MaxQuant)
   - `experimentalDesignTemplate.txt` (mapping TMT channels to sample names)

2. **Processing steps**:
   - Selection of reporter intensity columns corresponding to real biological samples
   - Exclusion of control channels (e.g., HEK standard in channel 11)
   - Removal of samples with known issues (e.g., poor TMT labeling)
   - Renaming columns to reflect actual sample names
   - Generation of `quant_input.csv` as input for PROTRIDER
   - *(Optional)* generation of `covariates.csv` with metadata (e.g., batch, sample group)

3. **Output files**:
   - `quant_input.csv`
   - `covariates.csv` *(if applicable)*
   - `config.yaml` for running PROTRIDER