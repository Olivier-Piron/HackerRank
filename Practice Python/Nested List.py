# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    li = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name, score])

    sorted_students = sorted(li, key = lambda x: x[1])

    second_lowest_score = sorted(list(set([x[1] for x in sorted_students])))[1]
    desired_students = []
    
    for student in sorted_students:
        if student[1] == second_lowest_score:
            desired_students.append(student[0])
    print("\n".join(sorted(desired_students)))