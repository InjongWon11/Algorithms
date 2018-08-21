def merge_sort(lst: list)->list:
    if len(lst) <= 1:
        return lst
    left_index = lst[:len(lst)//2]
    right_index = lst[len(lst)//2:]
    sorted_left = merge_sort(left_index)
    sorted_right = merge_sort(right_index)
    end_list = []
    left_index = 0
    right_index = 0
    while left_index < len(sorted_left) and right_index < len(sorted_right):
        if sorted_left[left_index] < sorted_right[right_index]:
            end_list.append(sorted_left[left_index])
            left_index += 1
        else:
            end_list.append(sorted_right[right_index])
            right_index += 1
    return end_list + sorted_left[left_index:] + sorted_right[right_index:]


def merge_lists(lst1: list, lst2: list) -> list:
    """Merge two lists together. """
    i, j = 0, 0
    merged_list = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    return merged_list + lst1[i:] + lst2[j:]


def mergesort_in_place(lst: list) -> None:
    """
    Sort lst in non-descending order using merge sort.
    """
    mergesort_in_place_helper(lst, 0, len(lst))


def mergesort_in_place_helper(lst,i:int, j:int)->None:
    """Sort  lst[i:j] in non - descending order.
    """
    # TODO: Make recursive calls
    if len(lst) == 1:
        return
    # left = lst[i:j][:len(lst)//2]
    # right = lst[i:j][len(lst)//2:]
    middle = len(lst) // 2
    mergesort_in_place_helper(lst, i, middle)
    mergesort_in_place_helper(lst, middle,j)
    lst[i:j] = merge_lists(lst[i:middle],lst[middle,j])


def quicksort_in_place(lst: list) -> None:
    """
    Sort lst in non-descending order using merge sort.
    """
    mergesort_in_place_helper(lst, 0, len(lst))


def quicksort_in_place_helper(lst: list, i: int, j: int) -> None:
    """
    Sort lst[i:j] in non-descending order.
    """
    # TODO: Make recursive calls
    if len(lst) == 1:
        return
    pivot_index = partition_list(lst, i, j)
    quicksort_in_place_helper(lst, i, pivot_index)
    quicksort_in_place_helper(lst, pivot_index+1, j)


def partition_list(lst, i: int, j: int):
    """ build something """
    pivot = lst[len(lst)//2]
    smaller = []
    same = []
    bigger = []
    for item in lst:
        if item < pivot:
            smaller.append(item)
        elif item == pivot:
            same.append(item)
        else:
            bigger.append(item)
    list[i:j] = smaller + same + bigger
    return i + len(smaller)



if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="lab_pyta.txt")
    lst =[8,9]
    quicksort_in_place_helper(lst,0,1)

