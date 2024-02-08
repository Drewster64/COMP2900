payRate = float(input("Pago por Hora: ")) 
hourRate = float(input("Horas trabajadas: "))

if hourRate > 40:
    overtimeHours = hourRate - 40
    overtimePay = overtimeHours * (payRate * 2)
    regularPay = 40 * payRate
    grossPay = regularPay + overtimePay
    netPay = grossPay - (grossPay * 0.15)
    print("El empleado trabajó overtime.")
    print(f"El sueldo bruto del empleado es {grossPay}")
    print(f"El sueldo neto del empleado es {netPay}")
else:
    grossPay = hourRate * payRate
    netPay = grossPay - (grossPay * 0.15)
    print(f"El sueldo bruto del empleado es {grossPay}")
    print(f"El sueldo neto del empleado es {netPay}")
