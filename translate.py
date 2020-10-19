import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
a = np.load('boston_housing.npy')
print(a)
np.savetxt("a.txt",a,fmt="%s",newline="\n")