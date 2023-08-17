# 12 Prove: Assignment - Data Analysis


with open("life-expectancy.csv") as file:
    next(file)

    #--------LISTS FROM FILE--------
    entities = []
    years = []
    life_expect = []

    #--------USER INPUT LISTS AND VARIABLES--------
    index = 0
    user_entities = []
    user_years = []
    user_life_expect = []

    #--------FIND MAX, MIN VARIABLES--------
    highest_life_entity = ""
    highest_life = 0
    highest_year = 0


    lowest_life_entity = ""
    lowest_life = 9999
    lowest_year = 9999

    #--------ITERATES FILE--------
    for line in file:
        line_stripped = line.strip()
        line_splited = line_stripped.split(",")
        
        #Add each column to different lists
        entities.append(line_splited[0])
        years.append(int(line_splited[2]))
        life_expect.append(float(line_splited[3]))

    #--------HIGHEST, LOWEST OVERALL LIFE EXPECT--------
    for i in range(len(entities)):
        
        entity = entities[i]
        max_life = life_expect[i]
        min_life = life_expect[i]
        year = years[i]

        if max_life > highest_life: #HIGHEST
            highest_life = max_life
            highest_life_entity = entity
            highest_year = year

        elif min_life < lowest_life: #LOWEST
            lowest_life = min_life
            lowest_life_entity = entity
            lowest_year = year
    
    #OUTPUT / PRINT
    print("---OVERALL INFO---")
    print(f"The overall max life expectancy is: {highest_life:.2f} from {highest_life_entity} in {highest_year}")
    print(f"The overall min life expectancy is: {lowest_life:.2f} from {lowest_life_entity} in {lowest_year}")

    #---RESETS VARIABLES---
    highest_life_entity = ""
    highest_life = 0
    highest_year = 0

    lowest_life_entity = ""
    lowest_life = 9999
    lowest_year = 9999

    #--------USER INPUT [YEAR]--------
    user_input = int(input("\nEnter the year of interest: "))
    
    #Add to lists matches between user and full lists
    for i in years: 
        if i == user_input:

            user_entities.append(entities[index])
            user_years.append(int(years[index]))
            user_life_expect.append(float(life_expect[index]))
        
        index += 1

    #HIGHEST, LOWEST USER LIFE EXPECT
    for i in range(len(user_life_expect)):
        
        entity = user_entities[i]
        max_life, min_life = user_life_expect[i], user_life_expect[i]

        if max_life > highest_life: #HIGHEST
            highest_life = max_life
            highest_life_entity = entity

        
        if min_life < lowest_life: #LOWEST
            lowest_life = min_life
            lowest_life_entity = entity

    #OUTPUT / PRINT      
    avarage = sum(user_life_expect) / len(user_life_expect)
    print(f"---IN {user_input} INFO:---")
    print(f"The avarage life expectancy across all countries was {avarage:.2f}")
    print(f"The max life expectancy was in {highest_life_entity} with {highest_life:.2f}")
    print(f"The min life expectancy was in {lowest_life_entity} with {lowest_life:.2f}")

    #---RESET VARIABLES AND LISTS---
    index = 0
    user_entities = []
    user_years = []
    user_life_expect = []

    highest_life_entity = ""
    highest_life = 0
    highest_year = 0

    lowest_life_entity = ""
    lowest_life = 9999
    lowest_year = 9999  

    #--------USER INPUT [COUNTRY]--------
    user_input = input("\nEnter the country of interest: ")
    
    #Add to lists matches between user and full lists
    for i in entities: 

        if i == user_input.title():

            user_entities.append(entities[index])
            user_years.append(int(years[index]))
            user_life_expect.append(float(life_expect[index]))
        
        index += 1

    #HIGHEST, LOWEST USER LIFE EXPECT
    for i in range(len(user_life_expect)):
        
        entity = user_entities[i]
        max_life, min_life = user_life_expect[i], user_life_expect[i]

        if max_life > highest_life: #HIGHEST
            highest_life = max_life
            highest_life_entity = entity

        
        if min_life < lowest_life: #LOWEST
            lowest_life = min_life
            lowest_life_entity = entity

    #OUTPUT / PRINT 
    avarage = sum(user_life_expect) / len(user_life_expect)     
    print(f"---IN {user_input.upper()} OVERALL INFO:---")
    print(f"The overall life expectancy is {avarage:.2f}")
    print(f"The max life expectancy was in {highest_life_entity} with {highest_life:.2f}")
    print(f"The min life expectancy was in {lowest_life_entity} with {lowest_life:.2f}")

    







    
        

    
    

    