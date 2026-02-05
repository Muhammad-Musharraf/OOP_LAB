from vector_2d import Vector2D
def test():
    # Objects
    v1=Vector2D(4,8)
    v2=Vector2D(2,4)
   
    print(v1)  
    print("Magnitude",v1.magnitude())
    print("Normalize",v1.Normalize())

if __name__=="__main__":
    test()

