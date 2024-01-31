import pandas as pd

print("*-----------------------------------------------------*")
print("|   ^____^                                    ^____^  |  ")
print("|   (*__*)  WELCOME TO ATTENDENCE CALCULATOR  (*__*)  |")
print("|    /  \                                      /  \   |")
print("*-----------------------------------------------------*")


print("1.Annual attendance calculation")
print("2.Monthly attendance calculation ")
print("what do you want to know ? ")

user_input = int(input("enter your choice:"))
#---------------------------------------------------------------------------------------------------------
def per_one_sub_annual():
    #for one subject
    subject_name=input("enter subject name: ")

    total_count_t=int(input(f"enter total classes count of {subject_name} suject  in thoery: "))
    present_count_t=int(input(f"enter present classes count of {subject_name} suject in theory: "))
    total_count_p=int(input(f"enter total classes count of {subject_name} suject  in practical: "))
    present_count_p=int(input(f"enter present classes count of {subject_name} suject in practical: "))
    
    
    x1=(present_count_t*100)/(total_count_t)
    #print("Your number is ",x1)
    x2=(present_count_p*100)/(total_count_p)
    #print("Your number is ",x2)
    print('* Enter week classes*')
    xt=int(input(f"enter theory classes per week in {subject_name}: "))
    xp=int(input(f"enter practical(including lab and tutorial) classes per week in {subject_name}: "))
    t=xt/(xt+xp)
    p=xp/(xt+xp)
    #print(t,p)

    average=(x1*t)+(x2*p)
    #print(average)
    print("*-----------------------------------------------------*")
    print(f"  percentage in {subject_name} is {average}%")
    print("*------------------------------------------------------*")
    
def per_all_sub_annual():
    #for all subject
    n=int(input("enter total subjects you are interested to know their persentage attendance: "))

    subjects=[]
    percentage=[]
    for i in range(1,n+1):
        subject_name=input(f"enter subject{i} name: ")
        #print("DISCLAIMER: If there is no theory or practical classes for that respective subject, give input 1 for total classes count and 0 for present classes count")

        total_count_t=int(input(f"enter total classes count of {subject_name} suject  in thoery: "))
        present_count_t=int(input(f"enter present classes count of {subject_name} suject in theory: "))
        if total_count_t==0:
            total_count_t=1
        
        total_count_p=int(input(f"enter total classes count of {subject_name} suject  in practical: "))
        present_count_p=int(input(f"enter present classes count of {subject_name} suject in practical: "))
        if total_count_p==0:
            total_count_p=1
        
        x1=(present_count_t*100)/(total_count_t)
        #print("Your number is ",x1)
        x2=(present_count_p*100)/(total_count_p)
        #print("Your number is ",x2)

        xt=int(input(f"enter theory classes per week in {subject_name}: "))
        if xt==0:
            xt=1
        xp=int(input(f"enter practical(including lab and tutorial) classes per week in {subject_name}: "))
        t=xt/(xt+xp)
        p=xp/(xt+xp)
        #print(t,p)

        average=(x1*t)+(x2*p)
        #print(average)
        print("--------------------------------------------")
        print(f" percentage in {subject_name} is {average}%")
        print("--------------------------------------------")
        subjects.append(subject_name)
        percentage.append(average)
        
    per_sheet=pd.Series(percentage,index=subjects)
    print(per_sheet)
    
def per_annual_default():
    a1=input("this is wrong input, do you want to continue?(y/n)")
    if a1.lower()=="y":
        percentage_annual()
    else:
        print("thank you")

