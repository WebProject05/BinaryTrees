class Heap:
    def __init__(self, size):
        self.customList = [None] * (size + 1)  # Corrected list initialization
        self.heapSize = 0
        self.maxSize = size + 1

def peekOfHeap(rootNode):
    if not rootNode or rootNode.heapSize == 0:
        return None
    else:
        return rootNode.customList[1]

def sizeOfHeap(rootNode):
    if not rootNode:
        return 0
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode or rootNode.heapSize == 0:
        print("Heap is empty")
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i], end=" ")
        print()

newBinaryHeap = Heap(5)

newBinaryHeap.customList[1] = 10
newBinaryHeap.customList[2] = 20
newBinaryHeap.customList[3] = 30
newBinaryHeap.customList[4] = 40
newBinaryHeap.heapSize = 4

levelOrderTraversal(newBinaryHeap)
