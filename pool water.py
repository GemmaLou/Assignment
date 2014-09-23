#Gemma Buckle
#23/09/2014
#volume of water for pool

length_deep=int(input("Please enter the length of the deepest end of the swimming pool: "))
width_deep=int(input("Please enter the width of the deepest end of the swimming pool: "))
depth_deep=int(input("Please enter the depth of the deepest end of the swimming pool: "))
length_shallow=int(input("Please enter the length of the shallowest end of the swimming pool: "))
width_shallow=int(input("Please enter the width of the shallowest end of the swimming pool: "))
depth_shallow=int(input("Please enter the depth of the shallowest end of the swimming pool: "))

volume_deep=length_deep*width_deep*depth_deep
volume_shallow=length_shallow*width_shallow*depth_shallow

print("The volume of water required to fill the deepest end of this pool is {0} and the volume of water required to fill the shallowest end is {1}.".format(volume_deep,volume_shallow))
