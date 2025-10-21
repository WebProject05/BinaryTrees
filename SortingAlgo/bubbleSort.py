def bubbleSort(arr):
  for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
      if (arr[j] > arr[j + 1]):
        arr[j], arr[j+1] = arr[j+1], arr[j]
  
  print(arr)

customList = [1,4,2,0,1,9]
bubbleSort(customList)