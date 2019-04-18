#!/usr/bin/env python
from __future__ import print_function

#----------------------------------------------------------------------
##  BLOCK OF FUNCTIONS USED IN THE MAIN CODE
#----------------------------------------------------------------------
def read_poscar():

    ''' a subroutine to number of atoms in POSCAR file'''

    file = open('POSCAR', "r")
    content = [x.rstrip("\n") for x in file]
    natom = content[6].split()
    natoms  = int(natom[0])+ int(natom[1])
    file.close()
    return natoms


def read_OUTCAR(natoms):

    ''' readin OUTCAR and out put OCCMATRIX files'''

    file = open('OUTCAR',"r")
    content = [x.rstrip("\n") for x in file]
    data = [x.split()[:] for x in content[:]]
    readdata = False
    OCCMAT_count = 0
    hardstop = 0
    count = 0

    for line in data:
        count += 1
        if len(line) > 2 and line[0] == "atom" and line[2] == "1":
            line_1 = count
            readdata = True
            OCCMAT_count += 1
            f=open('OCCMATRIX'+str(OCCMAT_count), 'w')
        if len(line) > 2 and line[0] == "atom" and line[2] == str(natoms):
            hardstop = count+((count-1)-(line_1-1))/(int(natoms)-1)

        if hardstop == count:
            readdata = False

        if readdata == True:
            print(content[count-1],file=f)

#----------------------------------------------------------------------
##  MAIN CODE
#----------------------------------------------------------------------
if __name__ == '__main__':
    nat = read_poscar()
    read_OUTCAR(nat)
