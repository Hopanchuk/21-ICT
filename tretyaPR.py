def remove_duplicates(lst):
    return list(set(lst))

def sort_list(lst):
    numbers = sorted([item for item in lst if isinstance(item, int)])
    strings = sorted([item for item in lst if isinstance(item, str)])
    return numbers + strings

lst = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

lst_no_duplicates = remove_duplicates(lst)

sorted_lst = sort_list(lst_no_duplicates)

print(sorted_lst)
