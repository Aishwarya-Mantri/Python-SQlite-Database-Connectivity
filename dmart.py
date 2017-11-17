import sqlite3
import random
import time
import pandas
from random import randint
import datetime
import radar #random date time
import pandas as pd
import matplotlib.pyplot as plt

conn=sqlite3.connect('paste.db')
c=conn.cursor()

def create_table(): #function definition
    c.execute("create table toothpaste (id int, date date,brand text, price int,discount float)")
#create_table() function call

def insert_values():
    c.execute("insert into toothpaste(id,date,brand,price,discount) values(3,'2017-11-15','Ultra Brite',160,10)")
    conn.commit()
    c.close()
    conn.close()
#insert_values()

def altertable():
    c.execute("alter table toothpaste add id int auto_increment primary key")
#altertable()

def update_table():
    c.execute("update toothpaste set id=3 where price=90")
    conn.commit()
    c.close()
    conn.close()
#update_table()

def delete_row():
    c.execute("delete from toothpaste where brand='Colgate'")
    conn.commit()
    c.close()
    conn.close()
#delete_row()

def drop_column():
    c.execute("alter table toothpaste drop column id")
    conn.commit()
    c.close()
    conn.close()
#drop_column()
               
def drop_table():
    c.execute("drop table toothpaste")
    conn.commit()
    c.close()
    conn.close()
#drop_table()   
              

def dynamic_entry():
  
    #brand="CloseUp"
    l1=['Babul','CloseUp','Himalaya','DabourRed','Patanjali','Ultra Brite','Kalodont','AquaFresh']
    l2=[4,5,6,7,8,9,10,11,12,13,14]
    #id1=str(sorted(range(4,12)))
    #date='2017-11-16'
    id1=random.choice(l2)
    #print id1
    date=radar.random_date(start='2017-11-02',stop='2017-11-17')
    #print date
    date=datetime.date(randint(2017,2017),randint(1,12),randint(1,22))    
    
    price=random.randrange(40,130)
    discount=random.randrange(10,55)
    brand=random.choice(l1)
    c.execute("insert into toothpaste(id,date,brand,price,discount) values(?,?,?,?,?)",(id1,date,brand,price,discount))
    conn.commit()
for i in range(11):
        dynamic_entry()
        time.sleep(2)
#dynamic_entry()
        
#second Table    
    
def create_table(): 
    c.execute("create table toothpasteind (brand text,location text)")
#create_table() 
    
def insert_values():
    c.execute("insert into toothpasteind(brand,location) values('Himalaya','Nagpur')")
    conn.commit()
    c.close()
    conn.close()
#insert_values()

#Join
def natural_join():
    c.execute("select * from toothpaste natural join toothpasteind")
    df=pd.DataFrame(c.fetchall())
    print df
    #print c.fetchall()
    conn.commit()
    c.close()
    conn.close()
natural_join()

def inner_join():
    c.execute("select * from toothpaste left join toothpasteind on toothpaste.brand=toothpasteind.brand ")
    df=pd.DataFrame(c.fetchall())
    print df
#inner_join()
              


def delete_row():
    c.execute("delete from toothpaste where id>3 and id<20")
    conn.commit()
    c.close()
    conn.close()
#delete_row()
              











