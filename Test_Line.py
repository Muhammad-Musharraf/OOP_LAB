from line import Line
from point_ import Point

def test():
    p1=Point(8,9)
    p2=Point(7,3)
    l1=Line(p1,p2)
    print(p1)
    p1.x=20
    p1.y=25
    print(p1)
    print(p1.calculate_distance(p2))
    print(l1)


if __name__=="__main__":
    test()
    