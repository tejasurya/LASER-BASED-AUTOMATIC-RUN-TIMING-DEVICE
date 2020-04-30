import time
import serial
import socket
import sys
import serial.tools.list_ports
import MySQLdb as sql
from selenium import webdriver
track=10
c=0
x=0
z=0
t = False
f = 5
g = 5
h = 5
i = 5
j = 5
k = 5
l = 5
m = 5
n = 5
o = 5
ab = 4
ba = 4
ac = 4
ca = 4
ad = 4
da = 4
ae = 4
ea = 4
af = 4
fa = 4
port = ""
port1 = ""
a = webdriver.Firefox()
a.get("http://localhost/TestStopwatch/index.html")
rank = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
db=sql.connect("localhost","root","","automation")
cursor=db.cursor()
query = "select * from tracks;"
cursor.execute(query)
result=cursor.fetchone()
track=int(result[0])
ports=list(serial.tools.list_ports.comports())
if ports[0][1].find('Silicon Labs') != -1:
    port =  ports[0][0]
elif ports[1][1].find('Silicon Labs') != -1:
    port =  ports[1][0]
if ports[0][1].find('USB Serial Port') != -1:
    port1 =  ports[0][0]
elif ports[1][1].find('USB Serial Port') != -1:  
    port1 = ports[1][0]
#connect Starting Arduino to right side and Finish arduino to the Left side
ser = serial.Serial(port1, 9600)
cer = serial.Serial(port, 9600)
print "Started"
if track==1:
    while x < 5000:
        x+=1
        if ser.read() == 'a' and ab == 4:
            print "first track false start"
            t=True
            ab = 1
elif track==2:
    while x < 5000:
        x+=1
        if ser.read() == 'a' and ab == 4:
            print "first track false start"
            t=True
            ab = 1
        if ser.read() == 'c' and ba == 4:
            print "second track false start"
            t=True
            ba = 2
elif track==3:
    while x < 5000:
        x+=1
        if ser.read() == 'a' and ab == 4:
            print "first track false start"
            t=True
            ab = 1
        if ser.read() == 'c' and ba == 4:
            print "second track false start"
            t=True
            ba = 2
        if ser.read() == 'e' and ac == 4:
            print "third track false start"
            t=True
            ac = 1
elif track==4:
    while x < 5000:
        x+=1
        if ser.read() == 'a' and ab == 4:
            print "first track false start"
            t=True
            ab = 1
        if ser.read() == 'c' and ba == 4:
            print "second track false start"
            t=True
            ba = 2
        if ser.read() == 'e' and ac == 4:
            print "third track false start"
            t=True
            ac = 1  
        if ser.read() == 'g' and ca == 4:
            print "fourth track false start"
            t=True
            ca = 2
elif track==5:
    while x < 5000:
        x+=1
        if ser.read() == 'a' and ab == 4:
            print "first track false start"
            t=True
            ab = 1
        if ser.read() == 'c' and ba == 4:
            print "second track false start"
            t=True
            ba = 2
        if ser.read() == 'e' and ac == 4:
            print "third track false start"
            t=True
            ac = 1  
        if ser.read() == 'g' and ca == 4:
            print "fourth track false start"
            t=True
            ca = 2
        if ser.read() == 'i' and ad == 4:
            print "fifth track false start"
            t=True
            ad = 1
elif track==6:
    while x < 5000:
        x+=1
        if ser.read() == 'a' and ab == 4:
            print "first track false start"
            t=True
            ab = 1
        if ser.read() == 'c' and ba == 4:
            print "second track false start"
            t=True
            ba = 2
        if ser.read() == 'e' and ac == 4:
            print "third track false start"
            t=True
            ac = 1  
        if ser.read() == 'g' and ca == 4:
            print "fourth track false start"
            t=True
            ca = 2
        if ser.read() == 'i' and ad == 4:
            print "fifth track false start"
            t=True
            ad = 1
        if ser.read() == 'k' and da == 4:
            print "sixth track false start"
            t=True
            da = 2
