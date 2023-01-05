# This function print instruction calculator
def print_instructions():
    print("Eliga una Operación del Menu")
    print("Realice el número de operaciones que usted desee")
    print("Todas Operaciones en el menú del 1 al 3 admiten N Valores")


# This function print main menu
def print_menu():
    print("MENU:")
    menu = {
        "1": "Sumar",
        "2": "Restar",
        "3": "Multiplicar",
        "4": "Dividir",
        "5": "Raiz N",
        "6": "Exponente N ",
        "7": "Seno",
        "8": "Conseno",
        "9": "Tangente",
    }
    print(menu)


# This function print exit menu
def print_menu_salida():
    print("Seleccione una Opción")
    print("10. Regresar al Menu Principal")
    print("11. Volver a Realizar la Misma Operación")
    print("12. Apagar")
