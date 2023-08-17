# https://byui-cse.github.io/cse110-course/lesson11/prove.html
# 11 Prove: Assignment Milestone

with open("life-expectancy.csv") as file:

    #---LISTS FROM FILE---
    entities = []
    codes = []
    years = []
    life_expectancies =[]

    #---ITERATES FILE---
    for line in file:
        line_stripped = line.strip()
        line_splited = line_stripped.split(",")
        
        #Add each column to different lists
        entities.append(line_splited[0])
        codes.append(line_splited[1])
        years.append(line_splited[2])
        life_expectancies.append(line_splited[3])
        
    #---MAX AVARAGE---
    ##Steps: Get max life exp. / Get index from max life exp. / Find entity name and year with same index
    max_life_exp = max(life_expectancies[1:])
    max_index = life_expectancies.index(max_life_exp) 
    max_entity_name = entities[max_index] 
    max_year = years[max_index]  

    print(f"The overall max life expectancy is: {max_life_exp} from {max_entity_name} in {max_year}")

    #---MIN AVARAGE---
    ##Steps: Get min life exp. / Get index from min life exp. / Find entity name and year with same index
    min_life_exp = min(life_expectancies[1:])
    min_index = life_expectancies.index(min_life_exp)
    min_entity_name = entities[min_index]
    min_year = years[min_index] 

    print(f"The overall min life expectancy is: {min_life_exp} from {min_entity_name} in {min_year}")


    
        

    
    

    