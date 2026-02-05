
import math
class Vector:
    #A=xi+ yj+ zk
   
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"({self.i}i+{self.j}j+{self.k}k)"

    def mangnitude(self):
        return math.sqrt((self.i**2+self.j**2+self.k**2))
    
    def normalize(self):
        mag=self.mangnitude()
        if mag==0:
            return Vector(0,0,0)
        return mag
    def dot(self,others):
        return (self.i*others.i +self.j*others.j+ self.k*others.k)
    
    def to_tuple(self):
        return (self.i, self.j,self.k)
    
    # def diatance(self):
    #     return math.sqrt((self.i)**2+(self.j)**2+(self.k)**2)

    


   

    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
    def __sub__(self,x):
        return Vector(self.i-x.i,self.j-x.j,self.k-x.k)
    
    def __mul__(self,x):
        return Vector(self.i*x.i,self.j*x.j,self.k*x.k)
    
    def __truediv__(self,scalar):
        if scalar == 0:
            raise ZeroDivisionError("can not be divided by zero")
            
        else:
            return Vector(self.i/scalar.i,self.j/scalar.j,self.k/scalar.k)

        
 
    
v1=Vector(10,12,6)  
v2=Vector(1,7,8)
print("Magnitude:",v2.mangnitude())
print("Normalize:",v2.normalize())
print(v1.to_tuple())

print(v1.dot(v2))

print(v1)
print(v2)
print(v1+v2)
print(type(v1+v2))
print(v1-v2)
print(v1*v2)
print(v1/v2)