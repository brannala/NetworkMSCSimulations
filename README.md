# Introduction
The purpose of this repository is to document the parameters used in simulations evaluating the statistical performance of the program [BPP](https://github.com/bpp/bpp) for Bayesian inference of species trees and networks.  The scripts (and embedded random number seeds) archived here allow the simulation results to be reproduced exactly.  The simulation study results are summarized in the supplemental material of the following article:

* Flouri T., Jiao X., Rannala B., Yang Z. 2019. A Bayesian multispecies coalescent model with introgression for comparative genomic analysis. Proc. Natl. Acad. Sci. (In Review). 

## Detailed procedure for reproducing the simulation results
The attached scripts generate 480 simulated datasets and then run the bpp program to analyze them. It is assumed that a unix system will be used to do this that has at least 32 cores and adequate free disk space. 

### Install dependencies
To run bpp and the simulation scripts you will need bison, flex, a C compiler, and python 3. On a debian linux machine those can be installed with apt

``` bash
sudo apt install flex bison gcc python3
```

### Install bpp and simulation scripts
The following commands will create a subdirectory named simulations containing a bpp executable and the simulation scripts for reproducing the simulation results. The simulations in the paper were done using release bpp 4.1.3. 

``` bash
mkdir simulations; cd simulations
git init; git clone https://github.com/brannala/NetworkMSCSimulations.git; cd networkmscsimulations 
wget https://github.com/bpp/bpp/archive/v4.1.3.zip; unzip v4.1.3.zip
cd bpp-4.1.3/src; make PROG=bpp4; cp bpp4 ../../
```

### Run the simulations
The script main.py generates all the control files for generating the simulations and running bpp on the simulated datasets. Warning: the following commands will generate many subdirectories and files as well as starting 480 bpp analyses on your machine(s). Don't say you weren't warned. If you need to terminate all the jobs that the script spawns you can use `pkill -f "bpp"` to do so.
``` bash
python3 ./main.py
```
You can check the status of your runs using a program such as `htop` or the unix command `ps -aux | grep bpp`.

### Summarize the simulation results
When the runs have completed (which may take either days, weeks, or months, depending on your computer resources) the following command will summarize the results for the posterior distributions of parameters 
``` bash
python3 results.py
```
This creates a set of 8 files summarizing results for different combinations of parameters. There are 8 R scripts that correspond to each of the summary files and that will create the plots using the summary files. The plots are created using ggplot so it is suggested that the [tidyverse](https://www.tidyverse.org/) set of R packages be installed which provides ggplot and other useful data analysis functions. 
