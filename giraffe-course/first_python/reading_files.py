'''import os.path
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'teste')'''

#reading files
'''exercise = open('teste', 'r') 
for list in exercise.readlines():
    print(list)
exercise.close()'''

exercise = open('newtest', 'w') 
exercise.write("\nTestando teste")
exercise.close()

