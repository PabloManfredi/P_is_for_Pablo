def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir (a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b

def multiplicar (n1, n2):
    return n1 * n2

def main ():
   
    opciones = input("Ingrese el numero de la operacion que desea realizar:\n"+"1-Suma\n2-Resta\n3-Multiplicacion\n4-Division\n")
    if opciones in ["1","2","3","4"]:
        n1 = float(input("Determine el primer numero:\n"))
        n2 = float(input("Determine el segundo numero:\n"))
        if opciones == "1":
            resultado =sumar(n1,n2)
        elif opciones == "2":
            resultado =restar(n1,n2)
        elif opciones == "3":
            resultado =multiplicar(n1,n2)
        elif opciones == "4":
            resultado =dividir(n1,n2)
        print(f"El resultado es: {resultado}")

main()





















































# def introducir_numero ():
#     n1 = int(input("ingrese el primer numero:\n"))
#     n2 = int(input("ingrese el  segundo numero:\n"))
#     return n1,n2                    


# def realizar_operaciones(numero_1, numero_2):
#      resultados = []
#      funciones = [sumar, restar, multiplicar, dividir]
#      for funcion in funciones:
#          resultado = funcion(numero_1, numero_2)
#          if resultado is not None:
#              resultados.append(resultado)
#          else:
#              resultados.append("No se puede dividir por cero")
#      return resultados







# def mostrar_resultado(resultados):
#     print("Resultados:")
#     for resultado in resultados:
#         print(resultado)

# def main_programa():
#     numero_1, numero_2 = introducir_numero()
#     resultados = realizar_operaciones(numero_1, numero_2)
#     mostrar_resultado(resultados)

    

# main_programa()