#-------------------------------------------------------------------------------------------------------------------
def est_one_sub_annual():
    #for one subject
    subject_name=input("enter subject name: ")
    def est_annual1(a,subject_name):
        total_count=int(input("Enter total count of classes as mentioned in course policy) :"))
        
        xt=int(input(f"enter theory classes per week in {subject_name}: "))
        xp=int(input(f"enter practical(including lab and tutorial) classes per week in {subject_name}: "))
        weeks=total_count//xt
        total_theory_classes=weeks*xt
        total_practical_classes=weeks*xp
        
        
        classes_to_attended_theory=(a * total_theory_classes)//(100) + 1 # even if 30.4 gives 31 preventing any chances of safety prediction    
        absents_to_take1= (total_theory_classes)-(classes_to_attended_theory)   
        
        classes_to_attended_practical=(a * total_practical_classes)//(100) + 1 # even if 30.4 gives 31 preventing any chances of safety prediction    
        absents_to_take2= (total_practical_classes)-(classes_to_attended_practical)
        
        
        total_absents=absents_to_take1 + absents_to_take2 
        
        
        
        print("<---   IN ", subject_name ,":   --->" )
        print("classes to be attended in theory is: ",classes_to_attended_theory)
        print( f"YOU CAN TAKE {absents_to_take1} LEAVES in THEORY CLASSES")
        print("<----------------------------->")
        print("classes to be attended in practical is: ",classes_to_attended_practical)
        print( f"YOU CAN TAKE {absents_to_take2} LEAVES IN PRACTICAL CLASSES")
        print("<----------------------------->")
        print("TOTAL YOU CAN TAKE LEAVE OF: ",total_absents)
        print("<------ THANK YOU -------> ")
        
        


    print("Default attendance is calculated for 80% ")
    decision_default=input("Do you want change default attendance 80%? (y/n)")
    if decision_default.lower()=="y":
        default_per=int(input("Enter default percentage to be calculated: "))
        est_annual1(default_per,subject_name)
        
    else:
        est_annual1(80,subject_name)
        

def est_all_sub_annual():
    #for all subjects
    import pandas as pd
    n=int(input("enter total subjects you are interested to know their persentage attendance: "))

    subjects=[]
    absents_to_take_theory=[]
    absents_to_take_practical=[]
    index1=[]

    def est_annual2(a,n):
        for i in range(1,n+1):
            subject_name=input(f"enter subject{i} name: ")
            total_count=int(input(f"Enter total count of classes in {subject_name} as mentioned in course policy) :"))
            
            xt=int(input(f"enter theory classes per week in {subject_name}: "))
            xp=int(input(f"enter practical(including lab and tutorial) classes per week in {subject_name}: "))
            weeks=total_count//xt
            total_theory_classes=weeks*xt
            total_practical_classes=weeks*xp
            
            
            classes_to_attended_theory=(a * total_theory_classes)//(100) +1
            absents_to_take1= (total_theory_classes)-(classes_to_attended_theory)
            
            classes_to_attended_practical=(a * total_practical_classes)//(100) + 1 
            absents_to_take2= (total_practical_classes)-(classes_to_attended_practical)  
            
            #total_absents=absents_to_take1 + absents_to_take2
            
            index1.append(i)
            subjects.append(subject_name)
            absents_to_take_theory.append(absents_to_take1)
            absents_to_take_practical.append(absents_to_take2)
            
            data = {'subject name': subjects, 'safe absents in theroy': absents_to_take_theory, 'safe absents in practical': absents_to_take_practical}
            
        est_sheets=pd.DataFrame(data,index=index1)
        print(est_sheets)
        print("Thank you")
        
        
        
    print("Default attendance is calculated for 80% ")
    decision_default=input("Do you want change default attendance 80%? (y/n)")

    if decision_default.lower()=="y":
        default_per=int(input("Enter default percentage to be calculated: "))
        est_annual2(default_per,n)
    else:
        est_annual2(80,n)

def est_annual_defult():
    a1=input("this is wrong input, do you want to continue?(y/n)")
    if a1.lower()=="y":
        estimate_annual()
    else:
        print("thank you")
    
#-------------------------------------------------------------------------------------------------------------------
def percentage_annual():
    print("11.would like to know attendence for one subject")
    print("22.would like to know attendence of all subjects")
    a=int(input("Enter your choice:"))
    if a==11:
        per_one_sub_annual()
    elif a==22:
        per_all_sub_annual()
    else:
        per_annual_default()
        
def estimate_annual():
    print("11.would like to know attendence for one subject")
    print("22.would like to know attendence of all subjects")
    a=int(input("Enter your choice:"))
    if a==11:
        est_one_sub_annual()
    elif a==22:
        est_all_sub_annual()
    else:
        est_annual_defult()

