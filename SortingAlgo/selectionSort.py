def selectionSort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_idx]:
        min_idx = j
    if min_idx != i:
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
  print(arr)


arr1 = [0,3,1,3,2,9,6,10]
selectionSort(arr1)