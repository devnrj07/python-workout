# Basketball roster program
print(f'\n welcome to the IBA Roster program')

roster:list = []

point_guard = input('\n Who is your point guard: ').capitalize()
roster.append(point_guard)
shooting_guard = input('\n Who is your shooting guard: ').capitalize()
roster.append(shooting_guard)
small_forward = input('\n Who is your small forward: ').capitalize()
roster.append(small_forward)
power_forward = input('\n Who is your power forward: ').capitalize()
roster.append(power_forward)
center = input('\n Who is your center : ').capitalize()
roster.append(center)

print('\n Your starting 5 for upcoming season')
print(f'\n Point guard : \t\t\t {roster[0]}')
print(f'\n Shooting guard : \t\t {roster[1]}')
print(f'\n Small forward : \t\t {roster[2]}')
print(f'\n Power forward : \t\t {roster[3]}')
print(f'\n Center : \t\t\t {roster[4]}')

print(f'\n ufh! {roster[2]} is injured')
roster.remove(roster[2])
print(f'\n Your rooster has {len(roster)} players')
new_small_forward = input(f'\n Who will be the replacement for {small_forward}: ').capitalize()
roster.insert(2,new_small_forward)

print(f'\n Your rooster has {len(roster)} players now')

print('\n Your updated roster with 5 for upcoming season')
print(f'\n Point guard : \t\t\t {roster[0]}')
print(f'\n Shooting guard : \t\t {roster[1]}')
print(f'\n Small forward : \t\t {roster[2]}')
print(f'\n Power forward : \t\t {roster[3]}')
print(f'\n Center : \t\t\t {roster[4]}')

print(f'\n Good luck {roster[2]}. You\'ll do great')