#Gemma Buckle
#19/09/2014
#currency notes assignment

def currency
money1=int(input("Please enter a whole amount of money: £"))

answer20=money1//20
money2=money1%20

answer10=money2//10
money3=money2%10

answer5=money3//5
money4=money3%5

answer2=money4//2
money5=money4%2

answer1=money5

print("The minimum number of notes this can be made in is {0} £20s, {1} £10s, {2} £5s, {3} £2s and {4} £1s!!.".format(answer20,answer10,answer5,answer2,answer1))
