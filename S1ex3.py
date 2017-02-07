Segundos = input("Por favor, entre com o número de segundos que deseja converter:")

dias = int(Segundos)//(3600*24)
segundosrestantes = int(Segundos)%(3600*24)

horas = segundosrestantes//3600
segundosrestantes = segundosrestantes%3600

minutos = segundosrestantes//60
segundosrestantes = segundosrestantes%60

print (dias,"dias,",horas,"horas,",minutos,"minutos e",segundosrestantes,"segundos.")


