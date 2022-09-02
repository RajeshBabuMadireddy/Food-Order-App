class Admin_details:

    def __init__(self,admin_name,admin_mobile_number,admin_email,admin_address,admin_password):
        self.admin_name=admin_name
        self.admin_mobile_number=admin_mobile_number
        self.admin_email=admin_email
        self.admin_address=admin_address
        self.admin_password=admin_password

    def __str__(self):
        return f"FULL NAME:{self.admin_name}\nMOBILE NUMBER:{self.admin_mobile_number}\nEMAIL:{self.admin_email}\nADDRESS:{self.admin_address}\nPASSWORD:{self.admin_password}"


    def get_admin_name(self): 
        return self.admin_name

    def set_admin_name(self,admin_name):
        self.admin_name=admin_name

    def get_admin_mobile_number(self):
        return self.admin_mobile_number

    def set_admin_phone_number(self,admin_mobile_number):
        self.admin_mobile_number=admin_mobile_number

    def get_admin_email(self):
        return self.admin_email

    def set_admin_email(self,admin_email):
        self.admin_email=admin_email

    def get_admin_address(self):
        return self.admin_address

    def set_admin_address(self,admin_address):
        self.admin_address=admin_address

    def get_password(self):
        return self.admin_password

    def set_password(self,admin_password):
        self.admin_password=admin_password    

class User_details:

    def __init__(self,user_name,user_mobile_number,user_email,user_address,user_password):
        self.user_name=user_name
        self.user_mobile_number=user_mobile_number
        self.user_email=user_email
        self.user_address=user_address
        self.user_password=user_password

    def __str__(self):
        return f"FULL NAME:{self.user_name}\nMOBILE NUMBER:{self.user_mobile_number}\nEMAIL:{self.user_email}\nADDRESS:{self.user_address}\nPASSWORD:{self.user_password}"                  

    def get_user_full_name(self):
        return self.user_full_name

    def set_user_full_name(self,user_full_name):
        self.user_full_name=user_full_name

    def get_user_phone_number(self):
        return self.user_phone_number

    def set_user_phone_number(self,user_phone_number):
        self.user_phone_number=user_phone_number

    def get_user_email(self):
        return self.user_email

    def set_user_email(self,user_email):
        self.user_email=user_email

    def get_user_address(self):
        return self.user_address

    def set_user_address(self,user_address):
        self.user_address=user_address

    def get_user_password(self):
        return self.user_password  

    def set_user_password(self,user_password):
        self.user_password=user_password                                

class Food:
    def __init__(self,food_id,name_of_food,quantity_of_food,food_cost,discount_for_food,food_stock):
        self.food_id=food_id
        self.name_of_food=name_of_food
        self.quantity_of_food=quantity_of_food
        self.food_cost=food_cost
        self.discount_for_food=discount_for_food
        self.food_stock=food_stock

    def __str__(self):
        return f"FOOD ID:{self.food_id}\nNAME OF FOOD:{self.name_of_food}\nQUANTITY OF FOOD:{self.quantity_of_food}\nFOOD COST:{self.food_cost}\nDISCOUNT FOR FOOD:{self.discount_for_food}\nFOOD STOCK:{self.food_stock}"

    def get_food_id(self):
        return self.food_id

    def set_food_id(self,food_id):
        self.food_id=food_id

    def get_name_of_food(self):
        return self.name_of_food

    def set_name_of_food(self,name_of_food):
        self.name_of_food=name_of_food

    def get_quantity_of_food(self):
        return self.quantity_of_food

    def set_food_quantity(self,quantity_of_food):
        self.quantity_of_food=quantity_of_food

    def get_food_cost(self):
        return self.food_cost  

    def set_food_price(self,food_cost):
        self.food_cost=food_cost  

    def get_discount_for_food(self):
        return self.discount_for_food       

    def set_discount_for_food(self,discount_for_food):
        self.discount_for_food=discount_for_food     

    def get_food_stock(self):
        return self.food_stock

    def set_food_stock(self,food_stock):
        self.food_stock=food_stock                                




