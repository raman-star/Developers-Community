##TO CHECK TYPE OF TRIANGLE##


a=int(input())
b=int(input())
c=int(input())
if a==b and b==c and c==a:
    print("Equilateral triangle")
elif a==b or a==c or c==b:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
