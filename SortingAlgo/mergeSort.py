def merge(arr, l, m, r):
  n1 = m - l + 1
  n2 = r - m

  L = [0] * n1
  R = [0] * n2

  for i in range(n1):
    L[i] = arr[l + i]
  for j in range(n2):
    R[j] = arr[m + 1 + j]

  i = j = 0
  k = l

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1


def mergeSort(arr, l, r):
  if l < r:
    m = (l + r) // 2
    mergeSort(arr, l, m)
    mergeSort(arr, m + 1, r)
    merge(arr, l, m, r)


array = [0, 2, 3, 1, 9, 5, 3, 5, 9, 7, 5, 3, 6]
mergeSort(array, 0, len(array) - 1)
print(array)
