# GAMA
Guess Add Mate Algorithm (GAMA) for Minimal Genome Design

GAMA and Minesweeper: genome design algorithms for whole-cell models
====================================================================
Minesweeper Github: https://github.com/GriersonMarucciLab/Minesweeper

Paper: Rees and Chalkley et al 2019, https://doi.org/10.1101/344564 (update post publication)

README Authors: 
Joshua Rees, joshua.rees@bristol.ac.uk, github: squishybinary

Oliver Chalkley, o.chalkley@bristol.ac.uk, github: OliCUoB

Affiliation: Genome Design Group, Life Sciences, University of Bristol BS8TQ UK

Minesweeper License: GNU General Public License v3.0, gpl-3.0 https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)

GAMA License: GNU General Public License v3.0, gpl-3.0 https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)

Minesweeper Version: 0.9
GAMA Version: 0.1 (Chalkley et al 2019, https://doi.org/10.1101/681270)

Last Updated: 2019-06-28 	



Description
===========
This code, in combination with the Mycoplasma genitalium whole-cell model https://github.com/CovertLab/WholeCell produces in-silico genome designs by knocking out modelled genes at scale.
Both algorithms require supercomputer(s) to run the simulations. The GAMA algorithm also needs a dedicated PC to split and monitor the simulations across the cluster(s) automatically.
The Minesweeper algorithm can be manually run on a non-dedicated desktop, with its output determining what simulations to be run on the supercomputer.
The algorithms and the background theory are explained in our paper, available on bioRxiv https://doi.org/10.1101/344564 .
For more information, see a copy of the Methods section of the manuscript, at the bottom of this document.		



Images
======
To visualise the steps of our algorithms see our figures, available on FigShare https://doi.org/10.6084/m9.figshare.c.4514813.v1 .



GAMA (Installation) (Chalkley et al 2019, https://doi.org/10.1101/681270)
=========================================================================
GAMA is written in Python3 and relies on a variety of different packages. These dependencies can be easily taken care of by installing it from PyPI using either:
> pip install genome_design_suite 
> conda install genome_design_suite 
(it is recommended that you do this from within a virtual environment since this is pre-alpha and has not been extensively tested with different versions of all the libraries). 
A list of dependencies is available in the main directory of the github repository if you would like to do this manually. The main dependency is the genome_design_suite which is a suite of tools created by Oliver Chalkley 
at the University of Bristol which enables it to be easily run on different (or even multiple) clusters and well as enabling automatic data processing and database management. 
In order to run this code you must have a computer dedicated to remotely managing the simulations. A PC with a quad-core Intel(R) Xeon(R) CPU E5410 (2.33GHz) and 1GB of RAM running CentOS-6.6 was used as our computer manager, 
which is referred to as OC2. GAMA was run on OC2 using the scripts contained in gama_management.zip.

For more information about setting the genome design suite see Chalkley et al 2019, https://doi.org/10.1101/681270 .



Demo (GAMA)
===========
GAMA utilises the genome design suite to run massive in-silico gene knock-out experiments using the whole-cell model of M. genitalium - please see https://doi.org/10.1101/681270 to learn about using the genome design suite. 
The genome design suite requires that one has a Linux computer dedicated to managing the in-silico experiments. There are three broad modules of code that the genome genome design suite uses (1) computer communication; 
(2) cluster management; and (3) genome design algorithm. Sub-classes of the parent class of (1) and (3) need to be made so that a user can customise experiments for different computer clusters or gene knock-out algorithms. 
Classes for module (2) need to be written to fit the users custom cluster management goals.


Computer communication
-----------------------
The genome design suite provides child computer communication classes that run on BlueCrystalIII and BlueGem - these act as templates for clusters with PBS/Torque or Slurm queuing systems, respectively. 
These child classes were used in this research (BlueCrystalIII for R&D and BlueGem to run GAMA). If a user wishes to run GAMA on a different cluster then s/he must set up encryption key access to the cluster through SSH, 
and create a child-class of the computer communication base class.


Cluster management 
-------------------
Two cluster management classes were presented in [] that allowed for data processing. A user can use this setup provided that they make two SQLite3 databases 
with corresponding Python modules available on the cluster.


Genome design algorithm
------------------------
GAMA is the genome design algorithm in this case and is designed to be a sub-class of the MGA class of the genome design suite. If the Computer communication and the cluster management modules are setup correctly then this 
will run without modification.


Running GAMA
-------------
The guess stage has not been fully integrated with the add and mate stage as a unique class as the different classes need to be run sequentially - GeneticAlgorithmFocusSet, and MixFocusSets, respectively. 
An instance of GeneticAlgorithmFocusSet class will simulate one partition from the guess stage and since there are 4 partitions, 4 scripts are needed to start each partition. These scripts are called focus_on_NE_split_X.py, 
where X is an integer between 1 and 4 to identify each partition. The add and mate stages should only require one starting script but the initial script contained an error which was corrected by stopping after four generations 
(i.e. after generation 3 because there is generation 0) and increasing the size of each generation from 400 to 1,000 children. The initial script is called mix_NE_focus_splits.py and the second script is called 
big_mix_of_split_mixes.py. If the user would like to run these in-silico experiments on a different cluster then instead of instead of creating an instance of the BG class as done in this script the user should create 
the computer communication sub-class relating to the desired structure. The creation of this sub-class is described in the 'Computer communication' section above. These scripts must be run in Python3.5. It is advised that 
if one connects to the hub computer through SSH that the job should be run in some kind of terminal multiplexer like GNU Screen or tmux so that it is possible to start the in-silico experiment, log out, and then log in  
later to monitor the progress. For the latter aim, one must be able to view the standard-out produced by the starting scripts. However, it is also useful to be able to have a record of the standard-out in a 
file so it is recommended that the start-up scripts are executed with the following command 'python starting_script.py 2>&1 | tee stdout_and_stderr.out' whilst in the appropriate Python3.5 environment.




Copy of Methods Section
=======================

Model Availability
------------------
The M.genitalium whole-cell model is freely available: https://github.com/CovertLab/WholeCell. The model requires a single CPU and can be run with 8GB of RAM. We run the M.genitalium whole-cell model on Bristols supercomputers using MATLAB R2013b, 
with the models standard settings. However, we use our own version of the SimulationRunner.m. MGGRunner.m is designed for use with supercomputers that start hundreds of simulations simultaneously, artificially incrementing the time-date value 
for each simulation, as this value is subsequently used to create the initial conditions of the simulation. This incrementation prevents the running of multiple simulations with identical initial conditions. 
Our research copy of the whole-cell model was downloaded 10th January 2017.


Code Availability
-----------------
The code used for this research is openly available on Github. This includes the code for Minesweeper and GAMA genome design tools, scripts for statistical analysis, scripts for analysing GO terms, our custom simulation runner, analysis scripts, 
a template bash script, as well as the bash scripts and text files used to generate the simulations in this paper.


Statistics
----------
We used the R binom package https://www.rdocumentation.org/packages/binom to conduct one-tailed binomial proportion confidence intervals on our 41 genes showing inconsistent results (success ranging from 6 to 9 replicates, out of a total of 10 replicates). 
We used binom.confit.exact (Pearson-Klopper) using 95% CIs, producing for: 6/10 replicates [0.26, 0.87], 7/10 replicates [0.34, 0.93], 8/10 replicates [0.44, 0.97], 9/10 replicates[0.55, 0.99]). We graphed these results in R and in Python using Seaborn 
https://seaborn.pydata.org/ the exact values, code, and graphs produced are available in Supplementary Information B & N. 
Figure 5 was generated by creating a similarity matrix between all of the 2955 genomes, with the gene information represented in a binary format (present or absent). The matrix calculated a distance metric (1 - Adjusted Rand Index), 
with each genome comparison given a normalised score (0 = the genomes were identical, 1 = as different as would be expected if each genome was generated randomly, 2 = completely different). The resulting 2955 x 2955 matrix was then 
reduced to two dimensions with a standard PCA. 


Minesweeper
-----------
Minesweeper is written in Python3 and consists of four scripts (one for each stage). It uses no external libraries, so should be able to be run on any modern operating system (as they come with Python preinstalled) via a terminal. 
Each stage/script requires a text file(s) as input, with each stage outputting simulation files. These are run on a supercomputer and the automatically produced summary file is used as input for the next stage. Stages one to three are sequential, 
with stage four repeating until Minesweeper stops. Detailed instructions are provided in the README and progress is recorded in the deletion log in /OUTPUT_final.

The first stage of Minesweeper is optional, if you already have single gene knockout simulation results, you can proceed to the second stage. 

The second stage creates 26 deletion segments: 
100%, 90%A, 90%B, 80%A, 80%B, 70%A, 70%B, 60%A, 60%B, 50%A, 50%B, 33%A-C, 25%A-D, 12.5%A-H. 
The A segments start from the top of the list of genes, whereas the B segments start from the bottom of the list of genes. 

The third stage progresses with the three largest deletion segments that produced a dividing cell, these three variants are referred to as red, yellow, blue. These perform as replicates and as a check on if the results are converging. 
The three variants are matched with smaller, dividing, non-overlapping segments using a list of allowed matches (implementation is detailed in third stage script), and unique combinations generated using a python implementation of powersets. 

The fourth stage splits the remaining genes into eight groups. The reason for selecting eight groups and three variants, is that a set of eight produces 256 unique combinations. 

Three variants each with 256 simulations (768 total) is 85% of the capacity of BlueGem. A set of nine groups with three variants (1536 simulations total) is 170% the capacity of BlueGem. 
Queueing systems mean that you dont require this number of CPUs in total, but the execution time is multiplied as you wait for the simulations to process. 
The number of variants and groups can be lowered or increased depending on the number of CPUs you have available.


GAMA
----
GAMA is written in Python3 and relies on a variety of different packages. These dependencies can be easily taken care of by installing it from PyPI using either pip install genome_design_suite or conda install genome_design_suite 
(it is recommended that you do this from within a virtual environment since this is pre-alpha and has not been extensively tested with different versions of all the libraries). 
A dependencies list is available in the main directory of the github repository if you would like to do this manually. The main dependency is the genome_design_suite which is a suite of tools created by Oliver Chalkley at the University of Bristol 
which enables it to be easily run on different (or even multiple) clusters and well as enabling automatic data processing and database management. Due to the large amount of data produced by the whole-cell model, the simulation output data was 
reduced to essential data, converted into Pandas DataFrames (https://pandas.pydata.org/) and saved in Pickle files. GAMA would have produced 100s of TBs of data in the models native output format (compressed matlab files) which we are not able 
to store so this was an essential step. In order to run this code you must have a computer dedicated to remotely managing the simulations. A PC with a quad-core Intel(R) Xeon(R) CPU E5410 (2.33GHz) and 1GB of RAM running CentOS-6.6 was used as 
our computer manager, which is referred to as OC2. GAMA was run on OC2 using the scripts contained in gama_management.zip. Each stage of GAMA was run individually and manually updated as it was in proof-of-concept stage when GAMA_236 was found. 
ko.db is an SQLite3 database used to stored key information about simulations like average growth rate and division time.

The guess stage splits the singularly non-essential genes in roughly equally sized partitions. The four files, focus_on_NE_split_[1-4].py, run the exploration of each of the four partitions of the guess stage from OC2 - after unzipping gama_management.zip 
these can be found in gama/guess. The submission scripts and other files automatically created to run the simulations on the cluster can be found in gama_run_files.zip -> gama_run_files/guess. The simulation output is saved in Pickle files and can be found
 in gama_data/guess. viability_of_ne_focus_sets_pickles.zip contains the viability data of these simulations and the Python script used to collect it.

The add stage was executed on OC2 by running the files in gama_management.zip -> gama/add. The submission scripts and other files automatically created to run the simulations on the cluster can be found in gama_run_files.zip -> gama_run_files/add. 
The simulation output can be found in gama_data/add and an overview of the simulation results can be found in ko.db where the batchDescrription.name is some derivative of mix_ne_focus_split.

The mate stage was executed on OC2 by running the file in gama_management.zip -> gama/mate. The submission scripts and other files automatically created to run the simulations on the cluster can be found in gama_run_files.zip -> gama_run_files/mate. 
The simulation output can be found in gama_data/mate and an overview of the simulation results can be found in ko.db where batchDescription.name is some derivative of big_mix_of_split_mixes.
 

Equipment
---------
We used the University of Bristol Advanced Computing Research Centress BlueGem, a 900-core supercomputer, which uses the Slurm queuing system, to run whole-cell model simulations. 
GAMA also used BlueCrystal, a 3568-core supercomputer, which uses the PBS queuing system.
We used a standard office desktop computer, with 8GB of ram, to write new code, interact with the supercomputer, and run single whole-cell model simulations. 
We used the following GUI software on Windows/Linux Cent OS: Notepad++ for code editing, Putty (ssh software)/the terminal to access the supercomputer, and FileZilla (ftp software) to move files in bulk to and from the supercomputer. 
The command line software we used included: VIM for code editing, and SSH, Rsync, and Bash for communication and file transfer with the supercomputers. 


Data Format
-----------
The majority of output files are state-NNN.mat files, which are logs of the simulation split into 100-second segments. The data within a state-NNN.mat file is organised into 16 cell variables, each containing a number of sub-variables. 
These are typically arranged as 3-dimensional matrices or time series, which are flattened to conduct analysis. The other file types contain summaries of data spanning the simulation. 


Data Analysis Process
----------------------
The raw data is automatically processed as the simulation ends. runGraphs.m carries out the initial analysis, while compareGraphs.m overlays the output on collated graphs of 200 unmodified M.genitalium simulations. Both outputs are saved as MATLAB .fig and .pdfs,
though the .fig files were the sole files analysed. The raw .mat files were stored in case further investigation was required.
 
To classify our data we chose to use the phenotype classification previously outlined by Karr (Figure 6B 17), which graphed five variables to determine the simulated cells phenotype. However, the script responsible for producing Figure 6B, 
SingleGeneDeletions.m, was not easily modified. This led us to develop our own analysis script recreating the classification: runGraphs.m graphs growth, protein weight, RNA weight, DNA replication, cell division, ands records several experimental details. 

There are seven possible phenotypes caused by knocking out genes in the simulation: non-essential if producing a dividing cell; and essential if producing a non-dividing cell because of a DNA replication mutation, RNA production mutation, 
protein production mutation, metabolic mutation, division mutation, or slow growing. 

For the single gene knockout simulations produced in initial input, the non-essential simulations were automatically classified and the essential simulations flagged. Each simulation was investigated manually and given a phenotype manually using 
the decision tree (see Supplementary Information D). 

For simulations conducted by Minesweeper and GAMA, simulations were automatically classified solely by division, which can be analysed from cell width or the endtime of the simulation.

Further analysis, including: cross-comparison of single-gene knockout simulations, comparison to Karr et als 17 results, analysis of Minesweeper and GAMA genomes (genetic content and similarity, behavioural analysis, phenotypic penetrance, gene ontology), 
and identification and investigation of high and low essentiality genes and groupings, were completed manually. The GO term analysis of gene deletion impacts was processed by a created script, then organised into tables of GO terms 
that were unaffected, reduced, or removed entirely.


Modelling: Scripts, Process and Simulations
-------------------------------------------
Generally, there are six scripts we used to run the whole-cell model. Three are the experimental files created with each new experiment (the bash script, gene list, experiment list), and three are stored within the whole-cell model 
and are updated only upon improvement (MGGrunner.m, runGraphs.m, and compareGraphs.m). The bash script is a list of commands for the supercomputer(s) to carry out. Each new bash script is created from the GenericScript.sh template, 
which determines how many simulations to run, where to store the output, which analysis to run, and where to store the results of the analysis. The gene list is a text file containing rows of gene codes (in the format 'MG_XXX',). 
Each row corresponds to a single simulation and determines which genes that simulation should knockout. 

The experiment list is a text file containing rows of simulation names. Each row corresponds to a single simulation and determines where the simulation output and results of the analysis are stored. 
In brief, to manually run the whole-cell model: a new bash script, gene list, and experiment list are created on the desktop computer to answer an experimental question. The supercomputer is accessed on the desktop via ftp software, 
where the new experimental files are uploaded, the planned output folders are created, and MGGRunner.m, runGraphs.m, compareGraphs.m files are confirmed to be present. The supercomputer is then accessed on the desktop via ssh software, 
where the new bash script is made executable and added to the supercomputers queuing system to be executed. Once the experiment is complete, the supercomputer is accessed on the desktop via ssh software, where the results of the analysis are 
moved to /pdf and /fig folders. These folders are accessed on the desktop via ftp software, where the results of the analysis are downloaded. More detailed instructions are contained within the template bash script.
Each wild-type simulation consists of 300 files requiring 0.3GB. Each gene manipulated simulation can consist of up to 500 files requiring between 0.4GB and 0.9GB. Each simulation takes 5 to 12 hours to complete in real time, 7 - 13.89 hours in simulated time.


Data Availability
-----------------
The databases used to design our in-silico experiments, and compare our results to, includes Karr et al 17 and Glass et al 24 Supplementary Information, and Fraser et al M.genitalium G37 genome 18 interpreted by KEGG 26 and UniProt 25 as 
strain ATCC 33530/NCTC 10195. 
Minesweeper simulations raw and transformed output (.mat files) are available upon request, as they require 4.2 TB of storage. The output .fig files (10 GB) are available for download from our groups Research Data Repository 
at the University of Bristol. GAMA simulations transformed output is available in ko.db.

