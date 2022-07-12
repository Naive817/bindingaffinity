from pymol import cmd
import pandas as pd
#works with Equibind,automatically calculate a ligand's RMSD between two conformations
def RMSD(i):
    if os.path.exists(os.path.join(r"D:/mystuff/test", i)) and os.path.exists(os.path.join(r"D:\Python\EquiBind\testing_output", i)):
        ref = r"D:/mystuff/test/{}/{}_ligand.sdf".format(i,i)
        probe = r"D:\Python\EquiBind\testing_output/{}/lig_equibind_corrected.sdf".format(i,i)
        cmd.load(ref,i)
        cmd.load(probe)
        a= cmd.align(i, "lig_equibind_corrected")[0]
        print(i,a)
        cmd.delete(i)
        cmd.delete('lig_equibind_corrected')
        cmd.delete('all')
        return a
    else:
        print("error")
        return 0

d=r"D:/mystuff/equibind/fep binding affinity data.csv"
df = pd.read_csv(d)
l=df.loc[:,'PDB']
for i in l:
    RMSD(i)


cmd.extend("RMSD", RMSD)
