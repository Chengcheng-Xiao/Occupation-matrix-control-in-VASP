#!/usr/bin/env python
from __future__ import print_function
import sys

#----------------------------------------------------------------------
##  BLOCK OF FUNCTIONS USED IN THE MAIN CODE
#----------------------------------------------------------------------
def read_poscar():

    ''' a subroutine to number of atoms in POSCAR file'''

    file = open('POSCAR', "r")
    content = [x.rstrip("\n") for x in file]
    natom = content[6].split()
    natoms  = [int(i) for i in natom]
    file.close()
    return natoms

def read_input():
    LDAUL   = [int(i) for i in sys.argv[2:]]
    mode    = sys.argv[1]
    return LDAUL, mode

def read_OUTCAR(natoms, LDAUL, mode):

    ''' readin OUTCAR and out put OCCMATRIX files'''

    file = open('OUTCAR',"r")
    content = [x.rstrip("\n") for x in file]
    data = [x.split()[:] for x in content[:]]
    readdata = False
    OCCMAT_count = 0
    line_1 = 0
    count = 0
    total_line_num = 0

    for i in range(len(natoms)):
            total_line_num += (16+8*LDAUL[i])*natoms[i]

    if mode == "with_o":
        for line in data:
            count += 1
            if len(line) > 2 and line[0] == "atom" and line[2] == "1":
                line_1 = count
                readdata = True
                OCCMAT_count += 1
                f=open('OCCMATRIX'+str(OCCMAT_count), 'w')

            if count < line_1+total_line_num and readdata == True:
                if not content[count-1].startswith(" occupancies and") and not content[count-1].startswith(" onsite density") and not content[count-1].startswith("atom ") and len(data[count-1]) == 0:
                    print(content[count-1],file=f)
                elif content[count-1].startswith("atom "):
                    print('\n{0:d}   {1:d} 2'.format(int(data[count-1][2]), int(data[count-1][8])),file=f)
    else:
        for line in data:
            count += 1
            if len(line) > 2 and line[0] == "atom" and line[2] == "1":
                line_1 = count
                readdata = True
                OCCMAT_count += 1
                f=open('OCCMATRIX'+str(OCCMAT_count), 'w')

            if count < line_1+total_line_num and readdata == True:
                if not content[count-1].startswith("  o =") and not content[count-1].startswith(" occupancies and") and not content[count-1].startswith(" onsite density") and not content[count-1].startswith("atom ") and not len(data[count-1]) == 0:
                    print(content[count-1],file=f)
                elif content[count-1].startswith("atom "):
                    print('\n{0:d}   {1:d} 2'.format(int(data[count-1][2]), int(data[count-1][8])),file=f)


#----------------------------------------------------------------------
##  MAIN CODE
#----------------------------------------------------------------------
if __name__ == '__main__':
    nat = read_poscar()
    LDAUL,mode = read_input()
    read_OUTCAR(nat,LDAUL,mode)
