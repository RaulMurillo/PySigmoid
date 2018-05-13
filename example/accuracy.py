
from PySigmoid import Posit, set_posit_env
from math import log
from decimal import Decimal as D, getcontext
import numpy as np
import matplotlib.pyplot as plt

# 500 digits of precision
getcontext().prec = 500
def decacc(x, y):
    if x == y:
        return D('inf')
    else:
        try:
            return -abs((x / y).log10()).log10()
        except:
            return 0

set_posit_env(8, 1)

p = Posit()
p.set_bit_pattern(p.maxpos)
p = -p
while p.number <= p.maxpos:
    q = p
    q.sigmoid()
    xx.append(float(p))
    yy.append(float(q))
    p.number += 1
 
# Plot
plt.plot(xx, yy, alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()