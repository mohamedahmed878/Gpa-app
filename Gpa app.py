# Gpa app 
print (" hello in Gpa calculator app ")

#Add the names of college subjects
# 100 grade

math = input("Add the student's grades in a subject math: ")

english = input("add the student is grades in a subject english: ")

Microsoft = input("add the student is grades in a subject Microsoft: ")

Cyber = input("add the student is grades in a subject cyber: ")

iot = input("add the student is grades in a subject iot: ")

C_programming = input("add the student is grades in a subject english: ")

#Add a variable to collect materials
sum =  math + english + Microsoft + Cyber + iot + C_programming 

#add variables percentage 
precentage = float(sum) / 600
 
#Gpa 
Gpa = precentage / 0.25

if Gpa >= 3.7:
    print("your  grade 'A' :" + str(Gpa))

elif Gpa >= 2.7:
    print(" your is grade 'B':" + str(Gpa))

elif Gpa >= 1.7 :
    print("your is grade 'C': " + str(Gpa))

elif Gpa >= 1:
    print("your is grade 'D':" + str(Gpa)) 

else :
    print("your is grade 'F':" + str(Gpa))

#message 
print("thank you for use our app")      