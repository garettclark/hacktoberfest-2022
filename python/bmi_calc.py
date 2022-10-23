Height=float(input("Enter your height in centimeters: "))Height/100
Weight=float(input("Enter your Weight in Kg: "))
BMI=Weight/(Height*Height)
print("your Body Mass Index is: {}".format(BMI))
if(BMI>0):
    if(BMI<=16):
        print("you are severely underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("you are Healthy")
    elif(BMI<=30):
        print("you are overweight")
    else: print("you are severely overweight")
else:("enter valid details")
