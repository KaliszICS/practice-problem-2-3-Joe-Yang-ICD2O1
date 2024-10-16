

def q1(): 
  #Write Assignment code here
  num = input()
  if num[-1] == "y"
    print("ies")
  elif num[-1] == "ey":
    print("eys")
  elif num[-1] == "if"
    print("ives")
  else: 
    print("s")


def q2(): 
  #Write Assignment code here

  num = input()
  if num < 0:
    print(f"{num} is negative")
  elif num > 0:
    print(f"{num} is positive")

def q3(): 
  #Write Assignment code here

  num = float(input("Input a number: "))
  num2 = float(input("Input a number: "))
  num3 = float(input("Input a number: "))
  if num != num2 and num != num3 and num2 != num3:
    print("Scalene")
  elif num == num2 and num != num3 and num2 != num3:
    print("Isosceles")
  elif num == num2 and num == num3 and num2 == num3:
    print("Equilateral")
  elif num + num2 < num3:
    print("No Triangle")
  elif num + num3 < num2:
    print("No Triangle")
  elif num2 + num3 < num:
    print("No Triangle")







#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