elif track==7:
    while x < 5000:
        x+=1
        if ser.read() == 'a' and ab == 4:
            print "first track false start"
            t=True
            ab = 1
        if ser.read() == 'c' and ba == 4:
            print "second track false start"
            t=True
            ba = 2
        if ser.read() == 'e' and ac == 4:
            print "third track false start"
            t=True
            ac = 1  
        if ser.read() == 'g' and ca == 4:
            print "fourth track false start"
            t=True
            ca = 2
        if ser.read() == 'i' and ad == 4:
            print "fifth track false start"
            t=True
            ad = 1
        if ser.read() == 'k' and da == 4:
            print "sixth track false start"
            t=True
            da = 2
        if ser.read() == 'm' and ae == 4:
            print "seventh track false start"
            t=True
            ae = 1
elif track==8:
    while x < 5000:
        x+=1
        if ser.read() == 'a' and ab == 4:
            print "first track false start"
            t=True
            ab = 1
        if ser.read() == 'c' and ba == 4:
            print "second track false start"
            t=True
            ba = 2
        if ser.read() == 'e' and ac == 4:
            print "third track false start"
            t=True
            ac = 1  
        if ser.read() == 'g' and ca == 4:
            print "fourth track false start"
            t=True
            ca = 2
        if ser.read() == 'i' and ad == 4:
            print "fifth track false start"
            t=True
            ad = 1
        if ser.read() == 'k' and da == 4:
            print "sixth track false start"
            t=True
            da = 2
        if ser.read() == 'm' and ae == 4:
            print "seventh track false start"
            t=True
            ae = 1
        if ser.read() == 'o' and ea == 4:
            print "eigth track false start"
            t=True
            ea = 2
elif track==9:
    while x < 5000:
        x+=1
        if ser.read() == 'a' and ab == 4:
            print "first track false start"
            t=True
            ab = 1
        if ser.read() == 'c' and ba == 4:
            print "second track false start"
            t=True
            ba = 2
        if ser.read() == 'e' and ac == 4:
            print "third track false start"
            t=True
            ac = 1  
        if ser.read() == 'g' and ca == 4:
            print "fourth track false start"
            t=True
            ca = 2
        if ser.read() == 'i' and ad == 4:
            print "fifth track false start"
            t=True
            ad = 1
        if ser.read() == 'k' and da == 4:
            print "sixth track false start"
            t=True
            da = 2
        if ser.read() == 'm' and ae == 4:
            print "seventh track false start"
            t=True
            ae = 1
        if ser.read() == 'o' and ea == 4:
            print "eigth track false start"
            t=True
            ea = 2
        if ser.read() == 'q' and af == 4:
            print "nineth track false start"
            t=True
            af = 1
elif track==10:
    while x < 5000:
        x=x+1
        if ser.read() == 'a' and ab == 4:
            print "first track false start"
            t=True
            ab = 1
        if ser.read() == 'c' and ba == 4:
            print "second track false start"
            t=True
            ba = 2
        if ser.read() == 'e' and ac == 4:
            print "third track false start"
            t=True
            ac = 1  
        if ser.read() == 'g' and ca == 4:
            print "fourth track false start"
            t=True
            ca = 2
        if ser.read() == 'i' and ad == 4:
            print "fifth track false start"
            t=True
            ad = 1
        if ser.read() == 'k' and da == 4:
            print "sixth track false start"
            t=True
            da = 2
        if ser.read() == 'm' and ae == 4:
            print "seventh track false start"
            t=True
            ae = 1
        if ser.read() == 'o' and ea == 4:
            print "eigth track false start"
            t=True
            ea = 2
        if ser.read() == 'q' and af == 4:
            print "nineth track false start"
            t=True
            af = 1
        if ser.read() == 's' and fa == 4:
            print "Tenth track false start"
            t=True
            fa = 1
if t == True:
    a.close()
    sys.exit()
else :
    a.find_element_by_xpath("//button[@title='Start']").click()
    ser.close()
xoxo="0"+cer.readline()
if track==1:
    while z < 1:
        abdc=0
        ahf = cer.readline()
        bhf = cer.readline()
        chf = cer.readline()
        dhf = cer.readline()
        ahf=ahf+bhf+chf+dhf
        if ahf.find("b") !=-1 and f == 5:
            f = 50
        if ahf.find("d") !=-1 and f == 50:
            rank[z] = 1
            z+=1
            print "first"
            f=51
            a.find_element_by_xpath("//button[@title='Split']").click()
