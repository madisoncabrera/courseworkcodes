import math

class Polygon(object):
        def __init__(self, name, sides):
                self.name=name
                self.sides=sides
                # define name and sides instance variable
                # name is the Polygon name
                # sides is a list of all the side lenghts
                
        def get_perimeter(self):
                '''Calculates and returns the perimeter of the polygon.'''
                perimeter=0 #initalize perimeter
                for p in self.sides:
                        perimeter+=p #augmented addition 
                return f'The perimeter is {perimeter}.' #print message with final value
                        
s                # perimeter is the sum of all the sides

        def __str__(self):
                return f'Sides of {self.name}: {self.sides}'

# define a Triangle class - a subclass of Polygon
class Triangle(Polygon):
        def __init__(self, name, sides):
                if len(sides) != 3:
                        raise ValueError(f'Triangle must be initialized with three sides')
                super().__init__(name,sides) #super call pulls in name and sides from parent class
                # initialize name and sides with super call 
        
        def get_area(self):
                '''return area of a triangle'''
                a,b,c=self.sides #name each side individually 
                smp= (a+b+c)/2 #semiperimeter
                #p= Polygon.get_perimeter(self)
                area= math.sqrt(smp*(smp-a)*(smp-b)*(smp-c)) #area formula
        
                return f'The area of the Triangle is {area:.2f}.' #print message
                
                # formula given in the spec file

def main():
        # 1. Create a Triangle t1 (a special type of Polygon)
        # with name as Triangle and sides as [2,3,4]
        t1=Triangle('T1',[2,3,4])
        print(t1)
        print(Polygon.get_perimeter(t1))
        print(Triangle.get_area(t1))
        # print triangle object t1
        # print perimeter of t1
        # print area of t1
        
        t2=Triangle('T2',[2,3,4,5])
        # 2. Create a Triangle with four sides and sides are [2,3,4,5]
        # this will raise an Error        


main()
