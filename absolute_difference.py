print('Welcome to absolute diffference calculator.')

size = int(input('Please array size: '))

array = []
#We split every element in the array with " " a space
array = input('Enter array elements: ').split(' ', size)

for i in range(size):
    array[i] = int(array[i])

#Setting an initial value for the variable
minimum_diff = array[0] - array[1]

for i in range(size):
    for j in range(i+1, size):
        if abs(array[i]-array[j]) < minimum_diff:
            minimum_diff = abs(array[i]-array[j])

else:
    print(minimum_diff)