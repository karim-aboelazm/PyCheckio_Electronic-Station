from typing import List


def is_family(tree: List[List[str]]) -> bool:
    ancestor = {elem: set() for elem in sum(tree, [])}
    for parent, child in tree:
        if (ancestor[parent] | {parent}) & (ancestor[child] | {child}):
            return False
        ancestor[child] |= ancestor[parent] | {parent}

    result = list(child for _, child in tree)
    return len(result) == len(set(result)) and \
        list(ancestor.values()).count(set()) == 1


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father to your brother?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    assert is_family([
      ['Jack', 'Mike'],
      ['Logan',  'Mike'],
      ['Logan', 'Jack'],
    ]) == False, 'Two fathers'
    print("Looks like you know everything. It is time for 'Check'!")
