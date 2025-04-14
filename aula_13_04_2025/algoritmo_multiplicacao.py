def multiplicacao():
    x = str(input("Informe o primeiro operando: "))
    y = str(input("Informe o segundo operando: "))
    resultado = 0
    op1 = ['','','','']
    op2 = ['','','','']
    for i in range(3,-1,-1):
        op1[i] = int(x[i])
    for i in range(3,-1,-1):
        op2[i] = int(y[i])
    for i in range(3,-1,-1):
        for c in range(3,-1,-1):
            resultado_parcial = 0
            resultado_parcial = i * c 
            if resultado_parcial > 9:
                resultado_parcial % 10
                resultado = resultado + resultado_parcial
                vai_um = resultado_parcial // 10
            resultado = resultado + resultado_parcial
    print(resultado)
    print(op1)
    print(op2)
multiplicacao()


'''
x = '1234'
op1 = ['','','','']
for i in range(3, -1, -1):
    op1[i] = int(x[i])
    print(op1)'''