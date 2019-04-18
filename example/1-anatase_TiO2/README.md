## Anatase TiO2
### Introduction and Structure
The bulk anatase structure is shown in Fig. 1 and is orthorhombic in nature (space group I41/amd). It possess six-coordinate d0 Ti(IV) ions in a distorted octahedral environment and three-coordinate oxygen ions in a trigonal planar arrangement.

![FIG.1](./fig/FIG1.png)

The advantage of using the anatase polymorph over the more stable rutile form is that no rotation of the cell (or rotation of the occupation matrix) is required to ensure that the Ti–O bonds lie in the same planes as the principal axes, which is not the case for rutile.

### Folders
Folders contain:
```
|____OCC_change
| |__5-5 to 9-9:    Fixing occupation matrix elements (5,5), (6,6), (7,7), (8,8) and (9,9).
| |__SCF:           SCF with no occupation change.
| |__OPT_unitcell:  OPT of unitcell with no occupation change.
| |__OPT_primitive: OPT of primitive cell with no occupation change.
```

### Result

Spin density of `5-5`
![FIG.5-5](./fig/FIG5-5.png)

Spin density of `6-6`
![FIG.6-6](./fig/FIG6-6.png)

Spin density of `8-8`
![FIG.8-8](./fig/FIG8-8.png)

Fixing (7,7) and (9,9) will relax back to (5,5) and (6,6).

Spin density of `no_fix`
![FIG.no_fix](./fig/FIGno_fix.png)
