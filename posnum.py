# to count positive numbers in a List

list = [-1, -2, -3, -4, 1, 2, 3]

pve = [num for num in list if num >= 1]
pve_count = len(pve)

print("Positive numbers in the list: ", pve_count)
