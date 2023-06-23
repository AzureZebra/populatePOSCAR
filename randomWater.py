import scipy as sc
import numpy as np
import random as rng
f = open('POSCAR',"r")
lines = f.readlines()
g = open('POSCARnew',"w")


'''
line 1 = scaling
line 2, 3, 4 = vetors
line 6 = # of atoms
line 7 = SelDyn
line 8 = coordinate type


'''

scale = float(lines[1])
vec1 = np.array([float(j) for j in (lines[2].split())])
vec2 = np.array([float(j) for j in (lines[3].split())])
vec3 = np.array([float(j) for j in (lines[4].split())])

vol = abs(np.dot(vec1,np.cross(vec2,vec3)))*10**(-30)
#print(vol)
rho = 10**6 #g/m^3
NA = 6.023*10**23
mass = rho*vol #g
atomicMass = 18 #g/mol
mol = mass/atomicMass
totalAtoms = mol*NA
totalAtoms = int(totalAtoms)
oxyAtoms = int(3*totalAtoms/4)
nitAtoms = int(totalAtoms/4)
totalAtoms = oxyAtoms + nitAtoms 
#print(totalAtoms)

rng.seed(25)
rand = rng.random()
print(rand)
scaleFac = totalAtoms**(1/3) #length scaling factor
intFac = int(scaleFac)+1

for line in lines[:5]:
    g.write(line)

#line[5]
newLine = [j for j in lines[5]]
g.write(str("O") + "    " + str("H") + " ".join(newLine))
newLine = [j for j in lines[6]]
g.write(str(totalAtoms) + "    " + str(2*totalAtoms) + " ".join(newLine))

g.write('Cartesian \n')
X = vec1/intFac
Y = vec2/intFac
Z = vec3/intFac
print(X)
'''
given number
choose! totalAtoms positions from available positions 
rng.sample(XYZ,totalAtoms)

N = x + yX + zXY

'''

def randRot():
    tempMatrix = np.random.random((3,3))
    [tempQ, tempR] = np.linalg.qr(tempMatrix)
    return tempQ

OH_vec1 = np.array([1,0,0])
OH_vec2 = np.array([0,1,0])

samples = rng.sample(range(intFac**3),totalAtoms)

O_coords = []

for i in range(0,totalAtoms):
    pos = samples[i]
    x = int(pos%intFac)
    y = int(((pos-x)/intFac)%intFac)
    z = int(((pos-x-y*intFac)/intFac**2)%intFac)
    #print(x + rng.random(),y + rng.random(), z + rng.random())
    
    x = x + 0.5#rng.random()
    y = y + 0.5#rng.random()
    z = z + 0.15 + 0.7*rng.random()

    O_coord = x*X + y*Y + z*Z
    O_coords.append(O_coord)
    newLine = " ".join([str(j) for j in O_coord])
    g.write(newLine+ "   T   T   T"  +"\n")

for i in range(0,totalAtoms):
    O_pos = O_coords[i]
    Q = randRot()
    print(Q)
    OH_vec1_new = Q.dot(OH_vec1)  
    OH_vec2_new = Q.dot(OH_vec2)  
    OH1 =  O_pos + OH_vec1_new
    OH2 = O_pos + OH_vec2_new
    newLine = " ".join([str(j) for j in OH1])
    g.write(newLine+ "   T   T   T" + "\n")
    newLine = " ".join([str(j) for j in OH2])
    g.write(newLine+ "   T   T   T" + "\n")
print(totalAtoms)




for line in lines[9:]:
    g.write(line)
    '''coord = [float(j) for j in (line.split()[:3])]
    newCoord = scale*(coord[0]*vec1 + coord[1]*vec2 + coord[2]*vec3)
    
    newCoord = np.append(newCoord, (line.split()[3:]))
    newLine = " ".join([str(j) for j in newCoord])
    g.write(newLine+"\n")'''


'''    print(coord)
    print(newCoord)
    print(newLine)
    print(line)'''


'''
print(lines)
print(lines[7].split())
g = open('POSCAR.new',"w")
for line in lines:
    dat = [j for j in (line.split())]
    try:
        floatDat = [float(j) for j in (line.split())]
    except:
        pass

i    #print(line)
    if dat == ['Direct']:
        line = 'Cartesian\n'
        #print(dat)
    else:
        try:
            fDat = float(dat)
        except:
            pass

    g.write(line)
    #print(dat)
    joined = " ".join(dat)
    #print(joined)'''
f.close()
g.close()
