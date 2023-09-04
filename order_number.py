

def input_array():
  
  

  array = []
  while True:
    element = input("Enter valid integer to continue or to stop press enter ")
    try:
      element = int(element)
      array.append(element)
    
    except ValueError:
     print("Invalid input. Please enter an integer.")
     break

    
      

  return array


array = input_array()
print("The array is:", array)
# We can also use sort function print("the sorted array is: ",list(sorted(array)))
#  but for better understanding:
for i in range(0, len(array)):
    for j in range(i+1, len(array)):
        if array[i] >= array[j]:
            temp =array[i]
            array[i] = array[j]
            array[j] = temp
print("The sorted array is: " ,array)
