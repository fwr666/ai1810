

from student_info import *
from menu import *


doc = []
while True:

    show_menu()

    ch = input('请输入命令')

    if ch == '1':
        doc += input_student()

    elif ch == '2':
        output_student(doc)

    elif ch == '3':
        doc = delete_student(doc)

    elif ch == '4':
        doc = modify_student_score(doc)

    elif ch == '5':
        output_student_by_score_desc(doc)

    elif ch == '6':
        putput_student_by_score_asc(doc)

    elif ch == '7':
        putput_student_by_age_desc(doc)

    elif ch == '8':
        age_lower_to_high(doc)

    elif ch == '9':
        doc=read_file()

    elif ch == '10':
        save_file(doc)

    elif ch == 'q':
        break
    else:
        print('没有这个命令')
