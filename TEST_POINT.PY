from point_ import Point
def test():
    p1=Point(2,3)
    p2=Point(4,5)
    print(p1)

    print(p1+p2)
    print(p1.calculate_distance(p2))
    print(p1-p2)
    print(p1*p2)
    print(p1/p2)
    p1.x=5
    p2.y=10
    print(p1)
    print(p2)

if __name__=="__main__":
    test()
