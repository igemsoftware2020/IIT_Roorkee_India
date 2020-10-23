We developed a machine learning algorithm for detecting genes conferring resistance to bacterial strains. The algorithm utilises pangenome of different strains along with their resistant phenotype information to find the list of the most important genes for a particular antibiotic. 

The repository contains the following,
## Folders
- strain_genome: contains the genomic information of each bacterial strain i.e. whether a particular gene is present or absent in that strain
- list_strains: contains the list of resistant and susceptible strains to each antibiotic, along with complete list of genes and alleles present in the pangenome

## Files
- dataset_creation.py: used for creating datasets for each particular antibiotic which will be used to train and validate the model
- training.py: used for training the model, and storing the sum of absolute weight for each gene, and weights for each iteration
- sorting_and_correlation.py: used for selecting top genes in the order of decreasing weights, and finding correlation between pair of alleles in top 40 rank
- mutational_analysis.py: used for analysing impact of mutations in genes on the resistant phenotype of the strains

The files must be run in the order mentioned above