#--------------------------------------------------------------------------------------------------------------------
def d1():
    a1=input("this is wrong input, do you want to continue?(y/n)")
    if a1.lower()=="y":
        case1()
    else:
        print("thank you")
#-------------------------------------------------------------------------------------------------------------------
def case1():
    print("*-----------------------------------------------*")
    print("|                                               |")
    print("|    ANNUAL  ATTENDENCE CALCULATOR              |")
    print("|                                               |")
    print("*-----------------------------------------------*")
    
    print("1.would like to estimate abesents to be taken")
    print("2.would like to know percentage")
    a=int(input("Enter your choice:"))
    if a==1:
        estimate_annual()
    elif a==2:
        percentage_annual()
    else:
        d1()
#-----------------------------------------------------------------------------------------------------------------  
#===================================================================================================================  
#-----------------------------------------------------------------------------------------------------------------
def per_one_sub_month():
    #for one subject
    subject_name=input("enter subject name: ")

    total_count_t=int(input(f"enter total classes count of {subject_name} suject  in thoery: "))
    present_count_t=int(input(f"enter present classes count of {subject_name} suject in theory: "))
    total_count_p=int(input(f"enter total classes count of {subject_name} suject  in practical: "))
    present_count_p=int(input(f"enter present classes count of {subject_name} suject in practical: "))
    x1=(present_count_t*100)/(total_count_t)
    #print("Your number is ",x1)
    x2=(present_count_p*100)/(total_count_p)
    #print("Your number is ",x2)

    xt=int(input(f"enter theory classes per week in {subject_name}: "))
    xp=int(input(f"enter practical(including lab and tutorial) classes per week in {subject_name}: "))
    t=xt/(xt+xp)
    p=xp/(xt+xp)
    #week=total_count_t//xt
    #print(t,p)

    average=(x1*t)+(x2*p)
    #print(average)
    print(f"percentage in {subject_name} is {average}%")
    
def per_all_sub_month():
    n=int(input("enter total subjects you are interested to know their persentage attendance: "))

    subjects=[]
    percentage=[]

        
    for i in range(1,n+1):
        subject_name=input(f"enter subject{i} name: ")
        #print("DISCLAIMER: If there is no theory or practical classes for that respective subject, give input 1 for total classes count and 0 for present classes count")

        total_count_t=int(input(f"enter total classes count of {subject_name} suject  in thoery: "))
        present_count_t=int(input(f"enter present classes count of {subject_name} suject in theory: "))
        if total_count_t==0:
            total_count_t=1
        
        total_count_p=int(input(f"enter total classes count of {subject_name} suject  in practical: "))
        present_count_p=int(input(f"enter present classes count of {subject_name} suject in practical: "))
        if total_count_p==0:
            total_count_p=1
        
        x1=(present_count_t*100)/(total_count_t)
        #print("Your number is ",x1)
        x2=(present_count_p*100)/(total_count_p)
        #print("Your number is ",x2)

        xt=int(input(f"enter theory classes per week in {subject_name}: "))
        if xt==0:
            xt=1
        xp=int(input(f"enter practical(including lab and tutorial) classes per week in {subject_name}: "))
        t=xt/(xt+xp)
        p=xp/(xt+xp)
        #print(t,p)

        average=(x1*t)+(x2*p)
        #print(average)
        print("--------------------------------------------")
        print(f"percentage in {subject_name} is {average}%")
        print("--------------------------------------------")
        subjects.append(subject_name)
        percentage.append(average)
        
    per_sheet=pd.Series(percentage,index=subjects)
    print(per_sheet)
    
def per_month_default():
    a1=input("this is wrong input, do you want to continue?(y/n)")
    if a1.lower()=="y":
        percentage_month()
    else:
        print("thank you")

