
tup_form=('C', ':', '\\', 'U', 's', 'e', 'r', 's', '\\', 'A', 'd', 'm', 'i', 'n', '\\', 'D', 'e', 's', 'k', 't', 'o', 'p', '\\', 'A', 'T', 'R', 'A', '\\', 'C', '.', 's', '_', 'P', 'r', 'o', 'j', 'e', 'c', 't', '_', 'p', 'a', 'r', 't', 'h', '\\', 's', 'y', 's', 't', 'e', 'm', '.', 'p', 'y')
program_path=''
for i in tup_form:
   program_path+=i
print(program_path)

import os
from os.path import abspath, dirname
os.chdir(dirname(abspath(program_path)))
os.system(program_path)
