# -*- coding: utf-8 -*-
import random
import string
import colorama
from colorama import Fore, Back, Style
colorama.init()

def cgenf(str):
    for c in range(0,len(str)):
        if str[c] == 'X' or str[c] == 'Y' or str[c] == 'Z':
            rep = ""
            if str[c] == 'X':
                rep = ''.join(random.choices(string.ascii_uppercase, k=1))
            elif str[c] == 'Y':
                rep = ''.join(random.choices(string.digits, k=1))
            elif str[c] == 'Z':
                rep = ''.join(random.choices(string.ascii_uppercase + string.digits, k=1))
    
            str = str[:c] + rep + str[c+1:]
            
    return str;

def templateinput(keyformat):
    print("Введите количество ключей, которое вы хотите сгенерировать")
    
    steamkeytypeonenumber = input()
    
    steamkeytypeonenumber = float(steamkeytypeonenumber)
    
    steamkeytypeonenumber = int(float(steamkeytypeonenumber))
    
    steamkeytypecount = 0
    
    my_file = open('Keys.txt', 'w')
    
    while steamkeytypecount < steamkeytypeonenumber : 
        text_for_file = cgenf(keyformat)
        print(text_for_file)
        
        steamkeytypecount += 1
        
        text_for_file += chr(10) + chr(13)
        
        my_file.write(text_for_file)
        
    my_file.close()

print("                                                     ")
print(Fore.MAGENTA,"█▀ ▀█▀ █▀█ ▄▀█ █ █ █ █▄▄ █▀▀ █▀█ █▀█ █▄█ █▀▀ █▀▀ █▄ █")
print(Fore.MAGENTA,"▄█  █  █▀▄ █▀█ ▀▄▀▄▀ █▄█ ██▄ █▀▄ █▀▄  █  █▄█ ██▄ █ ▀█")
print("                                                     ")
    
print(Fore.GREEN,"Добро пожаловать в StrawberryGen!")
print(" Идеи по поводу генератора можете высылать сюда: strawberryboomber@gmail.com")
print(" Ключи скачиваются в файл keys.txt")
print("                                                     ")
print(Fore.CYAN,"Выберите тип ключа")
print(" 1. Steam")
print(" 2. UPlay")
print(" 3. Roblox")
print(" 4. Kaspersky")
print(" 9. Сделать свой ключ")
print(" 0. Поддержать проект")

keytype = input()

print(Style.RESET_ALL)

if keytype == "1" : 
    print("Выберите тип ключа Steam")
    print("1. AAAAA-BBBBB-CCCCC")
    print("2. AAAAA-BBBBB-CCCCC-DDDDD-EEEEE")
    print("3. 237ABCDGHJLPRST 23")
    
    steamkeytype = input()
    
    if steamkeytype == "1" :
        templateinput("XXXXX-XXXXX-XXXXX")
        
    if steamkeytype == "2" :
        templateinput("XXXXX-XXXXX-XXXXX-XXXXX-XXXXX")                    

    if steamkeytype == "3" :
        templateinput("YYYXXXXXXXXXXXX YY")

if keytype == "2" :
    print("Выберите тип ключа UPlay")
    print("1. AAAA-BBBB-CCCC-DDDD")
    print("2. AAA-BBBB-CCCC-DDDD-EEEE")
        
    uplaykeytype = input()
    
    if uplaykeytype == "1" :
        templateinput("XXXX-XXXX-XXXX-XXXX")
        
    if uplaykeytype == "2" :
        templateinput("XXX-XXXX-XXXX-XXXX-XXXX")
        
if keytype == "3" :
    templateinput("YYY-YYY-YYYY")
    
if keytype == "4" :
    templateinput("ZZZZZ-ZZZZZ-ZZZZZ-ZZZZZ")

if keytype == "9" :
    print("Напишите шаблон")
    print("X - Только буквы")
    print("Y - Только цифры")
    print("Z - Буквы и цифры")
    
    unitype = input()
    
    templateinput(unitype)        
    
print(Fore.CYAN,"Ключи сохранены в файл Keys.txt")