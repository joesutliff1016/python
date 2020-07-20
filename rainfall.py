def main():
    January = float(input('Rainfall for January: '))
    Febuary = float(input('Rainfall for Febuary: '))
    March = float(input('Rainfall for March: '))
    April = float(input('Rainfall for April: '))
    May = float(input('Rainfall for May: '))
    June= float(input('Rainfall for June: '))
    July = float(input('Rainfall for July: '))
    August = float(input('Rainfall for August: '))
    September = float(input('Rainfall for September: '))
    October = float(input('Rainfall for October: '))
    November = float(input('Rainfall for November: '))
    December = float(input('Rainfall for December: '))

    monthly_rainfall = [January, Febuary, March, April, May, June, July, August, September, October, November, December]
    total = 0.0
    for month in monthly_rainfall:
        total += month
    

    average_inches = total / total_month


    print('The total number of months is: ', total_month)
    print('The total inches of rainfall is: ', total_inches)
    print('The average rainfall per month for the entire period is: ', average_inches)

main()
    
