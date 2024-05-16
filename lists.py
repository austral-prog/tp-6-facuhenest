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

sample_input = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(sample_input))  # Output: ['Green', 'White', 'Black']

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    indice_final = len(list_to_add_elements)
    list_to_add_elements.insert(indice_final, "Yellow")
    return list_to_add_elements


sample_input = ['Red', 'Green', 'White', 'Black']
print(add_elements(sample_input))  

def is_empty(list_to_check):
    return len(list_to_check) == 0

print(is_empty([]))        
print(is_empty([1, 2, 3]))  

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    return False

print(check_lists([1, 2, 3], [4, 5, 3]))  
print(check_lists([1, 2, 3], [4, 5, 6]))   
print(check_lists([1, 2], [4, 5, 6]))     
print(check_lists([1, 2, 3], [4, 5]))     



def list_of_lists(list_of_lists_to_modify):
    modifications = []
    
    # Ensure that list_of_lists_to_modify has at least three sublists
    while len(list_of_lists_to_modify) < 3:
        list_of_lists_to_modify.append([])
    
    # Modify the first sublist
    if len(list_of_lists_to_modify[0]) == 0:
        first_modification = []
    elif len(list_of_lists_to_modify[0]) == 1:
        first_modification = [list_of_lists_to_modify[0][0]]
    else:
        first_modification = list_of_lists_to_modify[0][:2]
    modifications.append(first_modification)
    
    # Modify the second sublist
    if len(list_of_lists_to_modify[1]) < 2:
        second_modification = []
    elif len(list_of_lists_to_modify[1]) <= 4:
        second_modification = list_of_lists_to_modify[1][1:]
    else:
        second_modification = list_of_lists_to_modify[1][1:4]
    modifications.append(second_modification)
    
    # Modify the third sublist
    if len(list_of_lists_to_modify[2]) == 0:
        third_modification = []
    elif len(list_of_lists_to_modify[2]) == 1:
        third_modification = [list_of_lists_to_modify[2][0]]
    else:
        third_modification = list_of_lists_to_modify[2][-2:]
    modifications.append(third_modification)
    
    return modifications
