def small_element(A):
    return A[1]

def right_son(A,i):
    return A[2 * i]

def left_son(A, i):
    return A[2 * i + 1]

def dad(A,i):
    return A[i // 2]