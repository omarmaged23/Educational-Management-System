from TeacherModule import TeacherHomeGUI
from Environment import Db_Creation as Db_Creation
from Environment import Db_Queries as Db_Queries
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Db_Creation.create_All_Tables()

# Db_Queries.insert_teacher("al", 20, "al20", "153", "012", "dd", "2020-02-05", "gg")
# Db_Queries.insert_teacher("ka", 10, "ka10", "153", "012", "dd", "2020-02-05", "gg")
# Db_Queries.insert_teacher("ma", 30, "ma30", "153", "012", "dd", "2020-02-05", "gg")

# Db_Queries.insert_student("st1", 20, "st20", "153", "012", "2020-02-05", "gg")
# Db_Queries.insert_student("st2", 10, "st10", "153", "012", "2020-02-05", "gg")
# Db_Queries.insert_student("st3", 30, "st30", "153", "012", "2020-02-05", "gg")

# Db_Queries.insert_subscription(1, 1)
# Db_Queries.insert_subscription(1, 2)
# Db_Queries.insert_subscription(1, 3)
# Db_Queries.insert_subscription(2, 1)
# Db_Queries.insert_subscription(2, 2)
# Db_Queries.insert_subscription(3, 3)

# Db_Queries.delete_Subscription(1, 1)

# Db_Queries.insert_Lecture("logic", "gg", "vv", "2020-10-5", "oo", "1", 1)

# Db_Queries.insert_Quiz("logic", 10, 1, 10, 1)
# Db_Queries.delete_Quiz(1)

# Db_Queries.insert_Student_Lecture(1, 1)

# Db_Queries.insert_Student_Quiz(50, "15", "2020-5-6", 1, 1)

# Db_Queries.insert_Question("choose", "h", "k", "l", "s", "s", 1)

# Db_Queries.delete_Question(1)

# Db_Queries.insert_Lecture_Quiz(1, 1)



#print(Db_Queries.Get_Teacher(1))
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
