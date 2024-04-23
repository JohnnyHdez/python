def decorador(func_param):
    def datos(*args):
        print("Esta es una operación matemática")
        return func_param(*args)
    return datos


@decorador
def suma(*args: float):
    total = 0
    for x in args:
        total += x
    return total



mi_suma = suma(180.00,1.51, 8.60)
print("Total = {}".format(mi_suma))