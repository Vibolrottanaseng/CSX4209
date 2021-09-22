import numpy as np


print('GA Simulation: a + 2b + 3c + 4d = 30 where (1 <= {a,b,c,d} < 30)')
print('----------------------------------------------------------------')
print('chromosome No. \t\t chromosome \t\t Fitness \t\t Fitness Rate(%)  ')
print()
lst = []
lst1 = []
sum = 0
for i in range(5):
    array = np.random.randint(low=1, high=30, size=(4))
    fitness = (array[0] + 2*array[1] +
               array[2] + 4*array[3]) - 30
    mifv = 1/fitness
    lst.append(mifv)
    FR = float((mifv/np.sum(lst))*100)
    print('\tC', i, '\t\t', array, '\t\t',
          fitness, '\t\t', '\t', round(FR, 2))
