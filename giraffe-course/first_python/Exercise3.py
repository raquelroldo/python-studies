'''3- Faça um programa que leia 2 strings e informe o conteúdo 
delas seguido do seu comprimento. Informe também se as duas strings 
possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.'''

str1 = "Fazer uma casinha no alto de um morro eh tudo o que pedi pra Jah."
str2 = "Surfar uma onda no guaiba."


if str1 == str2:
    print("Is equal")
else:
    print("As strings nao sao iguais \n", str1, len(str1), str2, len(str2))
