

import os
import prody

# direccion de la proteína
filename = './data/chain.pdb'
# filename = './data/1pdfprueba2_1048.pdb'

# nombres de las carpetas donde van a estar lo aminoácidos en .pdb y el mapa de densidades en mrc
folder_pdb = 'Aminoacidos_pdb'
folder_mrc = 'Aminoacidos_mrc'

# esto ejecuta el script main_prody_all.py, le pasamos de argumentos la direccion de la proteína,
# y las carpetas de los aminoácidos
os.system("C:\\Users\\aleja\\AppData\\Local\\Programs\\Python\\Python37\\python.exe main_prody_all.py "+filename+' '+folder_pdb+' '+folder_mrc)

# esto carga la proteína
p = prody.parsePDB(filename)


# este diccionario es sobre los tipos de aminoacidos y su cantidad de moléculas
type_amino = {'ALA':5,'ARG':11,'ASN':8,'ASP':8,'GLN':9,'GLU':9,'GLY':4,'HIS':10,'ILE':8,'LEU':8 ,'LYS':9,'MET':8,'PHE':11, 'PRO': 7, 'SER':6,'THR':7,'TRP':14,'TYR':12,'VAL':7}
# esto simplemente toma que tipos de aminoácidos presenta esa proteína
types = set(p.getResnames())
#
# # itero en todos los tipos de aminoácidos
# for folder_amino in types:
#     # Me fijo que cantidad de archivos .pdb hay para saber cuanto tengo que iterar
#     cant_arch = len(os.listdir('.\\'+folder_pdb+'\\'+folder_amino+'\\'))
#     for num in range(cant_arch):
#         # uso el chimera para generar el mapa de densidades y guardarlo en la carpeta correspondiente
#         os.system("chimera --nogui  --nostatus --script \"density_map_chimera.py " +str(num)+ ' ' +folder_amino+' ' +folder_mrc+"\" -- .\\"+folder_pdb+"\\"+folder_amino+"\\amino"+str(num)+".pdb")







