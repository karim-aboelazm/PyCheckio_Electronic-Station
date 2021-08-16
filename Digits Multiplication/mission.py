def checkio(number: int) -> int:
    new_list = list(str(number))
    exclude_strlist = []
    for i in new_list:
        if int(i) != 0:
            exclude_strlist.append(int(i))
    a = 1
    for i in range(len(exclude_strlist)):
        a *= exclude_strlist[i]
    return a





if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
