def move_zeros(a_list):
    zeros = []
    while 0 in a_list:
         a_list.remove(0)     
         zeros.append(0)
    return a_list + zeros
