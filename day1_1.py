no_of_vec=int(input("number of vehicles: ")) 
no_of_wheels=int(input("number of wheels: ")) 
    
four_wheel = (no_of_wheels-2*no_of_vec)/2;
    
two_wheel =no_of_vec-four_wheel
print(two_wheel,four_wheel)