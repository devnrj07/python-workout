#Temparature conversion from Farahneit to Celsius

print('\nWelcome to the temperature conversion app')

temp_F = float(input(f'\nEnter temperature in Farhaneit: '))

temp_C = round((temp_F -32)*(5/9),4)
temp_K = round(temp_C+273.15,4)

print(f'\n {temp_F} F is {temp_C} C. ')
print(f'\n {temp_F}F is {temp_K} K. ')