elif track==2:
    while z < 2:
        abdc=0
        ahf = cer.readline()
        bhf = cer.readline()
        chf = cer.readline()
        dhf = cer.readline()
        ahf=ahf+bhf+chf+dhf
        if ahf.find("b") !=-1 and f == 5:
            f = 50
        if ahf.find("d") !=-1 and f == 50:
            rank[z] = 1
            z+=1
            print "first"
            f=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find("f") !=-1 and g == 5:
            g = 50
        if ahf.find("h") !=-1 and g == 50:
            rank[z] = 2
            z+=1
            print "second"
            g = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
elif track==3:
    while z < 3:
        abdc=0
        ahf = cer.readline()
        bhf = cer.readline()
        chf = cer.readline()
        dhf = cer.readline()
        ahf=ahf+bhf+chf+dhf
        if ahf.find("b") !=-1 and f == 5:
            f = 50
        if ahf.find("d") !=-1 and f == 50:
            rank[z] = 1
            z+=1
            print "first"
            f=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find("f") !=-1 and g == 5:
            g = 50
        if ahf.find("h") !=-1 and g == 50:
            rank[z] = 2
            z+=1
            print "second"
            g = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('j') !=-1 and h == 5:
            h = 50
        if ahf.find('l') !=-1 and h == 50:
            rank[z] = 3
            z+=1
            print "third"
            h=51
            a.find_element_by_xpath("//button[@title='Split']").click()
elif track==4:
    while z < 4:
        abdc=0
        ahf = cer.readline()
        bhf = cer.readline()
        chf = cer.readline()
        dhf = cer.readline()
        ahf=ahf+bhf+chf+dhf
        if ahf.find("b") !=-1 and f == 5:
            f = 50
        if ahf.find("d") !=-1 and f == 50:
            rank[z] = 1
            z+=1
            print "first"
            f=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find("f") !=-1 and g == 5:
            g = 50
        if ahf.find("h") !=-1 and g == 50:
            rank[z] = 2
            z+=1
            print "second"
            g = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('j') !=-1 and h == 5:
            h = 50
        if ahf.find('l') !=-1 and h == 50:
            rank[z] = 3
            z+=1
            print "third"
            h=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('n') !=-1 and i == 5:
            i = 50
        if ahf.find('p') !=-1 and i == 50:
            rank[z] = 4
            z+=1
            print "fourth"
            i=51
            a.find_element_by_xpath("//button[@title='Split']").click()
elif track==5:
    while z < 5:
        abdc=0
        ahf = cer.readline()
        bhf = cer.readline()
        chf = cer.readline()
        dhf = cer.readline()
        ahf=ahf+bhf+chf+dhf
        if ahf.find("b") !=-1 and f == 5:
            f = 50
        if ahf.find("d") !=-1 and f == 50:
            rank[z] = 1
            z+=1
            print "first"
            f=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find("f") !=-1 and g == 5:
            g = 50
        if ahf.find("h") !=-1 and g == 50:
            rank[z] = 2
            z+=1
            print "second"
            g = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('j') !=-1 and h == 5:
            h = 50
        if ahf.find('l') !=-1 and h == 50:
            rank[z] = 3
            z+=1
            print "third"
            h=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('n') !=-1 and i == 5:
            i = 50
        if ahf.find('p') !=-1 and i == 50:
            rank[z] = 4
            z+=1
            print "fourth"
            i=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('r') !=-1 and j == 5:
            j=50
        if ahf.find('t') !=-1 and j == 50:
            rank[z] = 5
            z+=1
            print "fifth"
            j=51
            a.find_element_by_xpath("//button[@title='Split']").click()
elif track==6:
    while z < 6:
        abdc=0
        ahf = cer.readline()
        bhf = cer.readline()
        chf = cer.readline()
        dhf = cer.readline()
        ahf=ahf+bhf+chf+dhf
        if ahf.find("b") !=-1 and f == 5:
            f = 50
        if ahf.find("d") !=-1 and f == 50:
            rank[z] = 1
            z+=1
            print "first"
            f=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find("f") !=-1 and g == 5:
            g = 50
        if ahf.find("h") !=-1 and g == 50:
            rank[z] = 2
            z+=1
            print "second"
            g = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('j') !=-1 and h == 5:
            h = 50
        if ahf.find('l') !=-1 and h == 50:
            rank[z] = 3
            z+=1
            print "third"
            h=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('n') !=-1 and i == 5:
            i = 50
        if ahf.find('p') !=-1 and i == 50:
            rank[z] = 4
            z+=1
            print "fourth"
            i=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('r') !=-1 and j == 5:
            j=50
        if ahf.find('t') !=-1 and j == 50:
            rank[z] = 5
            z+=1
            print "fifth"
            j=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('v') !=-1 and k == 5:
            k=50
        if ahf.find('x') !=-1 and k == 50:
            rank[z] = 6
            z+=1
            print "six"
            k = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
