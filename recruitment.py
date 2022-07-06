myName =''
def get_skills():
    # Add at least 3 random skills for the user to select from
    return ["Python","C++","Javascript","Juggling","Running","Eating","workout","swimming","video Games"]


def show_skills(skills):
    
    for i, skill in enumerate(skills,1):
        print(i, '. ' + skill, sep ='', end ='\n')
        
    # x=0
    # while(x<len(skills)-1):
    #     x = x+1
    #     print( str(x) +". "+skills[x])
        

    
    # Pretty print skills to the user
    # Write your code here
    ...


def get_user_skills(skills):
    show_skills(skills)
    userSelections = []
    
    print("Select two skills")
    firstSelection = input("Select the first skill:")
    secondSelection = input("Select the second skill:")
    userSelections.append(firstSelection)
    userSelections.append(secondSelection)

    return userSelections;

def get_user_cv(skills):
    cv ={}
    cv["name"] = input("Your name\n")
    
    myName =cv["name"]
    cv["age"] = input("Your age\n")
    cv["years of experience"] = input("Your years of experience\n ")

    cv["skills"] = get_user_skills(skills)
    

    print(cv["age"])
    return cv
    
    
    # Get the users CV from their inputs
    # Write your code here
    ...


def check_acceptance(cv, desired_skill):
    # 
    x = 0

    print(cv['age'])
    print(cv["years of experience"])
    print(desired_skill in cv["skills"])
    
    if((int(cv['age']) >= 28 and int(cv['age'])<=40) and (int(cv["years of experience"]) > 3)) and(desired_skill in cv["skills"]):
    #     for i in cv["skills"]:
        return True
    else:
        return False

def main():
    print("Welcome to the special recruitment program, please answer the following questions:")
    x = check_acceptance(get_user_cv(get_skills()), "C++")
    print(myName)

    if (x == True):
        print(" you are accepted")
    else:
        print("you are not accepted")
# print("sdsdsd")
# get_user_skills(get_skills())

if __name__ == "__main__":
    main()
