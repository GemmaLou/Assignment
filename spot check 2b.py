#Gemma Buckle
#23/09/2014
#number of weights needed to balance a value

weight1=int(input("Please enter the value of the weight to be balanced in whole grams: "))

answer100=weight1//100
weight2=weight1%100

answer50=weight2//50
weight3=weight2%50

answer10=weight3//10
weight4=weight3%10

answer5=weight4//5
weight5=weight4%5

answer2=weight5//2
weight6=weight5%2

answer1=weight6

print("The number of each weight needed to balance {0} is {1} 100g, {2} 50g, {3} 10g, {4} 5g, {5} 2g and {6} 1g!".format(weight1,answer100,answer50,answer10,answer5,answer2,answer1))
