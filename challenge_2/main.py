#program to convert Miles per hour to meters per second

speed_mph = input(f'\nEnter the speed in MPH: ')

speed_mps = round(float(speed_mph)/2.237,2)

print(f'{speed_mph}MPH converts to {speed_mps} MPS')