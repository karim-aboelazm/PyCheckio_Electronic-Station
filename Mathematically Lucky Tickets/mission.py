from itertools import product
_operations = [lambda a, b: a+b, lambda a, b: a-b, lambda a, b: a*b, lambda a, b: a/b if b != 0 else None]
def checkio(data):
    def c_gen(s):
        yield int(s)
        yield from filter(lambda n: n != None, ([op(l, r) for i in range(1, len(s))
                                                for l, r, op in product(c_gen(s[:i]), c_gen(s[i:]), _operations)]))
    return not any([e == 100 for e in c_gen(data)])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
