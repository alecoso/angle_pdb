
## Primero ejecutamos el main_total, pero solo la parte de generar los pdb

## Levantar cada pdb y guardar la orientación de cada uno

import os
import prody

# direccion de la proteína
filename = './data/chain.pdb'
# filename = './data/1pdfprueba2_1048.pdb'

# nombres de las carpetas donde van a estar lo aminoácidos en .pdb y el mapa de densidades en mrc
folder_pdb = 'Aminoacidos_pdb'
folder_mrc = 'Aminoacidos_mrc'


p = prody.parsePDB(filename)

type_amino = {'ALA':5,'ARG':11,'ASN':8,'ASP':8,'GLN':9,'GLU':9,'GLY':4,'HIS':10,'ILE':8,'LEU':8 ,'LYS':9,'MET':8,'PHE':11, 'PRO': 7, 'SER':6,'THR':7,'TRP':14,'TYR':12,'VAL':7}
# esto simplemente toma que tipos de aminoácidos presenta esa proteína
types = set(p.getResnames())

for folder_amino in types:
    # Me fijo que cantidad de archivos .pdb hay para saber cuanto tengo que iterar
    p1 = prody.parsePDB(".\\" + folder_pdb + "\\" + folder_amino + "\\amino" + str(0) + ".pdb")
    cant_arch = len(os.listdir('.\\'+folder_pdb+'\\'+folder_amino+'\\'))

    for num in range(cant_arch):
        file = ".\\"+folder_pdb+"\\"+folder_amino+"\\amino"+str(num)+".pdb"
        p2 = prody.parsePDB(file)
        p3, t = prody.superpose(p2, p1)
        file3 = ".\\" + folder_pdb + "\\" + folder_amino + "\\amino" + str(num) + "_aligned.pdb"
        prody.writePDB(file3, p3)



