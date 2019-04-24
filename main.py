import itertools
import subprocess
import os

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
        seed+=1

    
# test code
# createSimCtl(sim_params, sim_combinations[40], 2, 1)
# createSimCtl(sim_params, sim_combinations[40], 2, 2)



