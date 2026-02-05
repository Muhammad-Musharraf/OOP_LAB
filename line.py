from point_ import Point

class Line:
    def __init__(self,Start_point:Point,End_point:Point):
        self.__Start_point=Start_point
        self.__End_Point=End_point

    @property
    def Start_point(self):
        return self.__Start_point
    
    @Start_point.setter
    def Start_point(self,new_point:Point):

        self.__Start_point=new_point
        

    @property
    def End_point(self):
        return self.__End_Point
    
    @End_point.setter
    def End_point(self,new_point:Point):
        self.__End_Point=new_point

    def length(self):
        return self.Start_point.calculate_distance(self.End_point)
    
    def __str__(self):
        return f"Line from {self.Start_point} to {self.End_point} of length {round(self.length(),3)}"
    
    


        