print('O seguinte programa converte a temperatura em celsius para fahrenheit e kelvin\n')

c = float(input('A temp. em celsius (°C): '))

print(f'''
    Temp em °C = {c}°
    Temp em °F = {((9*c)/5)+32}°
    Temp em °K = {c+273}°''')