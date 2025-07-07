import pandas as pd

#table relative routes
protein_file = "../data/proteinGroups.txt"
mapping_file = "../data/mapping_table.tsv"

#read the MaxQuant file with protein intensities 
protein_df = pd.read_csv(protein_file, sep="\t", low_memory=False)

#read curstom mapping table with IDs to map the MaxQuant table
mapping_df = pd.read_csv(mapping_file, sep="\t")

#extract column names and new names
original_names = mapping_df["PCT_result_no"].tolist()
new_names = mapping_df["PCT_no"]

#subset de columnas + Protein IDs
columns_to_extract = ["Protein IDs"] + original_names
subset_df = protein_df[columns_to_extract].copy()

#rename columns
rename_dict = dict(zip(original_names, new_names))
subset_df = subset_df.rename(columns=rename_dict)

#set protein ID as the index
subset_df = subset_df.set_index("Protein IDs")
subset_df.index.name = "protein_ID"

#save results
subset_df.to_csv("../output/quant_input.tsv", sep="\t")



####################### to delete

protein_file = "test_1-6/proteinGroups.txt"
mapping_file = "test_1-6/mapping_table_1-6.tsv"

#read the MaxQuant file with protein intensities 
protein_df = pd.read_csv(protein_file, sep="\t", low_memory=False)

mapping_df = pd.read_csv(mapping_file, sep="\t")


subset_df.to_csv("../output/input_1-6.tsv", sep="\t")

# all
protein_file = "data/test_all/proteinGroups.txt"
mapping_file = "data/test_all/mapping_table_all.tsv"

#read the MaxQuant file with protein intensities 
protein_df = pd.read_csv(protein_file, sep="\t", low_memory=False)

mapping_df = pd.read_csv(mapping_file, sep="\t")


subset_df.to_csv("output/input_all.tsv", sep="\t")

# w HEK
protein_file = "data/test_w_hek/proteinGroups.txt"
mapping_file = "data/test_w_hek/mapping_table_w_hek.tsv"

#read the MaxQuant file with protein intensities 
protein_df = pd.read_csv(protein_file, sep="\t", low_memory=False)

mapping_df = pd.read_csv(mapping_file, sep="\t")


subset_df.to_csv("output/input_w_kek.tsv", sep="\t")