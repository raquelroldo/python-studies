'''8 - Faça um programa que solicite a data de nascimento 
(dd/mm/aaaa) do usuário e imprima a data com o nome do mês por 
extenso.'''
day = input("Enter you day of birth eg.:(02): ")
month = input("Enter you month of birth eg.:(05): ")
year = input("Enter you year of birth eg.:(2000): ")


monthConvertion = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
for month, value in monthConvertion:
    if value == monthConvertion.keys:
        print(month)
birthday = print(day, month, year)