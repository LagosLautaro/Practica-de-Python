from random import randrange,choice
from datetime import datetime

operators = ["+","-","*","/"]
times = 5
respuestas_correctas = 0
respuestas_incorrectas = 0
init_time = datetime.now()
print(f"Cuanto tardas en responder {times} operaciones?")
for i in range(0,times):
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    print(f"{i+1}- Cuanto es {number_1} {operator} {number_2}?")
    result = int(input("Resultado: "))
    if operator == "+":
        result_correcto = number_1 + number_2
    elif operator == "-":
        result_correcto = number_1 - number_2
    elif operator == "*":
         result_correcto = number_1 * number_2
    else:
        result_correcto = number_1 / number_2
    
    if result == result_correcto:
        print(f"Respuesta correcta!")
        respuestas_correctas += 1
    else:
       print(f"Respuesta incorrecta!")
       respuestas_incorrectas += 1

end_time = datetime.now()
total_time = end_time - init_time
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Tuviste {respuestas_correctas} respuestas correctas y {respuestas_incorrectas} incorrectas!")
