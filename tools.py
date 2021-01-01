import function
import numpy as np
def Reproduction(name,after,size,polygon_number):
    origin = function.Operate(None, 'read', name)
    new = []
    for i in range(after):
        new.append(function.Variation(origin,polygon_number,'hard',100,size))
    function.Operate(new, 'write', 'reproduction.npy')

if __name__ == '__main__':
    Reproduction('best.npy',30,(341, 351),4)
    
