import itertools
import subprocess
import os
import time
import re

def createResultFile(combo, result):
    ofile = open('results' + ''.join(combo) + '.txt',"+w")
    ofile.write(result)
    ofile.close()

def getOneReplicate(combo,locus,rep):
    rfile = open('sim' + ''.join(combo) + locus + '.' + str(rep) + '.out.txt',"r")
    for line in rfile:
        if re.match("mean", line):
            mean = line.split()
        elif re.match("2.5\%HPD", line):
            lci = line.split()
        elif re.match("97.5\%HPD", line):
            uci = line.split()
    results = ''
    if int(combo[3]) == 0:
        paramindex=[1,3,4,5,6,9,10,11,12]
        if locus == '0':
            loci = "10"
        elif locus == '1':
            loci = "100"
        else:
            loci = "1000"
        for param in paramindex:
            results += mean[param] + " "
            results += lci[param] + " "
            results += uci[param] + " "
        results += loci + "\n"
    elif int(combo[3]) == 1:
        paramindex=[1,3,4,5,7,9,11]
        if locus == '0':
            loci = "10"
        elif locus == '1':
            loci = "100"
        else:
            loci = "1000"
        for param in paramindex:
            results += mean[param] + " "
            results += lci[param] + " "
            results += uci[param] + " "
        results += loci + "\n"
    return results
    rfile.close()



# create vector of tuples with indexes of all possible parameter combinations (excluding loci)
sim_iter = itertools.product('10', '10', '10', '10')
sim_combinations = []
for it in sim_iter:
    sim_combinations.append(it)

# visit each simulation subdirectory
for combo in sim_combinations:
    if int(combo[3]) == 0:
        simSummary='theta_1A theta_1A_LCI theta_1A_UCI theta_3C theta_3C_LCI theta_3C_UCI theta_4R theta_4R_LCI theta_4R_UCI theta_5S theta_5S_LCI theta_5S_UCI	theta_6H theta_6H_LCI theta_6H_UCI tau_4R tau_4R_LCI tau_4R_UCI	tau_5S tau_5S_LCI tau_5S_UCI tau_6H tau_6H_LCI tau_6H_UCI phi_H phi_H_LCI phi_H_UCI noloci \n'
    else:
        simSummary='theta_1A theta_1A_LCI theta_1A_UCI theta_3C theta_3C_LCI theta_3C_UCI theta_4R theta_4R_LCI theta_4R_UCI theta_5S theta_5S_LCI theta_5S_UCI tau_4R tau_4R_LCI tau_4R_UCI tau_6H tau_6H_LCI tau_6H_UCI phi_H phi_H_LCI phi_H_UCI noloci \n'
    for locus in ('0','1','2'):
        os.chdir('./sim' + ''.join(combo) + locus)
        for rep in range(1,11):
            simSummary += getOneReplicate(combo,locus,rep)
        os.chdir('../')
    createResultFile(combo, simSummary)
        
