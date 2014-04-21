#!/usr/bin/env python3

import os.path

#init
base_file = os.path.abspath("data/base.txt")
new_file = os.path.abspath("data/new.txt")
inc_file = os.path.abspath("data/increment.txt")
chg_file = os.path.abspath("data/change.txt")
sep = '|'
key_column = (0,)

finc = open(inc_file,'w')
fchg = open(chg_file,'w')

#base dict,  key:line
base_dict = {}
with open(base_file) as fbase:
    for line in fbase:
        tmp_list = line.split(sep)
        key_list = sep.join([ tmp_list[i] for i in key_column ])
        base_dict[hash(key_list)]=hash(line)

#new file
with open(new_file) as fnew:
    for line in fnew:
        tmp_list = line.split(sep)
        key_list = sep.join([ tmp_list[i] for i in key_column ])
        #compare keys
        if hash(key_list) in base_dict:
            #compare lines
            if hash(line)!=base_dict[hash(key_list)]:
                fchg.write(line)
        else:
            finc.write(line)

#clean
fchg.close()
finc.close()
