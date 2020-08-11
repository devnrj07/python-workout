#Favourite Teachers program

#helper function
def print_teachers(teachers_list:list) -> list :
    print(f'\nTeachers in order of favouritness : {teachers_list}')
    sorted_teacher = sorted(teachers_list)
    reverse_sorted_teacher = sorted(teachers_list, reverse=True)
    print(f'\n Teachers sorted alphabetically : {sorted_teacher}')
    print(f'\n Teachers sorted in reverse alphabetical order : {reverse_sorted_teacher}')
    print(f'\n The top two teachers are : {fav_teachers[0:2]}')
    print(f'\n The next top teachers are : {fav_teachers[2:4]}')
    print(f'\n The last teacher is : {fav_teachers[-1]}')
    print(f'\n Total no. of teachers : {len(fav_teachers)}')


print('\n Welcome to Favourite Teacher program')
fav_teachers = list()

for i in range(0,5):
    teacher_name = input(f'\n {i+1} : Enter your favourite Teacher No. {i+1}\'s last name: ').title()
    fav_teachers.append(teacher_name)

print_teachers(fav_teachers)

#replace a new favourite teacher
new_top_fav_teacher = input('\n unfortunately your top favourite teacher left. Which is your next top teacher ? : ').title()
removed_teacher = fav_teachers.pop(0)
fav_teachers.insert(0,new_top_fav_teacher)
print_teachers(fav_teachers)

#remove an unfavourite teacher
remove_teacher = input('\n oh! Looks like we\'re recieving a complain for a techer. Which one is it ?').title()
fav_teachers.remove(remove_teacher)
print_teachers(fav_teachers)

print('\n Nice we had fun!!')


