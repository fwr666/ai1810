

from student_info import *
from menu import *
while True:
    show_menu()
    ch = input('请输入命令')
    if ch == '1':
        input_student()
    elif ch == '2':
        output_student(infos)
    elif ch == '3':
        delete_student()
    elif ch == '4':
        modify_student_score(infos)
    elif ch == '5':
        output_student_by_score_desc(infos)
    elif ch == '6':
        putput_student_by_score_asc(infos)
    elif ch == '7':
        putput_student_by_age_desc(infos)
    elif ch == '8':
        age_lower_to_high(infos)
    elif ch == '9':
        read_file()
    elif ch == '10':
        save_file(infos)
    elif ch == 'q':
        break
    else:
        print('没有这个命令')

