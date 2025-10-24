def swap(arr, index1, index2):
  temp = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = temp


def pivot(arr, pivotIndex, endIndex):
  swapIndex = pivotIndex
  for i in range(pivotIndex + 1, endIndex + 1):
    if arr[i] < arr[pivotIndex]:
      swapIndex += 1
      swap(arr, swapIndex, i)
  swap(arr, pivotIndex, swapIndex)

  return swapIndex


def quickSort(arr, left, right):
  if left < right:
    pivot_index = pivot(arr, left, right)
    quickSort(arr, left, pivot_index - 1)
    quickSort(arr, pivot_index + 1, right)

  return arr


myList = [2, 3, 7, 9, 0, 1]
print("Before:", myList)
pivotIndex = pivot(myList, 0, len(myList) - 1)
print("After: ", myList)
print("Pivot index:", pivotIndex)
finalList = quickSort(myList, 0, len(myList) - 1)
print("Sorted array:", myList)
