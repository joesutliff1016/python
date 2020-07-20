def main():
    anno = int(input('Enter year(e.g. 2015): '))
    anno = int(input('Enter month(1-12): '))
    anno = int(input('Enter day of the month(1-31): '))
    calc_day(anno)
    print('Day of the week is, ' ,day)
    
def calc_day(anno):
    if month == 1 or month == 2:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
def calc_day(anno):
    h = ( day + 26*(month+1)//10 + k + k//4 + j//4 + 5 * j) % 7
    
    if h == 0:
        day = 'Saturday'
    elif h == 1:
        day = 'Sunday'
    elif h == 2:
        day = 'Monday'
    elif h == 3:
        day = 'Tuesday'
    elif h == 4:
        day = 'Wednesday'
    elif h == 5:
        day = 'Thursday'
    else:
        day = 'Friday'
        
def calc_day(year, month, day):
    return day
        

main()
