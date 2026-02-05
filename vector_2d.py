import math
class Vector2D:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def __str__(self):
        return f"Vector({self.__x},{self.__y})"
    
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,new_x):
        if not isinstance(new_x,int):
            raise TypeError("must be integer")
        self.__x=new_x

    @property
    def y(self):
        return self.__y
    @x.setter
    def y(self,new_y):
        if not isinstance(new_y,int):
            raise TypeError("must be integer")
        self.__y=new_y

    
    def __add__(self,others):
        return Vector2D(self.__x+ others.__x,self.__y+ others.__y)
    
    def __sub__(self,others):
        return Vector2D(self.__x-others.__x,self.__y- others.__y)
    
    def __mul__(self,others):
        return Vector2D(self.__x* others.__x,self.__y* others.__y)
    
    def magnitude(self):
        return round(math.sqrt(self.__x**2 + self.__y**2),3)
    
    def Normalize(self):
        mag=self.magnitude()
        if mag==0:
            return Vector2D(0,0)
        unit_x=round(self.__x/mag,3)
        unit_y=round(self.__y/mag,3)
        return Vector2D(unit_x,unit_y)



