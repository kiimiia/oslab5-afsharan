from re import T
import csv
from os import close
from os import read
from os import write

products=[]

def show_menu():
    print("""\n  enter your choice
    1.add
    2.edit
    3.delete
    4.show list
    5.search
    6.buy
    7.save
    8.exit""")


def load_data_from_database():
    print('loading...')
    f=open('data.csv','r')
    text=f.read()
    
    rows=text.split('\n')
    
    for row in rows:
        info=row.split(',')
        new_dict={'id':info[0],'name':info[1],'price':info[2],'count':info[3]}
        products.append(new_dict)
    print('load complete.')

    
def add():
 while(True):
    
    new_dict={}
   
    while(True):
     x=0
     new_dict['name']=input("enter the name of product: ")
    

     for i in products:
        if i['name']==new_dict['name']:
            print("The product is available ")
            x=1

     if x==1:
         continue
     else:
         break   

          
    new_dict['id']=int(input("enter the id of product: "))
    new_dict['price']=int(input("enter the price of product: "))
    new_dict['count']=int(input("enter the count of product: "))
    products.append(new_dict)
    print("do you want to add another product?(yes\no)")
    f=input()
    if f=='no':
        break


def edit():
    x=0
    edit=input("enter the name of product  :")
    for i in products:
         if i['name']==edit:
             print("which part you want to edit?")
             print("1->id")
             print("2->name")
             print("3->price")
             print("4->count")
             c=int(input())
             if c==1:
              i['id']=int(input('enter the new id: '))
             elif c==2: 
              i['name']=input('enter the new name:')
             elif c==3:
              i['price']=int(input('enter the new price:'))
             elif c==4: 
              i['count']=int(input('enter the new count:'))
             print("edited sucssesfully")   
             x=1 

    if(x==0):
     print("not found!")
 

def show_list():
    
    for i in products:
        print(i)
    
def search():
    t=0
    sh=input("enter the name of product:")
    for i in products:
         if i['name']==sh:
             print("found : ")
             print(i)
             print("press 6 if you want to buy it.")
             t=1
    if t!=1:     
     print("not found!")
    

def buy():
    t=False
    while(True):
        b=input("enter the name of product:")
        for i in products:
            if i['name']==b and int(i['count']):
                
                  n=int(input("How many ? "))
                  print("buyed!")
                  print("Receipt:","\n id:",i['id'],"\n name:",i['name'],"\n you must pay:",int(i['price'])*n)
                  nc=int(i['count'])
                  nc-=1
                  i['count']=nc
                  t=True

             
        if t==False:
         print("The product isn't available ")
              
                
        print(" Do you want something else?(yes/no)")
        k=input()
        if (k=='no'):
            break


                
            
def delet():
    t=0
    d=input("enter the name of product :")
    for i in products:
         if i['name']==d:
            products.remove(i)
            print("removed ")
            t=1
    if t!=1:     
     print("not found!")


def save():
    lst = ['', '', '', '']
    f = open("data.csv", 'w')
    writer = csv.writer(f)
    for pr in products :
        lst[0] = pr['id']
        lst[1] = pr['name']
        lst[2] = pr['price']
        lst[3] = pr['count']
        writer.writerow(lst)
    f.close()
     

load_data_from_database()
while(True):
    show_menu()
    choice=int(input('please choose from menu: '))
    if  choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        delet()    
    
    elif choice==4:
        show_list()  
    elif choice==5:
        search()
    elif choice==6:
        buy()
    elif choice==7:
        save() 
    elif choice==8:
        exit()    
