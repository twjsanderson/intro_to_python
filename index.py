first_list = [2, 3, 4, 5, 6, 7, 8, 9]

# Conditional loop
# Return new list > base
def conditional_loop(list, base):
    res = []
    for x in list:
        if x > base:
            res.append(x)
    return res

# Linear search
def linear_search(list, el):
    for x in list:
        if x == el:
            return str(el) + " is present at index " + str(list.index(el))
    return str(el) + " is not present in list"

# Is an entire string included in another string
def is_included(str1, str2):
    if (len(str1) < 1 or len(str2) < 1):
        return False

    if str1 in str2:
        return True

    return False

print('conditional_loop: ', conditional_loop(first_list, 5))
print('linear_search: ', linear_search(first_list, 211))
print('is_included: ', is_included('th', 'thssii'))

print('====================================================')

sec_list = [23, 53, 635, 6, 323, 432, 53453, 31]
third_list = [23, 23, 62, 53, 312, 635, 62, 3232, 4322, 534532, 312]

# Does list include duplicate v1
def has_duplicate1(list):
    first_el = list[0]
    length = len(list)
    i = 1

    if length == 1: return False

    while i < length:
        if first_el == list[i]: return True
        i += 1
    
    list.pop(0)
    return has_duplicate1(list)

# Does list include duplicates v2
# sets cannot have duplicates, you can use the .add() method on a set
def has_duplicate2(list):
    numbersChecked = set()
    for x in list:
        if x in numbersChecked: return True
        numbersChecked.add(x)
    return False

# Does list include duplicates v3
# sets cannot have duplicates, just compare lengths to confirm equality
def has_duplicate3(list):
    return len(list) != len(set(list))

# Show list of all duplicate elements
def show_duplicates(list):
    dups = []
    numbersChecked = set()
    for x in list:
        if x in numbersChecked: dups.append(x)
        numbersChecked.add(x)
    return dups

# Return list without duplicates
def remove_duplicates(list):
    no_dups = []
    numbersChecked = set()
    for x in list:
        if x not in numbersChecked: no_dups.append(x)
        numbersChecked.add(x)
    return no_dups

print('has_duplicate1: ', has_duplicate1(sec_list))
print('has_duplicate2: ', has_duplicate2(sec_list))
print('has_duplicate3: ', has_duplicate3(sec_list))
print('show_duplicates: ', show_duplicates(sec_list))
print('remove_duplicates: ', remove_duplicates(third_list))

print('====================================================')