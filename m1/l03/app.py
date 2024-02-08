payRate = float(input("Pago por Hora: ")) 
hourRate = float(input("Horas trabajadas: "))

overtime = 0

if (hourRate > 40):
    overtimeHours = hourRate - 40
    totalPay = (40 * payRate) + (overtimeHours * (payRate * 2))
    print("El empleado trabajo overtime.")
    print(f"El sueldo a pagar al empleado es {totalPay}")

elif (hourRate > 40):
    print("El empleado trabajo overtime.")

else:
    totalPay = (hourRate * payRate)
    print(f"El sueldo a pagar al empleado es {totalPay}")