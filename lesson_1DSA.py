class Point: # class

    def __init__(self, x,y): # constructor
        self.vect_x=x
        self.vect_y=y

    #def get_human_readable(self):
        #return str(self.vect_x)+ ","+ str(self.vect_y)

    def __str__(self):
        return  str(self.vect_x)+ ","+ str(self.vect_y)


p1=Point(1,2) # p1 reference variable of this instance ...
p2=Point(3,4)
p3=Point(5,6)

print(f'Point on X_Axis {p1.vect_x} \nPoint on Y_Axis {p1.vect_y}')

#print(p3.get_human_readable())

print(p2) #(logically if they keeping objects so it should be behave like pointer)


class Shape:
    def __init__(self, all_points):
        self.all_points=all_points

    def __str__(self):
        ret=''

        for i in self.all_points:

            ret+=str(i)+" - "
            ret1= ret.strip(' -')

        return   ret1

points_list=[p1,p2,p3]

sh=Shape(points_list)

print(sh)



def print_points(self):

    for i in self.all_points:

        print(i)



Shape.print_points=print_points # when you want you can create function and add to a class in python
sh.print_points()

#Point.print_points=print_points # when you want you can create function and add to a class in python

#print(p1.print_points)

class Triangle(Shape):
    pass
t=Triangle(points_list)

t.print_points()

