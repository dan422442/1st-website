def A100613(n): # based on second formula in A018805
    if n == 0:
        return 0
    c, j = 1, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*(k1**2-A100613(k1))
        j, k1 = j2, n//j2