elif track==7:
    while z < 7:
        abdc=0
        ahf = cer.readline()
        bhf = cer.readline()
        chf = cer.readline()
        dhf = cer.readline()
        ahf=ahf+bhf+chf+dhf
        if ahf.find("b") !=-1 and f == 5:
            f = 50
        if ahf.find("d") !=-1 and f == 50:
            rank[z] = 1
            z+=1
            print "first"
            f=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find("f") !=-1 and g == 5:
            g = 50
        if ahf.find("h") !=-1 and g == 50:
            rank[z] = 2
            z+=1
            print "second"
            g = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('j') !=-1 and h == 5:
            h = 50
        if ahf.find('l') !=-1 and h == 50:
            rank[z] = 3
            z+=1
            print "third"
            h=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('n') !=-1 and i == 5:
            i = 50
        if ahf.find('p') !=-1 and i == 50:
            rank[z] = 4
            z+=1
            print "fourth"
            i=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('r') !=-1 and j == 5:
            j=50
        if ahf.find('t') !=-1 and j == 50:
            rank[z] = 5
            z+=1
            print "fifth"
            j=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('v') !=-1 and k == 5:
            k=50
        if ahf.find('x') !=-1 and k == 50:
            rank[z] = 6
            z+=1
            print "six"
            k = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('z') !=-1 and l == 5:
            l = 50
        if ahf.find('2') !=-1 and l == 50:
            rank[z] = 7
            z+=1
            print "seven"
            l = 51
            a.find_element_by_xpath("//button[@title='Split']").click()    
elif track==8:
    while z < 8:
        abdc=0
        ahf = cer.readline()
        bhf = cer.readline()
        chf = cer.readline()
        dhf = cer.readline()
        ahf=ahf+bhf+chf+dhf
        if ahf.find("b") !=-1 and f == 5:
            f = 50
        if ahf.find("d") !=-1 and f == 50:
            rank[z] = 1
            z+=1
            print "first"
            f=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find("f") !=-1 and g == 5:
            g = 50
        if ahf.find("h") !=-1 and g == 50:
            rank[z] = 2
            z+=1
            print "second"
            g = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('j') !=-1 and h == 5:
            h = 50
        if ahf.find('l') !=-1 and h == 50:
            rank[z] = 3
            z+=1
            print "third"
            h=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('n') !=-1 and i == 5:
            i = 50
        if ahf.find('p') !=-1 and i == 50:
            rank[z] = 4
            z+=1
            print "fourth"
            i=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('r') !=-1 and j == 5:
            j=50
        if ahf.find('t') !=-1 and j == 50:
            rank[z] = 5
            z+=1
            print "fifth"
            j=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('v') !=-1 and k == 5:
            k=50
        if ahf.find('x') !=-1 and k == 50:
            rank[z] = 6
            z+=1
            print "six"
            k = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('z') !=-1 and l == 5:
            l = 50
        if ahf.find('2') !=-1 and l == 50:
            rank[z] = 7
            z+=1
            print "seven"
            l = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('4') !=-1 and m == 5:
            m = 50
        if ahf.find('6') !=-1 and m == 50:
            rank[z] = 8
            z+=1
            print "eight"
            m=51
            a.find_element_by_xpath("//button[@title='Split']").click()
