from line import Line
class Shapes:
    def __init__(self,lines:Line):
        self.lines=lines

    def perimeter(self):
        return sum(line.length() for line in self.lines)
       
            
    

    def display(self):
        for i,line in enumerate(self.lines,1):
            print (f"{i} {line}")
        print(f"Total perimeter: {round(self.perimeter(),2)}")
        
# Example


        