#-------------------------------------------------------------------------------------------------------------------
def est_one_sub_month():
    #for one subject
    def est_month1(a,subject_name):
        total_count=int(input("Enter total count of classes as mentioned in course policy) :"))
        
        xt=int(input(f"enter theory classes per week in {subject_name}: "))
        xp=int(input(f"enter practical(including lab and tutorial) classes per week in {subject_name}: "))
        #t=xt/(xt+xp)
        #p=xp/(xt+xp)
        #print(t,p)
        weeks=total_count//xt
        total_theory_classes=weeks*xt
        total_practical_classes=weeks*xp
        
        print("IN ", subject_name ,":" )
        classes_to_attended_theory=(a * total_theory_classes)/(100)  # even if 30.4 gives 31 preventing any chances of safety prediction
        #print("classes to be attended in theory is: ",classes_to_attended_theory)
        total_classes_theory_month=int(input(f"enter total count of theory classes in {subject_name} till this month: "))
        present_classes_theory_month=int(input(f"enter attended classes count of theory in {subject_name} till this month: "))
        balance_t=(total_classes_theory_month)-(present_classes_theory_month)
        absents_to_take1= (total_theory_classes)-(classes_to_attended_theory)
        if balance_t > absents_to_take1:
            print(f"You are in defaulter list, cause maximum leaves can be taken in {subject_name} is : {absents_to_take1}")
        else:
            absents_to_take11= (total_theory_classes)-(classes_to_attended_theory) - (balance_t)
            print( f"YOU CAN TAKE {absents_to_take11} LEAVES in theory classes")
            
        
        
        
        classes_to_attended_practical=(a * total_practical_classes)/(100)  # even if 30.4 gives 31 preventing any chances of safety prediction
        #print("classes to be attended in practical is: ",classes_to_attended_practical)
        total_classes_practical_month=int(input(f"enter total count of practical classes in {subject_name} till this month: "))
        present_classes_practical_month=int(input(f"enter attended classes count of practical in {subject_name} till this month: "))
        balance_p=(total_classes_practical_month)-(present_classes_practical_month)
        absents_to_take2= (total_practical_classes)-(classes_to_attended_practical)
        if balance_p > absents_to_take2:
            print(f"You are in defaulter list, cause maximum leaves can be taken in {subject_name} is : {absents_to_take2}")
        else:
            absents_to_take22= (total_practical_classes)-(classes_to_attended_practical) - (balance_p)
            print( f"YOU CAN TAKE {absents_to_take22} LEAVES in practical classes")
            
            total_absents=absents_to_take11 + absents_to_take22
            print("TOTAL YOU CAN TAKE LEAVE OF: ",total_absents)
        
     


    subject_name=input("enter subject name: ")
    print("Default attendance is calculated for 80% ")
    decision_default=input("Do you want change default attendance 80%? (y/n)")
    if decision_default.lower()=="y":
        default_per=int(input("Enter default percentage to be calculated: "))
        est_month1(default_per,subject_name)
    else:
        est_month1(80,subject_name)
        
        
