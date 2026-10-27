menu={
    'pizza':120,
    'burger':50,
    'coffee':80,
    'pasta':40,
    'dosa':110,
}
print("Wellcome to PYTHON resturant")
print("pizza: Rs120\n burger: Rs50\n coffee: Rs80\n pasta: Rs40\n dosa: Rs110")

order_total=0

item_1= input("enter a name of a item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item{item_1}has been added to your order")
    
else:
    print(f"order item {item_1}is not available yet!")  

another_order = input("do you want to add another item?(yes/no)")
if another_order == "yes":
    item_2=("enter the name of second item")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"your item{item_2}has been added to your order")
    else:
        print(f"order item {item_2}is not available yet!")

        print(f"the total amount of items is to pay {order_total}")

        


   
  