class Admin:
    admin_list=[]
    food_list=[]
    def add_details(self):
        print("*********ADDING ADMIN DETAILS***********")
        admin_name=input("enter admin full name")
        admin_mobile_number=int(input("enter admin phone number"))
        admin_password=input("enter admin password")
        admin_address=input("enter admin address")
        admin_email=input("enter admin email")
        admin_obj=Admin_details(admin_name,admin_mobile_number,admin_email,admin_address,admin_password)
        self.admin_list.append(admin_obj)
        print(self.admin_list)
        
    def add_food_details(self):
        print("***********ADDING FOOD DETAILS************")
        food_id=int(input("enter food id")) 
        val1=food_id
        name_of_food=input("enter food name")
        val2=name_of_food
        quantity_of_food=int(input("enter food quantity"))
        val3=quantity_of_food
        food_cost=float(input("enter food price"))
        val4=food_cost
        food_discount=int(input("enter food discount"))
        val5=food_discount
        food_stock=int(input("enter food stock"))
        val6=food_stock
        food_obj=Food(food_id,name_of_food,quantity_of_food,food_cost,food_discount,food_stock)
        self.food_list.append(food_obj)
        keys=("FOOD ID","NAME OF FOOD","QUANTITY OF FOOD","FOOD COST","FOOD DISCOUNT","FOOD STOCK")
        values=(val1,val2,val3,val4,val5,val6)
        dic=dict(zip(keys,values))


        return dic

    def view_food_item(self):
        print("***************VIEW FOOD ITEMS*************")
        for i in self.food_list:
            print(i)

    def edit_food_item(self):
        print("*************EDIT FOOD ITEMS***************")
        edit_food_id=int(input("enter food id"))
        print("select option")
        print("1.edit name of food")
        print("2.edit  food quantity")
        print("3.edit food price")
        print("4.edit food discount")
        print("5.edit food stock")
        choice=int(input("enter your choice"))
        
        if choice==1:
            for j in self.food_list:
                if edit_food_id==j.food_id:
                    j.name_of_food=input("enter food name")
                    print("food name updated successfully") 
                    print(j.name_of_food)   
                
        elif choice==2:
            for j in self.food_list:
                if edit_food_id==j.food_id:
                    j.quantity_of_food=input("enter food quantity")
                    print("food quantity updated successfully") 
                    print(j.quantity_of_food)
                

        elif choice==3:
            for j in self.food_list:
                if edit_food_id==j.food_id:
                    j.food_cost=float(input("enter food price")) 
                    print(" food price updated successfully")
                    print("UPDATE FOOD PRICE:",j.food_cost)   
                    

        elif choice==4:
            for j in self.food_list:
                if edit_food_id==j.food_id:
                    j.food_discount=int(input("enetr food discount"))
                    print("food discount updated successfully")
                    print(j.food_discount)
                    
        elif choice==5:
            for j in self.food_list:
                if edit_food_id==j.food_id:
                    j.food_stock=int(input("enter food stock"))
                    print("food stock updated successfully")   
                    

        else:
            print("invalid choice")       

    def delete_food_item(self):
        print("************DELETE FOOD ITEMS**************")
        del_food_id=int(input("enter food id"))
        for food in self.food_list:
            if del_food_id==food.food_id:
                print("food item deleted successfully")
            else:
                pass    