def est_all_sub_month():
    #for all subjects
    import pandas as pd
    n=int(input("enter total subjects you are interested to know their persentage attendance: "))

    subjects=[]
    absents_to_take_theory=[]
    absents_to_take_practical=[]
    index1=[]

    def est_month2(a,n):
        for i in range(1,n+1):
            subject_name=input(f"enter subject{i} name: ")
            total_count=int(input(f"Enter total count of classes in {subject_name} as mentioned in course policy) :"))
            
            xt=int(input(f"enter theory classes per week in {subject_name}: "))
            xp=int(input(f"enter practical(including lab and tutorial) classes per week in {subject_name}: "))
            weeks=total_count//xt
            total_theory_classes=weeks*xt
            total_practical_classes=weeks*xp
            
            
            print("IN ", subject_name ,":" )
            classes_to_attended_theory=(a * total_theory_classes)//(100)+1  # even if 30.4 gives 31 preventing any chances of safety prediction
            #print("classes to be attended in theory is: ",classes_to_attended_theory)
            total_classes_theory_month=int(input(f"enter total count of theory classes in {subject_name} till this month: "))
            present_classes_theory_month=int(input(f"enter attended classes count of theory in {subject_name} till this month: "))
            balance_t=(total_classes_theory_month)-(present_classes_theory_month)
            absents_to_take1= (total_theory_classes)-(classes_to_attended_theory)
            if balance_t > absents_to_take1:
                z1=balance_t-absents_to_take1
                print(f"You are in defaulter list, cause maximum leaves can be taken in {subject_name} is : {absents_to_take1}")
                absents_to_take_theory.append(f"default by {z1}")
            else:
                absents_to_take11= (total_theory_classes)-(classes_to_attended_theory) - (balance_t)
                print( f"YOU CAN TAKE {absents_to_take11} LEAVES in theory classes")
                absents_to_take_theory.append(absents_to_take11)
                
            
            
            
            classes_to_attended_practical=(a * total_practical_classes)//(100)+1  # even if 30.4 gives 31 preventing any chances of safety prediction
            #print("classes to be attended in practical is: ",classes_to_attended_practical)
            total_classes_practical_month=int(input(f"enter total count of practical classes in {subject_name} till this month: "))
            present_classes_practical_month=int(input(f"enter attended classes count of practical in {subject_name} till this month: "))
            balance_p=(total_classes_practical_month)-(present_classes_practical_month)
            absents_to_take2= (total_practical_classes)-(classes_to_attended_practical)
            if balance_p > absents_to_take2:
                z2=balance_p-absents_to_take2
                print(f"You are in defaulter list, cause maximum leaves can be taken in {subject_name} is : {absents_to_take2}")
                absents_to_take_practical.append(f"default by {z2}")
            else:
                absents_to_take22= (total_practical_classes)-(classes_to_attended_practical) - (balance_p)
                print( f"YOU CAN TAKE {absents_to_take22} LEAVES in practical classes")
                absents_to_take_practical.append(absents_to_take22)
                
                
            if (balance_t < absents_to_take1) and (balance_p < absents_to_take2):
                total_absents=absents_to_take11 + absents_to_take22
                print("TOTAL YOU CAN TAKE LEAVE OF: ",total_absents)
                
            
            
            
            index1.append(i)
            subjects.append(subject_name)
            
            
            data = {'subject name': subjects, 'safe absents in theroy': absents_to_take_theory, 'safe absents in practical': absents_to_take_practical}
            
        est_sheets=pd.DataFrame(data,index=index1)
        print(est_sheets)
        
        print("Thank you")
        



    print("Default attendance is calculated for 80% ")
    decision_default=input("Do you want change default attendance 80%? (y/n)")

    if decision_default.lower()=="y":
        default_per=int(input("Enter default percentage to be calculated: "))
        est_month2(default_per,n)
    else:
        est_month2(80,n)

def est_month_defult():
    a1=input("this is wrong input, do you want to continue?(y/n)")
    if a1.lower()=="y":
        estimate_month()
    else:
        print("thank you")
    
#-------------------------------------------------------------------------------------------------------------------
def percentage_month():
    print("11.would like to know attendence for one subject")
    print("22.would like to know attendence of all subjects")
    a=int(input("Enter your choice:"))
    if a==11:
        per_one_sub_month()
    elif a==22:
        per_all_sub_month()
    else:
        per_month_default()
        
def estimate_month():
    print("11.would like to know attendence for one subject")
    print("22.would like to know attendence of all subjects")
    a=int(input("Enter your choice:"))
    if a==11:
        est_one_sub_month()
    elif a==22:
        est_all_sub_month()
    else:
        est_month_defult()


#---------------------------------------------------------------------------------------------------------------
def d2():
    a1=input("this is wrong input, do you want to continue?(y/n)")
    if a1.lower()=="y":
        case2()
    else:
        print("thank you")
#---------------------------------------------------------------------------------------------------------------
def case2():
    print("*-----------------------------------------------*")
    print("|                                               |")
    print("|    MONTH  ATTENDENCE CALCULATOR               |")
    print("|                                               |")
    print("*-----------------------------------------------*")
    
    print("1.would like to estimate abesents to be taken")
    print("2.would like to know percentage")
    a=int(input("Enter your choice:"))
    if a==1:
        estimate_month()
    elif a==2:
        percentage_month()
    else:
        d2()



    
#---------------------------------------------------------------------------------------------------------------
def default():
    print("This is the default case")
    
#------------------------------------------------------------------------------------------------------------------



# Define a dictionary to map cases to functions  
switch_dict = {
    1: case1,
    2: case2
}
# Set a default function for cases not in the dictionary
default_case = default

# Use get() to retrieve the function for the given case, defaulting to the default_case function
selected_case = switch_dict.get(user_input, default_case)
selected_case()