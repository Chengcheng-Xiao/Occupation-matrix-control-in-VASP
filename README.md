# Occupation-matrix-control-in-VASP

Occupation matrix control sets the occupations used when calculating the DFT+U corrections. It does not directly change the electron distribution. In this way it will effectively encourage the occupations entered. This has two direct uses:

1. To set a specific electronic occupation.

2. To obtain localisation at a specific site (atom and location) and look for the minimum energy occupation.

Before getting into things, you might want to check out the following paper:

[Phys. Chem. Chem. Phys., 16, 21016-21031 (2014)](https://pubs.rsc.org/en/content/articlelanding/2014/cp/c4cp01083c#!divAbstract)

## Installing

Put `OCC_mod_vasp_5.4.4.patch` file in the root directory of your VASP distro and type:
```
$ patch -p0 < OCC_mod_vasp_5.4.4.patch
```

Then Compile VASP as usual.

## Usage
### Input
There are two ways to control occupation matrixes:
#### (1). Directly from `INCAR`
In the `INCAR` file, a new tag `OCCDIRX` (where X can equals to number 1-999) should be added for occupation control. The format of `OCCDIRX` follows:
```
loop_A:      |      loop_0 (first loop of loop_A)        | |     loop_0 (second loop of loop_A)      | ...
         --- --------------------------------------------- -------------------------------------------
loop_B:                |    loop_00    | |    loop_01    |          |    loop_10    | |   loop_11    | ...
                      ----------------- -----------------          ----------------- ----------------
Result:   A   B0 C0 D0  E00 F00 J00 H00   E01 F01 J01 H01  B1 C1 D1  E10 F10 J10 H10   E11 F11 J1 H11  ...
```
| NAME                   |                                            MEANING                                    |
|:----------------------:|:-------------------------------------------------------------------------------------:|
| `A`                    | number of atoms to be considered (loop_A based on this number).                       |
| `B`                    | Chosen TOM number, as written in `POSCAR`.                                            |
| `C`                    | Orbital quantum number (LDAUL).                                                       |
| `D`                    | Number of occupation matrix elements to manipulate (loop_B based on this number).     |
| `E`                    | First index of chosen occupation matrix element (1-16) (1:s, 2-4:p, 5-9:d, 10-16:f).  |
| `F`                    | Second index of chosen occupation matrix element (1-16) (1:s, 2-4:p, 5-9:d, 10-16:f). |
| `J`                    | Spin channel (1-up, 0-down).                                                          |
| `H`                    | Occupation (Up to 1.0).                                                               |

Or, if you prefer a more descriptive explanation :
```
No of atoms, No * (ATOM, LDAUL, No of elements, No of E *( i, j, spin, occ))
```
| NAME                     |                        MEANING                        |
|:------------------------:|:-----------------------------------------------------:|
|`No of atoms`             |number of atoms specified on this line.                |
|`Atom`                    |atom number in POSCAR.                                 |       
|`LDAUL`                   |orbital type (0-s, 1-p, 2-d, 3-f).                     |
|`No of elements`          |Number of occupation matrix elements set for this atom.|
|`i,j`                     |matrix element (1-16,1-16).                            |
|`spin`                    |which spin the occupation is for (1-up, 2-down).       |
|`occ`                     |the occupation (up to 1.0).                            |

Example: `OCCDIR1 = 2 1 3 1 13 13 1 1.0 2 3 1 13 13 1 1.0`

          two Atom to be considered:

          Atom 1 in POSCAR - f orbital, 1 element to set: 13-13 (f-3) up spin occupation set to 1.0

          Atom 2 in POSCAR - f orbital, 1 element to set: 13-13 (f-3) up spin occupation set to 1.0


#### (2). From `OCCMATRIX`
*ALTERNATIVELY*, one can use file `OCCMATRIX` as input for matrix control once tag `OCCEXT = 1` is set. The format of `OCCMATRIX` is similar as the output of `LDAUPRINT = 2`. See example below:
```
2                                         No of atoms to be specified
3   2 2                                   Atom No (in POSCAR), L, spin(2) or not (1)
spin component  1                         Not really important what is here !
   0.7997  0.3554 -0.0000 -0.0000 -0.0000
   0.3554  0.5269 -0.0000 -0.0000 -0.0000
  -0.0000 -0.0000  1.0225  0.0653  0.0575
  -0.0000 -0.0000  0.0653  0.7468 -0.3435
  -0.0000 -0.0000  0.0575 -0.3435  0.6179
spin component  2
   0.9057 -0.3651  0.0000 -0.0000  0.0000
  -0.3651  0.3291  0.0000 -0.0000  0.0000
   0.0000  0.0000  0.5578  0.4221  0.0993
  -0.0000 -0.0000  0.4221  0.5288  0.2056
   0.0000  0.0000  0.0993  0.2056  0.2269
                                          Blank line between atoms
4   2 2                                   Atom No (in POSCAR), L, spin(2) or not (1)
spin component 2                          Spins switched to give the AFM arrangement
   0.7997  0.3554 -0.0000 -0.0000 -0.0000
   0.3554  0.5269 -0.0000 -0.0000 -0.0000
  -0.0000 -0.0000  1.0225  0.0653  0.0575
  -0.0000 -0.0000  0.0653  0.7468 -0.3435
  -0.0000 -0.0000  0.0575 -0.3435  0.6179
spin component  1
   0.9057 -0.3651  0.0000 -0.0000  0.0000
  -0.3651  0.3291  0.0000 -0.0000  0.0000
   0.0000  0.0000  0.5578  0.4221  0.0993
  -0.0000 -0.0000  0.4221  0.5288  0.2056
   0.0000  0.0000  0.0993  0.2056  0.2269
```

*ALTERNATIVELY*, you can use the python script `extract_OCC.py` by:
```
python extract_OCC.py
```
this script will output all matrix elements from each electronic step only if `LDAUPRINT = 2` defined in the `INCAR`. We can visualize how the occupation matrix change with each step. Or change matrix occupation based on the output of this script.

### Procedure

In general cases:
1. Use occupation control and relax the structure.
2. Use relaxed structure with occupation control, do a SCF calculation.
3. Read `WAVECAR` from step 2, do a relax without the occupation control.
4. Use relaxed structure from step 3. Do a SCF calculation without occupation control.

## How to cite

For the method please cite the following paper in any publications arising from the use of this code:

J. P. Allen and G. W. Watson,
*Occupation matrix control of d- and f-electron localisations using DFT + U*, [Phys. Chem. Chem. Phys., 16, 21016-21031 (2014)](https://pubs.rsc.org/en/content/articlelanding/2014/cp/c4cp01083c#!divAbstract)

## More
More details can be found in the [pdf file](./Docs/Occupation\ matrix\ control\ in\ VASP.pdf).

## License
  This project is licensed under the MIT License - see the [LICENSE.md](./LICENSE.md) for details
