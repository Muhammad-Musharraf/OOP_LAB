from line import Line
from point_ import Point
from shapes import Shapes

def main():
    p1=Point(0,0)
    p2=Point(4,0)
    p3=Point(4,3)
    p4=Point(0,3)


    l1=Line(p1,p2)
    l2=Line(p2,p3)
    l3=Line(p3,p4)
    l4=Line(p4,p1)

    #Shape
    rectangle=Shapes([l1,l2,l3,l4])
    rectangle.display()
    print()



    l1=Line(p1,p2)
    l2=Line(p2,p3)
    l3=Line(p3,p1)

    triangle=Shapes([l1,l2,l3])
    triangle.display()

    

    # square
    p5=Point(0,0)
    p6=Point(6,5)
    p7=Point(1,5)
    p8=Point(6,5)

    

    l5=Line(p5,p6)
    l6=Line(p6,p7)
    l7=Line(p7,p8)
    l8=Line(p8,p5)

    square=Shapes([l5,l6,l7,l8])
    square.display()








if __name__=="__main__":
    main()