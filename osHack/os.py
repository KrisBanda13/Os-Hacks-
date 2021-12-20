import socket
import sys
import random
import time 
from rich.console import Console

console = Console()

console.print("[green]-----------------------------------------[/green]")
console.print("Setting up variables [>----] 1/5 (20%)")
w: bool = True
console.print("Setting up variables [=>---] 2/5 (40%)")
loc: str = ""
console.print("Setting up classes   [==>--] 3/5 (60%)")

class command:
    def __init__(self, command: str, f):
        self.command: str = command
        self.f = f
    def start(self):
        self.f.__call__()
console.print("Setting up commands  [===>-] 4/5 (80%)")

def findc(a: str):
    for i in c:
        if i.command == a:
            return i

def Scaner():
    mas = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]

    console = Console()
    console.print("[blue]Сканер Портов[/blue]")
    print("")
    host = input ('Ведите имя сайта или IP Adres: ')
    console.print("[green]--------------------------------[/green]")
    console.print("[blue]Ожидайте идет санирование Портов[/blue]")
    console.print("[green]--------------------------------[/green]")
    for port in mas:
        s = socket.socket()
        try:
            s.connect((host, port))
        except socket.error:
            pass
        else:
            s.close
            print (host + ': ' + str(port) + ' порт активен')
    console.print("[green]--------------------------------[/green]")
    console.print("[blue]Процесс завершен[/blue]")

def Calculator():
    console = Console()
    console.print("[red]--------------------------------[/red]")
    console.print("[blue]Ведите 1 число >>")
    a = int(input())
            
    console.print("[red]--------------------------------")
            
    console.print("[blue]Ведите 2 число >>")
    b = int(input())
            
    console.print("[green]--------------------------------")
            
    console.print("[blue]Виберийте оперцию")
    console.print("[blue]1) сложить a+b", a+b)
    console.print("[blue]2) вьчислить a-b", a-b)
    d = int(input ())
            
    if d == 1:
        console.print("[red]сумма >>> ", a+b)
    if d == 2:
        console.print("[red]сумма >>> ", a-b)
                
    console.print("[violet]-------------------------------")

def Findbyutc():
    tar = int(input("enter target's time (hours): "))
    urt = int(input("your time at the same moment (hours): "))
    uut = int(input("enter your utc: "))
    print(uut-(urt-tar))    

def Password():    
    chars = "+-/*!&$#@?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    number = int(input("Количество паролей >>>"))
    lenght = int(input("Длина строки >>>"))

    for x in range(number):
        password = ""

        for i in range(lenght):
            password += random.choice(chars)

        console.print(password)   

def Randomaizer():
    num = True

    while num == True:
        number = input("Число : ")
        proges = input("Проценти : ")
        while type(number) != int:
            try:
                number = int(number)
                proges = int(proges)
            except ValueError:
                print("Вводи целочисленыые значения!")
                number = input("Число : ")
                proges = input("Проценти : ")
        while type(proges) != int:
            try:
                number = int(number)
                proges = int(proges)
            except ValueError:
                print("Вводи целочисленыые значения!")
                number = input("Число : ")
                proges = input("Проценти : ")

        finish = number / 100 * proges
        print("Ваш ответ : ", float(finish))

console.print("Setting up arrays    [====>] 5/5 (100%)")

c = [command("Scaner", Scaner), command("exit", exit), command("Calculator", Calculator), command("Findbyutc", Findbyutc), command("Password", Password), command("Randomaizer", Randomaizer)]
num = input ("Введите Name (Root) - ")

while w:
    if int (num == "Root"):
        console.print("[green]-----------------------------------------[/green]")
        console.print("[blue]Создатель KRIS_BANDA")
        console.print("[blue]Youtube - https://www.youtube.com/channel/UC1_Wx7WwXjPB_ZVs8BMuJZA")
        print("")
        console.print("[blue]Command : \n1) Scaner - Сканер Портов ) \n2) Calculator - Калькулятор умеит токо + - делать ) \n3) Password - Гиниратор паролей ) \n4) Findbyutc - Вичисление ) \n5) exit - Вихид из оперативной системи )")
        console.print("[green]-----------------------------------------[/green]")
        loc: str = ""
        inp: str = input(f"Root >>> ")
        r = findc(inp)
        if r is not None:
            r.start()
        else:
            print(f"ОШИБКА HackOS: в os.py>>>findc({inp})>>>{findc} \n{r}")
