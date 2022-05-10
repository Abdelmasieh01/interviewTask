print('Welcome to absolute diffference calculator.')

size = int(input('Please array size: '))

array = []
#We split every element in the array with " " a space
array = input('Enter array elements: ').split(' ', size)

for i in range(size):
    array[i] = int(array[i])

minimum_diff = 10000

for i in range(size):
    for j in range(i+1, size):
        if abs(array[i]-array[j]) < minimum_diff:
            minimum_diff = abs(array[i]-array[j])

if minimum_diff == 10000:
    print('An error happened.')

else:
    print(minimum_diff)