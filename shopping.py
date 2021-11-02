from os import close
from os import read
from os import write


Products=[]


def menu():
    print("""\n  enter your choice
    1.add
    2.edit
    3.delete
    4.show list
    5.search
    6.buy
    7.exit""")


def load():
 
    f=open("product.txt",'r')
    text = f.read()
    rows = text.split('/n')
    for row in rows:
        info = row.split(',')
        new_text={"code":info[0],"name":info[1],"price":info[2],"count":info[3]}
        Products.append(new_text)



def add():

    print('\n add new product \n')
    code = input('code: ')
    name = input('name: ')
    price = float (input('price: '))
    count = int (input('count: '))
    Products.append({"code":code,"name":name,"price":price,"count":count})
   


def edit():
  
    edited = input(' enter the name of product ')

    for product in Products:

         if edited == product['name']:
            edited_price = float (input("enter the new price: "))
            product['price'] = edited_price
            
            edited_count = int (input("enter the new count: "))
            product['count'] = edited_count
             
            edited_code = input("enter the new code: ")
            product['code'] = edited_code

         else :
            print('/n wrong name')
            break
    


def delete():

    deleted = input(' enter the name of product ')
    for product in  Products:
        if product["name"] == deleted:
            Products.remove(product)
            print(" delete !")
         
        else :
            print('/n wrong name')
            break   
    


def show_list():
    print("Code\tName\tPrice\tcount")
    for product in Products:
        print (product["code"],'\t',product["name"],'\t',product["price"],'\t',product["count"])



def search():

    search_name = input('enter the name of product ')
    for product in Products:
        if  search_name == product['name']:
            print(product) 
            return True  

        else :
             print("I can\'t find!!")
             return False



  
def buy():

    shopping_name = input('enter the name of product ')
    for product in Products:
        if shopping_name == product['name']:
            a=int(product["count"])
            if a==0:
                delete(shopping_name)
                break
            else:
               
                a-=1
                product["count"]=a
                return
    


def save():
    list=['','','','']
    f=open("product.txt",'w')

    writer =f.write
    
    for product in Products:
        list[0]= product ["code"]
        list[1]= product ["name"]
        list[2]= product ["price"]
        list[3]= product ["count"]
        writer.writerow(list) 
    f.close()
    exit()


load()

while 1 : 
   

    menu()
    
    choice=int(input("Enter your choice::"))

    if choice == 1:
        add()
        save()

    elif choice==2:
        edit()
        save()

    elif choice==3:
        delete()
        save()

    elif choice==4:
        show_list()

    elif choice==5:   
        search()

    elif choice==6:
        buy()
        save()

    elif choice==7:
       save() 
       exit()
