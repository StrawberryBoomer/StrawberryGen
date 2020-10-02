# -*- coding: utf-8 -*-
import random
import string

def steamgen(count):
    
    key = " "
    
    while count > 0:
        key += ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + "-"
        count -= 1
        
    key = key[:-1]
    
    return key

def steamgentwo():
    key = ''.join(random.choices(string.digits, k=3)) + ''.join(random.choices(string.ascii_uppercase, k=12)) + " " + ''.join(random.choices(string.digits, k=2))
    
    return key

def uplaygen(count):
    
    key = " "
    
    while count > 0:
        key += ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + "-"
        count -= 1
        
    key = key[:-1]
    
    return key

def uplaygentwo(count):
    
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) + "-"
    
    while count > 0:
        key += ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + "-"
        count -= 1
    
    key = key[:-1]
    
    return key

print("                                                     ")
print("█▀ ▀█▀ █▀█ ▄▀█ █ █ █ █▄▄ █▀▀ █▀█ █▀█ █▄█ █▀▀ █▀▀ █▄ █")
print("▄█  █  █▀▄ █▀█ ▀▄▀▄▀ █▄█ ██▄ █▀▄ █▀▄  █  █▄█ ██▄ █ ▀█")
print("                                                     ")

print("Добро пожаловать в StrawberryGen!")
print("Идеи по поводу генератора можете высылать сюда: strawberryboomber@gmail.com")
print("                                                     ")
print("Выберите тип ключа")
print("1. Steam")
print("2. UPlay")

keytype = input()

if keytype == "1" : 
    print("Выберите тип ключа Steam")
    print("1. AAAAA-BBBBB-CCCCC")
    print("2. AAAAA-BBBBB-CCCCC-DDDDD-EEEEE")
    print("3. 237ABCDGHJLPRST 23")
    
    steamkeytype = input()
    
    if steamkeytype == "1" :
        print("Введите количество ключей, которое вы хотите сгенерировать")
        
        steamkeytypeonenumber = input()
        
        steamkeytypeonenumber = int(float(steamkeytypeonenumber))
        
        steamkeytypecount = 0
        
        while steamkeytypecount < steamkeytypeonenumber : 
            print(steamgen(3))
            steamkeytypecount += 1
        
        
    if steamkeytype == "2" :
        print("Введите количество ключей, которое вы хотите сгенерировать")
        
        steamkeytypeonenumber = input()
        
        steamkeytypeonenumber = int(float(steamkeytypeonenumber))
        
        steamkeytypecount = 0
        
        while steamkeytypecount < steamkeytypeonenumber : 
            print(steamgen(5))
            
            steamkeytypecount += 1        

    if steamkeytype == "3" :
        print("Введите количество ключей, которое вы хотите сгенерировать")
        
        steamkeytypeonenumber = input()
        
        steamkeytypeonenumber = int(float(steamkeytypeonenumber))
        
        steamkeytypecount = 0
        
        while steamkeytypecount < steamkeytypeonenumber : 
            print(steamgentwo())
            
            steamkeytypecount += 1          
    

if keytype == "2" :
    print("Выберите тип ключа UPlay")
    print("1. AAAA-BBBB-CCCC-DDDD")
    print("2. AAA-BBBB-CCCC-DDDD-EEEE")
        
    uplaykeytype = input()
    
    if uplaykeytype == "1" :
        print("Введите количество ключей, которое вы хотите сгенерировать")
        
        uplaykeynumber = input()
        
        uplaykeynumber = int(float(uplaykeynumber))
        
        uplaykeycount = 0
        
        while uplaykeycount < uplaykeynumber : 
            print(uplaygen(4))
            uplaykeycount += 1  
            
    if uplaykeytype == "2" :
        print("Введите количество ключей, которое вы хотите сгенерировать")
        
        uplaykeynumber = input()
        
        uplaykeynumber = int(float(uplaykeynumber))
        
        uplaykeycount = 0
        
        while uplaykeycount < uplaykeynumber : 
            print(uplaygentwo(4))
            uplaykeycount += 1    