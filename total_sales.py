NUM_DAYS = 7

def main():
    sales = [0] * NUM_DAYS

    index = 0
    
    print('Enter the sales for each day of the week')
    
    while index < NUM_DAYS:
        print('Day #', index + 1, ': ', sep='', end='')
        sales[index] = float(input())
        index += 1

    
    
    numbers = sales
    total = 0
    for value in numbers:
        total += value
    print('The total sales are', total)
        

        

main()
    
    
