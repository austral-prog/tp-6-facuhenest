def remove_elements(list_to_remove_elements):
    longitud = len(list_to_remove_elements)
    if longitud == 0:
        return list_to_remove_elements
    elif longitud <= 4:
        del list_to_remove_elements[0]
    elif longitud == 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    else:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements 

def is_empty(list_to_check):
    return len(list_to_check) == 0

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    return False

def list_of_lists(list_of_lists_to_modify):
    first_modification = []
    second_modification = []
    third_modification = []

    # modifico la primera línea
    if len(list_of_lists_to_modify[0]) == 1:
        first_modification = [list_of_lists_to_modify[0][0]]
    elif len(list_of_lists_to_modify[0]) > 1:
        first_modification = list_of_lists_to_modify[0][:2]

    # modifico la segunda línea
    if len(list_of_lists_to_modify[1]) >= 2:
        second_modification = list_of_lists_to_modify[1][1:4]

    # modifico la tercera lista
    if len(list_of_lists_to_modify[2]) == 1:
        third_modification = [list_of_lists_to_modify[2][0]]
    elif len(list_of_lists_to_modify[2]) > 1:
        third_modification = list_of_lists_to_modify[2][-2:]

    list_of_lists_to_modify[0] = first_modification
    list_of_lists_to_modify[1] = second_modification
    list_of_lists_to_modify[2] = third_modification

    return list_of_lists_to_modify
