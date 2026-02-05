import math
class Point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,new_x):
        self.__x=new_x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,new_y):
        self.__y=new_y

     
    def calculate_distance(self,other):
        x=(other.__x-self.__x)**2
        y=(other.__y-self.__y)**2
        diatance=math.sqrt(x+y)

        return (round(diatance,3))
    

    def __add__(self,other):
        x=other.__x+self.__x
        y=other.__y+self.__y
    
        return (Point(x,y))
    
    def __sub__(self,other):
        x=other.__x-self.__x
        y=other.__y-self.__y
    
        return (Point(x,y))
    
    def __mul__(self,other):
        x=other.__x*self.__x
        y=other.__y*self.__y
    
        return (Point(x,y))
    
    def __truediv__(self,other):
        x=round(other.__x/self.__x,3)
        y=round(other.__y/self.__y,3)
    
        return (Point(x,y))



        

    
    def __str__(self):
        return f"P({self.__x},{self.__y})"
        
    