print("-------------")
name = input("Enter student name:")
roll_no = input("Enter Roll No.")
maths_score = float(input("Enter marks in Maths:"))
physics_score = float(input("Enter marks in Physics:"))
chemistry_score = float(input("Enter marks in chemistry:"))
print("-------------")
print("Here is the grade card:")
print("-------------")
print("Student Name:", name)
print("Student Roll:", roll_no)
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'
    
print("Grade in Maths:", calculate_grade(maths_score))
print("Grade in Physics:", calculate_grade(physics_score))
print("Grade in Chemistry:", calculate_grade(chemistry_score))
overall_score = (maths_score + physics_score + chemistry_score)/3
overall_grade = calculate_grade(overall_score)
print("Overall Grade:", overall_score)
print("-------------")
