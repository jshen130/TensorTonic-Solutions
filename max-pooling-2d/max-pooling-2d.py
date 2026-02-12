def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    # Write code here
    m, n = len(X), len(X[0])  # list, not matrix, can't use X.shape
    output = [[0]*(n//pool_size) for _ in range(m//pool_size)]
    # iterate through the number of pools
    for i in range(m//pool_size):
        for j in range(n//pool_size):
            row_start = i*pool_size
            row_end = (i+1)*pool_size
            col_start = j*pool_size
            col_end = (j+1)*pool_size
            output[i][j] = max(max(row[col_start:col_end]) for row in X[row_start:row_end])
    return output