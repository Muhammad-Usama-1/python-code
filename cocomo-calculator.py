#Effort In Organic Mode 
line_of_code = float(input("Enter Lines Of Code : "))
line_of_code = line_of_code/1000
def cocomo(a,b,d,mode, c= 2.5):
    mode = mode.upper()
    effort = a*(line_of_code**b)
    effort = round(effort,2)
    development_time = c*(effort**d)
    development_time = round(development_time,2)
    people = effort/development_time
    people = round(people,0)

    print(f"MODE IS {mode} : ---> EFFORT {effort}person-month DEVELOPMENT TIME {development_time}months PEOPLE REQUIRED {people}people-approx")

cocomo(2.4,1.05,0.38,"organic")
cocomo(3.0,1.12,0.35,"semi detached")
cocomo(3.6,1.20,0.32,"embedded")