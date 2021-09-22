
import math
from math import sqrt

Name = ['Bill', 'Henry', 'Mary',
        'Sally', 'John', 'Carl']
age = [32, 40, 16, 15, 15, 20]
gender = [0, 0, 1, 1, 0, 0]
Singer = ['Rolling Stone', 'Neither', 'Taylor Swift',
          'Rolling Stone', 'Taylor Swift', 'Neither']


def output():
    print()
    print('===================================================================================================')
    print('================ KNN Classifier to classify New Instance IRIS =====================================')
    print('===================================================================================================')
    print('')
    print('\t Name\t\t gender(Female=1,Male=0)\t\t age\t\t Singer')
    print('\t ----\t\t -----------------------\t\t ---\t\t -------')
    print()


output()
for i in range(len(Name)):
    print('\t', Name[i], '\t\t\t', gender[i],
          '\t\t\t\t', age[i], '\t\t', Singer[i])
print('')
x = int(input('Enter age: '))
y = int(input('Enter gender(Female=1,Male=0): '))

print(' ')
print()
print('===========================================================================================================')
print('================ KNN Classifier to classify New Instance IRIS =============================================')
print('===========================================================================================================')
print('')
print('\t Name\t\t gender(Female=1,Male=0)\t age\t\t Singer\t\t\tdistance')
print('\t ----\t\t ----------------------\t\t ---\t\t -------\t\t---------')
print()
lst = []
for j in range(len(Name)):
    euclidea_distance = math.sqrt((x-age[j])**2 + (y-gender[j])**2)
    lst.append(round(euclidea_distance, 2))
    print('\t', Name[j], '\t\t\t', gender[j], '\t\t\t', age[j],
          '\t\t', Singer[j], '\t\t', round(euclidea_distance, 2))

print('')
if (y == 1):
    print('')
    print('Test Data Element <Age, Gender>: ', x, 'yrs', 'Female')
elif (y == 0):
    print('')
    print('Test Data Element <Age, Gender>: ', x, 'yrs', 'Male')
else:
    print('Error')
print('The 3 Nearest neighbors of test data with their distance are: ')
print()
lst.sort()

print('\tdistance')
print('\t--------')
print('\t', lst[0], '\t(K=1)')
print('\t', lst[1], '\t(K=2)')
print('\t', lst[2], '\t(k=3)')
print()
