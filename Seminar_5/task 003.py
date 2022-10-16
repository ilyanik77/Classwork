# Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков 
# и определяет, можно ли из этих отрезков составить треугольник. 

a = int(input())
b = int(input())
c = int(input())

# 1 способ:
#def Triangle(a, b, c):
#        print("Yes")
#    else:
#        print("No")
#Triangle(a, b, c)
#    if (a + b) > c and (a + c) > b and (b + c) > a:

# 2 способ:
def Triangle(a, b, c):
    Flag = False
    if (a + b) > c and (a + c) > b and (b + c) > a:
        Flag = True
    return "Yes" if Flag else "No"
print(Triangle(a, b, c))
        
        