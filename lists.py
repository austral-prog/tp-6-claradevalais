def remove_elements(list_to_remove_elements):
    nueva_lista = list_to_remove_elements[:]  

    if len(nueva_lista) > 5:
        del nueva_lista[5]  

    if len(nueva_lista) > 4:
        del nueva_lista[4]  

    if len(nueva_lista) > 0:
        del nueva_lista[0]  
    return nueva_lista

def add_elements(list_to_add_elements):
    return ["Pink"] + list_to_add_elements + ["Yellow"] # Remove this line and implement


def is_empty(list_to_check):
    return len(list_to_check)==0 # Remove this line and implement


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2]      
    list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]     
    list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]     
    return list_of_lists_to_modify
