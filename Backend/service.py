import random

def validateInput(options, winners):
    errors = []

    if options is None or winners is None:
        errors.append("No puede haber datos vacíos")
        return errors

    if not isinstance(winners, int):
        errors.append("El número de ganadores debe ser un entero")

    if not isinstance(options, list) or len(options) < 2:
        errors.append("La lista de opciones debe contener al menos 2 elementos")

    if isinstance(winners, int) and winners > len(options):
        errors.append("No puede haber más ganadores que opciones disponibles")

    return errors

def selectRandomElement(options: list[str], winners:int)->list[str]:
    return random.sample(options, winners)
    
def service(options: list[str], winners: int) -> dict[str, any]:
    errors = validateInput(options, winners)
    if len(errors) == 0:
        return {"elección": selectRandomElement(options, winners)}
    else:
        return {"errors": errors}