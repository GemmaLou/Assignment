#Gemma Buckle
#23/09/2014
#Calculating volume of a swimming pool

width=int(input("Please enter the width of the pool: "))
length=int(input("Please enter the length of the pool: "))
depth=int(input("Please enter the depth of the pool: "))
main_section_volume=length*width*depth
circle_radius=width/2
circle_area=3.14*circle_radius**2
half_circle_volume=(circle_area/2)*depth
pool_volume=main_section_volume+half_circle_volume
print("The volume of this pool is {0}!".format(pool_volume))
