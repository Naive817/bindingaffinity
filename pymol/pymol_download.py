from pymol import cmd
import os

#downloads PDBs to a directory,one folder each

def download(i):
    if not os.path.exists(os.path.join(r"D:\mystuff\test", i)):
        os.mkdir(os.path.join(r"D:\mystuff\test",i))
    elif not os.path.exists(r"D:\mystuff\test\{}\{}.pdb".format(i, i)):
        print ("downloading {}".format(i))
        cmd.fetch (i,'protein','1')
        #time.sleep(10)
            #cmd.select ('protein' and not 'polymer') and not 'solvent'
            #cmd.extract ligand, sele
            #cmd.create pocket, byres protein within 5 of ligand
            #cmd.h_add ligand
        dir=r"D:/mystuff/test/{}/{}.pdb".format(i,i)
        cmd.save (dir,"protein")
        print("saving {}".format(i))
        #time.sleep(5)
        cmd.delete('protein')
        #time.sleep(5)
        cmd.delete('all')

#d=r"D:\mystuff\binding affinity data all.csv"
#df = pd.read_csv(d)
#l=df.loc[:,'PDB']
#for i in l:
    #download(i)

cmd.extend("download", download)