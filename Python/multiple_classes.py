# multiple_classes.py

#Create a class and function and list out the items in the list
class SubfieldsInAI():    
    def Subfields():
        subfields = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        for fields in subfields:
            print(fields)

#Create a function that checks whether the given number is Odd or Even
class OddEven():
    def OddEven():
        inpnum = int(input("Enter a number: "))
        if inpnum % 2 == 0:
            print(f"{inpnum} is Even number")
        else:
            print(f"{inpnum} is Odd number")

# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
class ElegiblityForMarriage:
    def Elegible():
        Gender = input("Your Gender:")
        Age = int(input("Your Age:"))
        if (Gender == "Male" and Age<21 ) or (Gender == "Female" and Age<18 ):
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")  

#calculate the percentage of your 10th mark
class FindPercent:
    def percentage():
        Subject1 = int(input("Subject1="))
        Subject2 = int(input("Subject2="))
        Subject3 = int(input("Subject3="))
        Subject4 = int(input("Subject4="))
        Subject5 = int(input("Subject5="))
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        Percentage = (Total / (5*100)) * 100    
        print("Total :", Total)
        print("Percentage :", Percentage)                  

#print area and perimeter of triangle using class and function
class triangle:
    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", (Height*Breadth)/2)
    
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", Height1+Height2+Breadth)   

