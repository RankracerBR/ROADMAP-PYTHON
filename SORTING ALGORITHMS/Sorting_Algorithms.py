from random import randint
from timeit import repeat

ARRAY_LENGTH = 10000
array = [8,2,6,4,5]
print(sorted(array))

def bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        '''
        create a flag that will allow the function to
        terminate early if there's nothing left to sort
        '''
        already_sorted = True
        
        '''
        Start looking at each item of the list one by one,
        comparing it with its adjacent value. With each
        iteration, the portion of the array that you look at
        shrinks because the remaining
        '''
        for j in range(n - i -1):
            if array[j] > array[j + 1]:
                '''
                if the item you're looking at is greater than its
                adjacent value, then swap them
                '''
                array[j], array[j +1] = array[j + 1], array[j]
                '''
                Since you have no swaps during the last iteration,
                the array is already sorted, and you can terminate
                '''
                already_sorted = False
        
        '''
        If there were no swaps during the last iteration,
        the array is already sorted, and you can terminate
        '''    
        if already_sorted:
            break
    
    return array

def run_sorting_algorithm(algorithm, array):
    '''
    Set up the context and prepare the call to the specified
    algorithm using the supplied array. Only import the
    algorithm function if it' not the buil-in `sorted()`.
    '''
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else "" # imports the name of the algorithm using the magic of Python’s f-strings. This is so that timeit.repeat() knows where to call the algorithm from
    
    stmt = f"{algorithm} ({array})" #prepares the call to the algorithm with the supplied array. This is the statement that will be executed and timed.
     
    '''
    Execute the code ten different times and return the time
    in seconds that each execution took
    '''
    times = repeat(setup=setup_code,stmt=stmt , repeat=3, number = 10) #calls timeit.repeat() with the setup code and the statement. This will call the specified sorting algorithm ten times, returning the number of seconds each one of these executions took
    
    '''
    Finally, display the name of the algorithm and the 
    minimun time it took to run
    '''
    print(f'Algorithm: {algorithm}. Minimun execution time: {min(times)}') #identifies the shortest time returned and prints it along with the name of the algorithm.

if __name__ == "__main__":
    '''
    Generate an array of `ARRAY_LENGTH` items consisting
    of random integer values between 0 and 999
    '''
    array = [randint(0,1000) for i in range(ARRAY_LENGTH)]
    
    '''
    Call the function using the name of the sorting algorithm
    and the array you just created
    '''
    run_sorting_algorithm(algorithm="bubble_sort", array=array)

def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    '''
    Loop from the second element of the array until
    the last element
    '''
    for i in range(left + 1, right + 1):
        '''
        This is the element we want to position in its
        correct place
        '''
        key_item = array[i]
        
        '''
        Initialize the variable that will be used to
        find the correct position of the element referenced
        by `key_item`
        '''
        j = i - 1
        
        '''
        Run through the list of items (the left 
        portion of the array) and find the correct position
        of the element referenced by `key_item`. Do this only
        if `key_item` is smaller than its adjacent values. 
        '''
        while j >= left and array[j] > key_item:
            '''
            Shift the value one position to the left
            and reposition j to point to the next element
            (from right to left)
            '''
            array[j + 1] = array[j]
            j -= 1
        
        '''
        When you finish shifting the elements, you can position
        `key_item` in its correct location
        '''
        array[j + 1] = key_item

def merge(left,right):
    '''
    If the first array is empty, then nothing needs
    to be merged, and can return the second array as the result
    '''
    if len(left) == 0:
        return right

    '''
    If the second array is empty, then nothing needs
    to be merged and you can return the first array as the result
    '''
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    '''
    Now go through both arrays until all the elements
    make it into the resultant array
    '''
    while len(result) < len(left) + len(right):
        '''
        The elements need to be sorted to add them to the 
        resultant array, so you need to decide whether to get 
        the next element from the first or the second array
        '''
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        '''
        If you reach the end of either array, then you can
        add the remaining elements from the other array to
        the result and break the loop
        '''
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    '''
    If the input array contains fewer than two elements,
    the return it as the result of the function
    '''
    if len(array) < 2:
        return array
    
    midpoint = len(array) // 2
    '''
    Sort the array by recursively splitting the input
    into two equal halves, sorting each half and merging them
    together into the final result
    '''
    return merge(
        left = merge_sort(array[:midpoint]),
        right = merge_sort(array[midpoint:])
    
)


def quicksort(array):
    '''
    If the input array contains fewer than two elements,
    then return it as the result of the function
    '''
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    '''
    Select your `pivot` element randomly
    '''
    pivot = array[randint(0, len(array) -1)]
    
    for item in array:
        '''
        Elements that are smaller than the `pivot` go to 
        the `low` list. Elements that are larger than 
        `pivot` go to the `high` list. Elements that are
        equal to `pivot` go to the `same` list.
        '''
        if item < pivot:
            low.append(item)

        elif item == pivot:
            same.append(item)

        elif item > pivot:
            high.append(item)

    '''
    The final result combines the sorted `low` list
    with the `same` list and the sorted `high` list
    '''
    return quicksort(low) + same + quicksort(high)

def timsort(array):
    min_run = 32
    n = len(array)
    
    '''
    Start by slicing and sorting small portions of the
    input array. The size of these slices is defined by
    your `min_run` size.
    '''
    for i in range(0, n, min_run):
        insertion_sort(array, i, min(( i + min_run - 1), n -1))
  
    '''
    Now you can start merging the sorted slices.
    Start from `min_run`, doubling the size on 
    each iteratiion until you surpass the length of
    the array
    '''
    size = min_run
    while size < n:
        '''
        Determine the arrays that will
        be merged together
        '''
        for start in range(0, n, size * 2):
            '''
            Compute the `mindpoint` ( where the first array ends
            and the second starts) and the `endpoint` (where 
            the second array ends)
            '''
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            
            '''
            Merge the two subarrays.
            The `left` array should go from `start` to
            `midpoint + 1`, while the `right` array should
            go from `midpoint + 1` to `end + 1`.
            '''
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end +1])
            
            '''
            Finally, put the merged array back into
            your array
            '''
            array[start:start + len(merged_array)] = merged_array
        
        '''
        Each iteration should double the size of your arrays
        '''
        size *= 2
    
    return array

if __name__ == "__main__":
    # Generate a sorted array of ARRAY_LENGTH items
    array = [i for i in range(ARRAY_LENGTH)]

    # Call each of the functions
    run_sorting_algorithm(algorithm="insertion_sort", array=array)
    run_sorting_algorithm(algorithm="merge_sort", array=array)
    run_sorting_algorithm(algorithm="quicksort", array=array)
    run_sorting_algorithm(algorithm="timsort", array=array)