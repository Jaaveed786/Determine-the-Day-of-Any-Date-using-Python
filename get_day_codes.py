d=int(input('Enter day : '))
m=int(input('Enter month : '))
y=int(input('Enter year : '))

def getday(date,month,year):
    month_code={1:0,2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5}
    day_code={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thrusday',5:'Friday',6:'Saturday'}
    db=[]

    if year in range(1600,1700) or year in range(2000,2100):
        i=6
        db.append(i)
    elif year in range(1700,1800) or year in range(2100,2200):
        i=4
        db.append(i)
    elif year in range(1800,1900) or year in range(2200,2300):
        i=2
        db.append(i)
    elif year in range(1900,2000):
        i=0
        db.append(i)

    y=int(str(year)[-2:])
    d=y//4          ##// is used to divide given numbers without floats(decimals)

    for k,j in month_code.items():
        if month==k:
            m=j
    tot=y+d+date+m+db[0]
    final=tot%7
    for m,n in day_code.items():
        if final==m:
            if year%4==0 and month==2:
                print(date,'/',month,'/',year,':','the day is : ',[m-1])
            else:
                print(date,'/',month,'/',year,':','the day is : ',n)

getday(d,m,y)