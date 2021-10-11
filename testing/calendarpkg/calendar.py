# to create the calendar design 
from calendarpkg.year_month import year_start

def calen(year,month):
    ans = year_start(year,month)
    if ans ==0:
        ans=7
    # day arrangement 
    mont = {'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'jun':30,'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
    
    if (year%100)%4 == 0:
        mont['feb']=29
    else:
        mont['feb']=28
    day = mont[month]
    b=ans-1
    d=7-b
    da=1
    for i in range (6):
        if b != 0:
            for i in range(1,b+1):
                print('   ',end='')
                b=0
                
            
        for z in range (d):
            print( '',da,'' , end='')
            da=da+1
            if da > day:
                break
        print()
        if da > day:
                break
        d=7
