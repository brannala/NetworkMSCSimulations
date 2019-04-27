import itertools
import subprocess
import os
import time


# create a simulation control file
def createSimCtl(simPars, simComb, seed, rep):
    dir_name = 'sim' + ''.join(simComb)
    ctlfilename = dir_name + "/" + "simgen" + ''.join(simComb) + "." + str(rep) + ".ctl"
    varphi = simPars[0][int(simComb[0])]
    theta = simPars[1][int(simComb[1])]
    model = simPars[2][int(simComb[2])]
    tree = simPars[3][int(simComb[3])]
    noloci = simPars[4][int(simComb[4])]
    
    if rep==1:
        subprocess.call(["mkdir", dir_name])
        subprocess.call(["cp", "Imap.txt", dir_name])
    ctlfile = open(ctlfilename, "+w")
    ctlfile.write("seed = " + str(seed) + "\n")
    ctlfile.write("seqfile = sim" + ''.join(simComb) + "." + str(rep) + ".phy\n")
    ctlfile.write("Imapfile = Imap.txt\n")
    ctlfile.write("species&tree = 3   A  B  C\n")
    ctlfile.write("                   10 10 10\n")
    if tree == "c":
        ctlfile.write("((A #" + theta + ", (C #" + theta + ")H[&phi=" + varphi + ",&tau-parent=no] :0.01) S :0.01 #" + theta + ", (H[&tau-parent=no], B #" + theta + ") T :0.01 #" + theta + " )R :0.03 #" + theta + " ;\n")
    else:
        ctlfile.write("((A #" + theta + ", (C #" + theta + ")H[&phi=" + varphi + ",&tau-parent=yes] :0.01 #" + theta + ") S  :0.02 #" + theta + ", (H[&tau-parent=yes] #" + theta + ", B #" + theta + ") T :0.02 #" + theta + " )R :0.03 #" + theta + " ;\n")
    if model == "0":
        ctlfile.write("model=0\n")
    else:
        ctlfile.write("model = 7\n")
        ctlfile.write("Qrates = 0  7.72   3.16   3.24   3.18   2.69   7.45\n")
        ctlfile.write("basefreqs = 0  20.49 21.22 20.46 20.97\n")
        ctlfile.write("alpha_siterate = 0 20 4 4\n")
        ctlfile.write("modelparafile = para" + ''.join(simComb) + "." + str(rep) + ".txt\n")
    ctlfile.write("loci&length=" + noloci + " 500")
    ctlfile.close()
    

def createBppCtl(simPars, simComb, seed, rep):
    varphi = simPars[0][int(simComb[0])]
    theta = simPars[1][int(simComb[1])]
    noloci = simPars[4][int(simComb[4])]
    tree = simPars[3][int(simComb[3])]
    dir_name = 'sim' + ''.join(simComb)
    bppctlfilename = dir_name + "/" + "sim" + ''.join(simComb) + "." + str(rep) + ".ctl"
    bppctlfile = open(bppctlfilename, "+w")
    bppctlfile.write("seed = " + str(seed+10000) + "\n")
    bppctlfile.write("seqfile = sim" + ''.join(simComb) + "." + str(rep) + ".phy\n")
    bppctlfile.write("Imapfile = Imap.txt\n")
    bppctlfile.write("outfile = sim" + ''.join(simComb) + "." + str(rep) + ".out.txt\n")
    bppctlfile.write("mcmcfile = sim" + ''.join(simComb) + "." + str(rep) + ".mcmc.txt\n")
    bppctlfile.write("species&tree = 3   A  B  C\n")
    bppctlfile.write("                   10 10 10\n")
    if tree == "c":
        bppctlfile.write("((A, (C)H[&phi=0.5,&tau-parent=no])S, (H[&tau-parent=no], B) T)R;\n")
    else:
        bppctlfile.write("((A, (C)H[&phi=0.5,&tau-parent=yes])S, (H[&tau-parent=yes], B) T)R;\n")
    bppctlfile.write("usedata = 1\n")
    bppctlfile.write("nloci = " + noloci + "\n")
    bppctlfile.write("cleandata = 0\n")
    bppctlfile.write("thetaprior = 3 " + str(2.0*float(theta)) + " e\n")
    bppctlfile.write("tauprior = 3 0.04 \n")
    bppctlfile.write("phiprior = 1 1 \n")
    bppctlfile.write("finetune = 1: 21.06 .0002 .0003 .00001 .2 .01 .01 .01\n")
    bppctlfile.write("print = 1 0 0 0\n")
    bppctlfile.write("burnin = 20000\n")
    bppctlfile.write("sampfreq = 2\n")
    bppctlfile.write("nsample = 200000\n")

    
print('Generating control files for simulations...\n')
            
#define values for simulation parameters
varphi = ["0.1", "0.5"]
theta = ["0.001", "0.01"]
model = ["0", "7"]
tree = ["a", "c"]
loci = ["10", "100", "1000"]
sim_params = [varphi, theta, model, tree, loci]

# create vector of tuples with indexes of all possible parameter combinations
sim_iter = itertools.product('10', '10', '10', '10', '012')
sim_combinations = []
for it in sim_iter:
    sim_combinations.append(it)

# create all control files for simulations
seed=1;
for combo in sim_combinations:
    for i in range(1, 11):
        createSimCtl(sim_params, combo, seed, i)
        createBppCtl(sim_params, combo, seed, i)
        currdir = 'sim' + ''.join(combo)
        subprocess.call(["cp","bpp4",currdir])
        seed+=1

# wait 1 seconds
time.sleep(1)

# simulate sequences
choice = input("Simulate sequences? (y/n)")
if choice == 'y':
    first = True
    print('Simulating sequence data...\n')
    for combo in sim_combinations:
        print('simulating combination: ' + ''.join(combo) + '\n')
        currdir = 'sim' + ''.join(combo)
        if first:
            os.chdir(currdir)
            first=False
        else:
            os.chdir('../'+currdir)
        #        time.sleep(0.1)
        for i in range(1, 11):
            sf = " --simulate simgen" + ''.join(combo) + "." + str(i) + ".ctl"
            os.system('./bpp4' + sf + ' > screensim' + ''.join(combo) + '.' + str(i) + '.txt 2>&1')
    os.chdir('../')

# wait 2 seconds
time.sleep(2)

# spawn simulation runs
choice2 = input("Analyze simulated data? (y/n)")
if choice2 == 'y':
    first = True
    print('Spawning MCMC analyses of simulated data...\n')
    for combo in sim_combinations:
        print('spawning replicates for combination: ' + ''.join(combo) + '\n')
        currdir = 'sim' + ''.join(combo)
        if first:   
            os.chdir(currdir)
            first=False
        else:
            os.chdir('../'+currdir)
        for i in range(1, 11):
            cf = " --cfile sim" + ''.join(combo) + "." + str(i) + ".ctl"
            of = "screen" + ''.join(combo) + "." + str(i) + ".txt"
            os.system('./bpp4' + cf + ' > ' + of + ' 2>&1 &')
# os.chdir('../')


# currdir = 'sim' + ''.join(sim_combinations[1])
# os.chdir(currdir)
# cf = " --cfile sim" + ''.join(sim_combinations[1]) + "." + "1" + ".ctl"
# os.system('./bpp4' + cf + ' > out.txt 2>&1 &')


    
# test code
# createSimCtl(sim_params, sim_combinations[40], 2, 1)
# createSimCtl(sim_params, sim_combinations[40], 2, 2)



