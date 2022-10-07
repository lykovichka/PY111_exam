a = len(arr) - 1  # O(1)
out = list()  # O(1)
while a > 0: # O(log(n))
    out.append(arr[a]) # O(1)
    a = a // 1.7 # O(1)
out.merge_sort() # O(n)

print('O(n + log(n))')



