def remove_dupls(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dupls(L1, L2)

# [2,3,4] as python overlooks 2 because it doesn't update the intenal counter
print(L1)
print(L2)
