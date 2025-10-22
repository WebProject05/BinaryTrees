def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr



arr1 = [0,4,1,0,8,2,9,8,7]
insertionSort(arr1)