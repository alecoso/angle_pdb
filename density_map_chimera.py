

#import chimera

from sys import argv
from chimera import runCommand  as rc

script, num,folder_amino,folder_mrc = argv

rc('molmap # 1.5')
rc('volume #0.1 save .\\'+folder_mrc+'\\'+folder_amino+'\\data'+str(num)+'.mrc')

