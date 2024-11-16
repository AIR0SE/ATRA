from pathlib import Path
folderpath = Path.cwd()
program_path= str(folderpath) + "\\C.s_Project_parth\\system.py"
string=\
'''
tup_form={}
program_path=''
for i in tup_form:
   program_path+=i
print(program_path)

import os
from os.path import abspath, dirname
os.chdir(dirname(abspath(program_path)))
os.system(program_path)
'''
with open('ATRA.py','w') as f:
    f.write(string.format(tuple(program_path)))
