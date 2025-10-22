from insertionSort import insertionSort
import math

def bucketSort(arr):
  if len(arr) == 0:
    return arr

  numBuckets = round(math.sqrt(len(arr)))
  maxValue = max(arr)
  tempArr = [[] for _ in range(numBuckets)]

  # distribute elements into buckets
  for j in arr:
    index_b = int(j * numBuckets / (maxValue + 1))
    tempArr[index_b].append(j)

  # sort individual buckets
  for i in range(numBuckets):
    tempArr[i] = insertionSort(tempArr[i])

  # merge sorted buckets
  k = 0
  for i in range(numBuckets):
    for j in range(len(tempArr[i])):
      arr[k] = tempArr[i][j]
      k += 1

  return arr


customList = [9, 0, 2, 1, 3, 5, 2, 5, 1]
print(bucketSort(customList))