order_list=[]
food_info={"dict1":{"food name":"tandoori",
                    "food price":"240rs",
                    "food quantity":"5 pieces"
},
                    "dict2":{"food name":"vegan burger",
                    "food price":"120rs",
                    "food quantity":"1 piece"

}


}
food_list={}
user_list=[]
class UserFunction:

    user_list=[]
    def add_user(self):
        print("***********ADDING USER DETAILS**********")
        user_name=input("enter user full name")
        user_mobile_number=int(input("enter user phone number"))
        user_email=input("enter user email")
        user_address=input("enter user address")
        user_password=input("enter user password")
        user_obj=User_details(user_name,user_mobile_number,user_email,user_address,user_password)
        self.user_list.append(user_obj)

    def update_profile(self):
        print("************UPDATE PROFILE************")
        update_username=input("enter username")
        print("select option")
        print("1.update user phone number")
        print("2.update  user email")
        print("3.update user address")
        print("4.update user password")
        option=int(input("enter option"))
        if option==1:
            for i in self.user_list:
                print(i.user_full_name)
                if i.user_name == update_username:
                    i.user_mobile_number=int(input("enter phone number"))
                    print("user phone number update successfully")
                    
        elif option==2:
            for i in self.user_list:
                if i.user_name == update_username:
                    i.user_email=input("enter email id")
                    print("user email updated succeccfully")
                    

        elif option ==3:
            for i in self.user_list:
                if i.user_name==update_username:
                    i.user_address=input("enter address")
                    print("user address updated successfully")
                    

        elif option ==4:
            for i in self.user_list:
                if i.user_name==update_username:
                    i.user_password=input("enter password")
                    print("user passsword updated successfully")
                    

        else:
            print("invalid option")        
            
    def place_new_order(self):
        print("***********NEW ORDER**********")
        for j in range(len(food_info)):
            print("select food item\n1.dict1\n2.dict2\n3.press 3 to quit")
            food_choice=int(input("enter choice"))
            if food_choice==1:
                print(food_info["dict1"])
                order_list.append(food_info["dict1"])
                
            elif food_choice==2:
                print(food_info["dict2"])
                order_list.append(food_info["dict2"])
                
            else:
                
                break        
        print("TOTAL_ORDER:",order_list)



        
    def order_history(self):
        print("***********ORDER HISTORY********")
        print(order_list)    
                                            
                                            


class Main:
    
    def __init__(self,admin_obj,user_obj):
        self.admin_obj=admin_obj
        self.user_obj=user_obj

    def execute(self,choice):
        if choice==1:
            print("********CREATE ADMIN ACCOUNT******")
            admin_obj=Admin()
            admin_obj.add_details()

        elif choice==2: 
            print("*********** CREATE USER ACCOUNT**********")
            user_obj=UserFunction()
            user_obj.add_user()
            
        elif  choice==3:
            print("************ADMIN LOGIN*************")
            admin_obj=Admin()
            a_name=input("enter admin name")
            a_password=input("enter password") 
            for i in Admin.admin_list:
                if a_name==i.admin_name and a_password==i.admin_password:
                    print("*********login successfull!********")
                    print("enter choice\n1.add food items\n2.view food items\n3.edit food items\n4.delete food item")
                    choice=int(input("enter your choice"))
                    if choice==1:
                        admin_obj=Admin()
                        admin_obj.add_food_details()
                        
                    elif choice==2:
                        admin_obj=Admin()
                        admin_obj.view_food_item()
                        
                    elif choice==3:
                        admin_obj=Admin()
                        admin_obj.edit_food_item()
                        
                    elif choice==4:
                        admin_obj=Admin()
                        admin_obj.delete_food_item()
                        
                    else:
                        break  
                else:
                    print("---------------------")
                    print("wrong credentials,please try again!")  
                    
           
        elif choice==4:
            print("**************USER LOGIN************")
            user_obj=UserFunction()     
            u_name=input("enter user name")
            u_password=input("enter user password")
            for i in UserFunction.user_list:
                if u_name==i.user_name and u_password == i.user_password:
                    print("**********LOGIN SUCCESSFULL!***********")
                    print("select option\n1.place new order\n2.order history\n3.update profile")
                    option=int(input("enter option"))
                    if option==1:
                        user_obj=UserFunction()
                        user_obj.place_new_order()
                        
                    elif option ==2:
                        user_obj=UserFunction()
                        user_obj.order_history()
                        
                    elif option ==3:
                        user_obj=UserFunction()
                        user_obj.update_profile()
                        
                    else:
                        print("*****invalid option*****")
                        break    
                else:
                    print("-------------------------")
                    print("wrong credential,please try again!")    
                    
        else:
            print("invalid choice")
            print(quit())        
         
if __name__=="__main__":
    admin_obj=Admin() 
    user_obj=UserFunction()    
    main=Main(admin_obj,user_obj)     

    while True:
        print("enter choice\n1.create admin account\n2.create user account\n3.admin login\n4.user login")
        choice=int(input("enter your choice"))
        main.execute(choice)    
        

