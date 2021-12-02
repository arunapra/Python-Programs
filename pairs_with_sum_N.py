def print_pairs(arr,N):
    hash_set = set()

    for i in range(len(arr)):
        val = N-arr[i]
        if val in hash_set:
            print("Pairs "+str(arr[i])+", "+str(val))
        hash_set.add(arr[i])

arr = [5, 2, 40, 1, 9, 3]
N = 4
print_pairs(arr, N)
