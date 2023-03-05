
import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Write this function

    tree = [[] for i in range (n)]

    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)


    root = np.where(parents == -1)[0][0]
    queue = [(root, 0)]
    max_height = 0

    while queue:
        node, height = queue.pop(0)
        max_height = max(max_height, height)
        for child in tree[node]:
            queue.append((child, height + 1))  
    return max_height + 1


def main():
    # implement input form keyboard and from files
    text = input()
    n = 0
    parents = []
    if text[0]=="I":
        n = int(input())
        arr= input()
        parents = [int(x) for x in arr.split()]
    elif text[0]=="F":
        file_name = "test/"
        file_name= file_name + input()
        if "a" in file_name:
            return
        with open(file_name, 'r') as file:
            text= file.read()
            lines = text.split('\n')
            n = int(lines[0])
            parents = [int(x) for x in arr.split()]
    print(compute_height(n, parents))
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()