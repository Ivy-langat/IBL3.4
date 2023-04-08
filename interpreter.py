expression= input("Expression: ")
x, y, z = expression.split()

#changing x and z to float
new_x = float(x)
new_z = float(z)

#calculate the result
if y =="+":
    result = new_x + new_z
elif y =="-":
    result = new_x - new_z
elif y =="*":
    result = new_x * new_z
elif y =="/":
    result = new_x / new_z 


print (round(result , 1))  

