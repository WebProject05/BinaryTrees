class Heap:
    def __init__(self, size):
        self.customList = [None] * (size + 1)
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


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return

    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:

            rootNode.customList[index], rootNode.customList[parentIndex] = (
                rootNode.customList[parentIndex],
                rootNode.customList[index],
            )
        heapifyTreeInsert(rootNode, parentIndex, heapType)

    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = (
                rootNode.customList[parentIndex],
                rootNode.customList[index],
            )
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The binary heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize = rootNode.heapSize + 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    # Case 1: no child
    if rootNode.heapSize < leftIndex:
        return

    # Case 2: only left child
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = (
                    rootNode.customList[leftIndex],
                    rootNode.customList[index],
                )
            return
        else:  # Max Heap
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = (
                    rootNode.customList[leftIndex],
                    rootNode.customList[index],
                )
            return

    # Case 3: two children
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] > rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = (
                    rootNode.customList[swapChild],
                    rootNode.customList[index],
                )
        else:  # Max Heap
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] < rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = (
                    rootNode.customList[swapChild],
                    rootNode.customList[index],
                )

        heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return "Heap is empty"

    extractedNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractedNode


def deleteTree(rootNode):
    rootNode.customList = None
    
# newBinaryHeap = Heap(5)

# newBinaryHeap.customList[1] = 10
# newBinaryHeap.customList[2] = 20
# newBinaryHeap.customList[3] = 30
# newBinaryHeap.customList[4] = 40
# newBinaryHeap.heapSize = 4

newHeap = Heap(5)

insertNode(newHeap, 10, "Min")
insertNode(newHeap, 32, "Min")
insertNode(newHeap, 11, "Min")
insertNode(newHeap, 1, "Min")


extractNode(newHeap, "Min")

levelOrderTraversal(newHeap)
