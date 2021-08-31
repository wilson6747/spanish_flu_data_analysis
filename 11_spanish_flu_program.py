#Opens file and sets it equal to a variable and creates 4 lists for each column.
import statistics
with open('spanish_flu_data.csv') as data_sheet:
    entity = []
    code = []
    year = []
    life_exp = []

    #Loops through and sets individual variables for each column
    for line in data_sheet:
        line = line.strip()
        seperate = line.split(',')
        entity.append(seperate[0])
        code.append(seperate[1])
        year.append(seperate[2])
        life_exp.append(seperate[3])

    #Removes column titles
    entity.pop(0)
    code.pop(0)
    year.pop(0)
    life_exp.pop(0)

    #Converts the year list into integers
    for i in range(0, len(year)):
        year[i] = int(year[i])

    #Converts the life_exp list into floats
    for i in range(0, len(life_exp)):
        life_exp[i] = float(life_exp[i])

    #Gets the min and max for the lists
    min_life = min(life_exp)
    min_index = life_exp.index(min_life)
    max_life = max(life_exp)
    max_index = life_exp.index(max_life)

    #Returns info for lowest and highest life expectancy
    print()
    print('SPANISH FLU DATA PROGRAM:')
    print()
    print('Listed Below is the country with the highest life expectancy follow by the lowest.')
    print()
    print('Lowest Life Expectancy:')
    print(f'ENTITY: {entity[min_index]} , CODE: {code[min_index]} , YEAR: {year[min_index]} , LIFE EXPECTANCY (YEARS): {life_exp[min_index]}')
    print()
    print('Highest Life Expectancy:')
    print(f'ENTITY: {entity[max_index]} , CODE: {code[max_index]} , YEAR: {year[max_index]} , LIFE EXPECTANCY (YEARS): {life_exp[max_index]}')
    print()

    #Asks for user input to find year
    print('This program will return the average life for a given year as well as the')
    print('countires with the lowest and highest life expectancies that year.')
    print()
    year_input = int(input('PLEASE ENTER A YEAR: '))
    if year_input < 1543 or year_input > 2019:
        print(f'{year_input} is not a valid year. Please enter a year between 1543 - 2019.')
        year_input = int(input('PLEASE ENTER A YEAR: '))

    #Creates list of indexes for the input year
    input_indexes = []
    for i in range(len(year)):
        if year[i] == year_input:
            input_indexes.append(i)
    
    #Uses indexes to create new list for the average of the input year and prints average to user
    input_life_exp = [life_exp[i] for i in input_indexes]
    input_avg = statistics.mean(input_life_exp)
    print(f'The average of the year {year_input} is {input_avg:.3f}')

    #Finds the lowest and the highest for the input year and prints to user
    max_input_life_exp = max(input_life_exp)
    max_input_life_index = life_exp.index(max_input_life_exp)
    min_input_life_exp = min(input_life_exp)
    min_input_life_index = life_exp.index(min_input_life_exp)
    print(f'The highest life expectancy in the year {year_input} was {max_input_life_exp} in {entity[max_input_life_index]}')
    print(f'The lowest life expectancy in the year {year_input} was {min_input_life_exp} in {entity[min_input_life_index]}')
    print()

