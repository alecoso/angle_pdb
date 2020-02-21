
import numpy
import prody
import os
import matplotlib.pyplot as  plt
from sys import argv

script,filename,folder_pdb,folder_mrc = argv

# cargo la proteína
p = prody.parsePDB(filename)
# divido por aminoácidos
aminos = p.getResnames()
# esto me da un vector con los tipos de aminoácidos que tiene esa proteína
types = set(p.getResnames())

try:
    os.makedirs('.//'+folder_pdb)
except:
    pass

try:
    os.makedirs('.//'+folder_mrc)
except:
    pass

## este diccionario es sobre los tipos de aminoacidos y su cantidad de moléculas
type_amino = {'ALA':5,'ARG':11,'ASN':8,'ASP':8,'GLN':9,'GLU':9,'GLY':4,'HIS':10,'ILE':8,'LEU':8 ,'LYS':9,'MET':8,'PHE':11, 'PRO': 7, 'SER':6,'THR':7,'TRP':14,'TYR':12,'VAL':7}

for i in types:
    ## Genero las carpetas
    try:
        os.makedirs('./' + folder_pdb + '/' + str(i))
    except:
        pass
    try:
        os.makedirs('./'+folder_mrc+'/'+str(i))
    except:
        pass

    # elijo el tipo de aminoácido correspondiente
    sel = p.select('resname '+str(i))

    for j in range(len(sel) // type_amino[i]):
        ind = j * type_amino[i]
        try :
            prody.writePDB('./'+folder_pdb+'/'+ str(i) + '/amino'+ str(j)+'.pdb', sel[int(ind):int(ind) + type_amino[i]])
        except:
            pass











