# https://byui-cse.github.io/cse110-course/lesson11/teach.html
# 11 Teach: Team Activity

with open("hr_system.txt") as file:

    names = []
    ids = []
    jobs = []
    salaries = []

    for line in file:
        strip_lines = line.strip()
        splited_lines = strip_lines.split(" ")
        
        names.append(splited_lines[0])
        ids.append(splited_lines[1])
        jobs.append(splited_lines[2])
        salaries.append(splited_lines[3]) 

    for index in range(len(names)):

        name = names[index]
        id = ids[index]
        job = jobs[index]
        salary = salaries[index]
        
        print(f"{name} (ID: {id}), {job} - ${salary}")