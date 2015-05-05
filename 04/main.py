class Dimension:
    def_init_(self,x,y):
        self.x=x
        self.y=y
    def area(self):
            pass
class Cycle(Dimension):
    def_init_(self,r):
         Dimension_init_(self,r,0)
    def area(self):
         return 3.14*self.x*self.x
class Ellipse(Dimension):
    def_init_(self,a,b):
        Dimension_init_(self,a,b)
    def area(self):
        return 3.14*self.x*self.y
class Rectangle(Dimension):
    def_init_(self,w,h):
         Dimension_init_(self,w,h)
    def area(self):
        return self.x*self.y
class Square(Dimension):
    def_init_(self,w,h):
         Dimension_init_(self,w,h)
    def area(self):
        return self.x*self.y
d1=Cycle(5)
d2=Ellipse(10,20)
d3=Retangle(20,15)
d4=Sequare(15,15)
print(d1.area(),d2.area(),d3.area(),d4.area())

        
            