elif track==9:
    while z < 9:
        abdc=0
        ahf = cer.readline()
        bhf = cer.readline()
        chf = cer.readline()
        dhf = cer.readline()
        ahf=ahf+bhf+chf+dhf
        if ahf.find("b") !=-1 and f == 5:
            f = 50
        if ahf.find("d") !=-1 and f == 50:
            rank[z] = 1
            z+=1
            print "first"
            f=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find("f") !=-1 and g == 5:
            g = 50
        if ahf.find("h") !=-1 and g == 50:
            rank[z] = 2
            z+=1
            print "second"
            g = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('j') !=-1 and h == 5:
            h = 50
        if ahf.find('l') !=-1 and h == 50:
            rank[z] = 3
            z+=1
            print "third"
            h=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('n') !=-1 and i == 5:
            i = 50
        if ahf.find('p') !=-1 and i == 50:
            rank[z] = 4
            z+=1
            print "fourth"
            i=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('r') !=-1 and j == 5:
            j=50
        if ahf.find('t') !=-1 and j == 50:
            rank[z] = 5
            z+=1
            print "fifth"
            j=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('v') !=-1 and k == 5:
            k=50
        if ahf.find('x') !=-1 and k == 50:
            rank[z] = 6
            z+=1
            print "six"
            k = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('z') !=-1 and l == 5:
            l = 50
        if ahf.find('2') !=-1 and l == 50:
            rank[z] = 7
            z+=1
            print "seven"
            l = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('4') !=-1 and m == 5:
            m = 50
        if ahf.find('6') !=-1 and m == 50:
            rank[z] = 8
            z+=1
            print "eight"
            m=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('8') !=-1 and n == 5:
            n = 50
        if ahf.find('!') !=-1 and n == 50:
            rank[z] = 9
            z+=1
            print "nine"
            n = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
elif track==10:
    while z < 10:
        abdc=0
        ahf = cer.readline()
        bhf = cer.readline()
        chf = cer.readline()
        dhf = cer.readline()
        ahf=ahf+bhf+chf+dhf
        if ahf.find("b") !=-1 and f == 5:
            f = 50
        if ahf.find("d") !=-1 and f == 50:
            rank[z] = 1
            z+=1
            print "first"
            f=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find("f") !=-1 and g == 5:
            g = 50
        if ahf.find("h") !=-1 and g == 50:
            rank[z] = 2
            z+=1
            print "second"
            g = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('j') !=-1 and h == 5:
            h = 50
        if ahf.find('l') !=-1 and h == 50:
            rank[z] = 3
            z+=1
            print "third"
            h=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('n') !=-1 and i == 5:
            i = 50
        if ahf.find('p') !=-1 and i == 50:
            rank[z] = 4
            z+=1
            print "fourth"
            i=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('r') !=-1 and j == 5:
            j=50
        if ahf.find('t') !=-1 and j == 50:
            rank[z] = 5
            z+=1
            print "fifth"
            j=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('v') !=-1 and k == 5:
            k=50
        if ahf.find('x') !=-1 and k == 50:
            rank[z] = 6
            z+=1
            print "six"
            k = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('z') !=-1 and l == 5:
            l = 50
        if ahf.find('2') !=-1 and l == 50:
            rank[z] = 7
            z+=1
            print "seven"
            l = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('4') !=-1 and m == 5:
            m = 50
        if ahf.find('6') !=-1 and m == 50:
            rank[z] = 8
            z+=1
            print "eight"
            m=51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('8') !=-1 and n == 5:
            n = 50
        if ahf.find('!') !=-1 and n == 50:
            rank[z] = 9
            z+=1
            print "nine"
            n = 51
            a.find_element_by_xpath("//button[@title='Split']").click()
        if ahf.find('#') !=-1 and o == 5:
            o = 50
        if ahf.find('%') !=-1 and o == 50:
            rank[z] = 10
            z+=1
            print "ten"
            o=51
            a.find_element_by_xpath("//button[@title='Split']").click()
print "stop"
a.find_element_by_xpath("//button[@title='Stop']").click()
cer.close()
cur=db.cursor()
time.sleep(10)
query1 = "select * from details;"
cur.execute(query1)
result1 = cur.fetchall()
count = cur.rowcount
row=result1[count-track][0]
strin=""
z=1
while z<=track:
    i=track
    d = 'cm'
    d += `z`
    time=str(a.find_element_by_id("time"+str(z)).text)
    cur.execute("""UPDATE details SET elapsedtime = %s WHERE sno >= %s AND trackno = %s""" , (time, str(row), str(rank[z-1])))
    while i>0:
        if int(result1[count-i][2])==rank[z-1]:
            strin=str(rank[z-1])+"  -  "+result1[count-i][1]
            a.find_element_by_id(d).send_keys(strin)
        i=i-1
    z=z+1
db.commit()
db.close()