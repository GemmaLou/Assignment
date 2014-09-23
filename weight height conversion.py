#Gemma Buckle
#23/09/2014
#converting inches to cm, stones to kg

height_inches=int(input("Please enter your height in inches: "))
weight_stones=int(input("Please enter your weight in stone: "))
height_cm=height_inches*2.54
weight_kg=weight_stones*6.364
print("Your height in centimetres is {0}cm and your weight in kilograms is {1}kg!".format(height_cm,weight_kg))
