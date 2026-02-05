import copy
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):

        return f"{self.i}i +{self.j}j +{self.k}k"
    
    def __add__(self,x):

        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
    def __sub__(self,x):

        return Vector(self.i-x.i,self.j-x.j,self.k-x.k)
    
    def __mul__(self,x):

        return Vector(self.i*x.i,self.j*x.j,self.k*x.k)
    
    def __truediv__(self,x):

        return Vector(self.i/x.i,self.j/x.j,self.k/x.k)
    
    def __floordiv__(self,x):

        return Vector(self.i//x.i,self.j//x.j,self.k//x.k)
    
    def __le__(self,x):
        return Vector(self.i<=x.i,self.j<=x.j,self.k<=x.i)
    
    def __ge__(self,x):
        return Vector(self.i>=x.i,self.j>=x.j,self.k>=x.i)
    
    


v1=Vector(9,8,8)
v2=Vector(9,3,8)

print("Original Vectors:")
print("v1 =", v1)
print("v2 =", v2)

v3=copy.copy(v1)
v4=copy.deepcopy(v1)

print('deep copy:',v4)



############################################
class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    
    def area(self):

        return self.x*self.y
    
class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14* super().area()

    # def area(self):
    #     return (3.14* self.radius* self.radius)

# s1=shape(3,4)
# print(s1.area())

c1=Circle(5)

print(c1.area())



    
        
    
