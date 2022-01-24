def creat_student(name, korean, math, english, science):
    return {"name": name, "korean": korean, "math": math,\
            "english": english, "science": science}

# 두번째 코드 작성 중

# 학생의 총점과 평균을 구하는 함수
def student_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_average(student):
    return student_sum(student) / 4

def print_student(student):
    print("{}   {}  {}".format(student["name"], student_sum(student), student_average(student)))






# 학생 리스트 선언
students = [
    creat_student("윤인성", 87, 98, 88, 95),
    creat_student("연하진", 92, 98, 96, 98),
    creat_student("구지연", 76, 96, 94, 90),
    creat_student("나선주", 98, 92, 96, 92),
    creat_student("윤아린", 95, 98, 98, 98),
    creat_student("윤명월", 64, 88, 92, 92)
]

print("{}    {}  {}".format("이름", "총점", "평균" ))

for student in students:
    print_student(student)