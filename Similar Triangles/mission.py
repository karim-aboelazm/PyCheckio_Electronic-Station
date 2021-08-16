from typing import List, Tuple
Coords = List[Tuple[int, int]]
def cut_length(a,b):
    s=(a[0]-b[0])**2+(a[1]-b[1])**2 #????? ??????? ? ????????
    return s
def triangle(x):
    side1 = cut_length(x[0],x[1]) #??????? ?????? ???????
    side2 = cut_length(x[1],x[2]) #??????? ?????? ???????
    side3 = cut_length(x[0],x[2]) #??????? ??????? ???????
    a=sorted([side1, side2, side3])
    return a
def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    w1=triangle(coords_1) #???????? ???? ?????? ??????? ????????????
    w2=triangle(coords_2) #???????? ???? ?????? ??????? ????????????
    if w1[0]/w2[0]==w1[1]/w2[1] and w1[0]/w2[0]==w1[2]/w2[2]:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
