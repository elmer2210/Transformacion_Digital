def calcular_promedio(numeros):
    """
    Calcula el promedio aritmético de una lista de números.

    Args:
        numeros (list): Una lista que contiene números enteros o flotantes.

    Returns:
        float: El valor promedio de los números proporcionados.

    Raises:
        ValueError: Si la lista proporcionada está vacía, para evitar 
                    el error de división por cero.
    """
    if not numeros:
        raise ValueError("La lista de números no puede estar vacía.")
    
    return sum(numeros) / len(numeros)

# --- Ejemplo de uso ---
edades = [22, 25, 20, 28, 21]
promedio_edades = calcular_promedio(edades)
print(f"El promedio es: {promedio_edades}")