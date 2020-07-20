

def main():
    year = int(input('Enter a year: '))

    animal_year = year % 12

    get_input(year, animal_year)


    
def get_input(year, animal_year):
    
    sign = ['monkey0', 'rooster1', 'dog2', 'pig3',\
             'rat4', 'ox5', 'tiger6', 'rabbit7',\
             'dragon8', 'snake9', 'horse10', 'sheep11']
    
   

    print(year, 'Is the year of the', animal_year, sign)
    
    
   
    

    
main()
