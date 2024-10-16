

def q1(): 
  #Write Assignment code here
  num = input("In: ")
  if num[-3:] == "ife":
    print("-ives")
  elif num[-2:] == "ey":
    print("-eys")  
  elif num[-1:] == "y":
    print("-ies") 
  else: 
    print("-s")


def q2(): 
  #Write Assignment code here

  num = int(input("In: "))
  if num > 0:
    print(f"{num} is positive")
  elif num < 0:
    print(f"{num} is negative")

def q3(): 
  #Write Assignment code here

  num = float(input("Input a number: "))
  num2 = float(input("Input a number: "))
  num3 = float(input("Input a number: "))
  if num + num2 < num3:
    print("No Triangle")
  elif num + num3 < num2:
    print("No Triangle")
  elif num2 + num3 < num:
    print("No Triangle")
  elif num != num2 and num != num3 and num2 != num3:
    print("Scalene")
  elif num == num2 and num != num3 and num2 != num3:
    print("Isosceles")
  elif num == num2 and num == num3 and num2 == num3:
    print("Equilateral")
  






#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
q3()
'''