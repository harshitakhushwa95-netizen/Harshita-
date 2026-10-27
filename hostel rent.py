## inpute we need for the project
#total rent
#total food ordered for food snacking 
#electricity unit spend
#charge per unit
#person living in room and flat

#output 
#total amount  you've to pay is

rent=int(input("enter your hostal/flat rent ="))
food=int(input("enter the total amount of food ordered ="))
electricity_spend=int(input("enter the  total lectricity spend="))
charge_per_unit=int(input("enter the charge per unit="))
person=int(input("enter the number of person living in room/flat= "))

total_bill = electricity_spend*charge_per_unit
output=(food+rent+total_bill)//person

print("each person will pay =", output)
