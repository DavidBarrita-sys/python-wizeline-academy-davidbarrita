import functions_calculator as calculator
import print_option as printer
import re


def use_regex(input_text):
    x = re.findall("[1-13]", input_text)
    return x


def fixToIntegerOrFloat(num):
    set_number = set(num)
    if "." in set_number:
        return float(num)
    else:
        return int(num)


def return_string_user(option):
    if option == "1":
        print("1: Sumar ")
    elif option == "2":
        print("2: Restar")
        print("Usted Puede Restar Dos Numeros o a un Numero Objetivo Los N Numeros que Usted Guste")
    elif option == "3":
        print("3: Multiplicar")
    elif option == "4":
        print("4: Dividir")
        print("El Primer Valor es el Dividor y El Segundo es el Divisor, Debe Agregar Dos Valores")
    elif option == "5":
        print("5: Raiz N")
    elif option == "6":
        print("6: Exponente")
        print("El Primer Numero es la Base y el Segundo Valor es el Exponente, Debe Agregar Dos Valores")
    elif option == "7":
        print("7: Seno")
    elif option == "8":
        print("8: Conseno")
    elif option == "9":
        print("9: Tangente")

    else:
        return "Agregue un número válido"


def return_result_calculator(option, values):
    values_two = values
    if option == "1":
        print("El Resultado  de la Suma es:")
        return calculator.addition(values_two)

    elif option == "2":
        if len(values_two) == 2:
            print("El Resultado  de la Resta de Dos Numeros es:")
            return calculator.subtract_by_simple(values_two)
        return calculator.subtract_by_target(values_two)

    elif option == "3":
        if len(values_two) == 2:
            return calculator.multiplication_by_simple(values_two)
        return calculator.multiplication_by_n_values(values_two)

    elif option == "4":
        print("4: Dividir")
        if len(values_two) > 2 or len(values_two) == 1:
            return "Operación No Permitada Solo La Division Adminte Dos Valores"
        if len(values_two) == 2:
            return calculator.divide_by_simple(values_two)

    elif option == "5":
        print("5: Raiz N")
        if len(values_two) == 1:
            return calculator.root_by_simple(values_two)
        return calculator.root_by_n_values(values_two)

    elif option == "6":
        print("6: Exponente N")
        if len(values_two) > 2 or len(values_two) == 1:
            print("Esta Operación Solo Permite Dos Valores")
        if len(values_two) == 2:
            return calculator.pow_by_simple(values_two)

    elif option == "7":
        print("7: Seno")
        if len(values_two) == 1:
            return calculator.sin_by_simple(values_two)
        return calculator.sin_by_n_values(values_two)
    elif option == "8":
        print("8: Conseno")
        if len(values_two) == 1:
            return calculator.cos_by_simple(values_two)
        return calculator.cos_by_n_values(values_two)

    elif option == "9":
        print("9: Tangente")
        if len(values_two) == 1:
            return calculator.cos_by_simple(values_two)
        return calculator.tan_by_n_values(values_two)

    else:
        return "Agregue un número válido"


def get_values_by_user(option_menu):
    return_string_user(option_menu)
    inputs_number = input("Ingresa la Cantidad de Numeros a Digitar: ")
    inputs_number = int(inputs_number)
    inputs_user = 0
    values = []
    while inputs_user < inputs_number:
        val = input("Ingresa el " + str(inputs_user + 1) + " Numero que Deseas " + ": ")
        values.append(fixToIntegerOrFloat(val))
        inputs_user += 1
    print("--- El Resultado de la Operación: --- ")
    print(return_result_calculator(option_menu, values))
    print("------------------------------------- ")


def home():
    printer.print_instructions()
    printer.print_menu()


def get_option_menu():
    type_operation = input("Ingresa Una Opción del Menu: ")
    return type_operation


def get_option_out():
    exit_option = input(": ")
    return exit_option
