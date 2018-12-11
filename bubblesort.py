"""
* Ryan Jenkins
* CSC 338 Group Project: Group 2
* bubbleSort.py
"""
import random
import multiprocessing as mp
import time


# Sort a list of elements using bubble sort then send the results to the parent process
def bubbleSort(conn, aList):
    #print("-> bubblesort.py -> bubbleSort()")
    #print(aList)
    startTime = time.time()
    noSwap = False
    while not noSwap:
        swapped = False
        for index in range(1, len(aList)):
            if aList[index - 1] > aList[index]:
                aList[index - 1], aList[index] = aList[index], aList[index - 1]
                swapped = True
        --len(aList)
        if not swapped:
            noSwap = True
    endTime = time.time()
    print("Bubble Sort Completed")
    #print(aList)
    conn.send([aList, endTime - startTime])
    conn.close()


# Main function call to test functionality of bubble bubbleSort
def main():
    print("-> bubblesort.py -> main()")
    lst = [i for i in range(100)]
    random.shuffle(lst)
    print(lst)
    bubbleSort(lst)
    print(lst)

if __name__ == "__main__":
    main()
