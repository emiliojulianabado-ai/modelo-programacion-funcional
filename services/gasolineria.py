from functools import reduce
from services.configuracion import Configuracion

# REGLA DE NEGOCIO: el rendimiento debe ser mayor que cero para evitar división entre cero.
def calcular_consumo_gasolina(distancia: float, rendimiento: float) -> float:
    return distancia / rendimiento if rendimiento > 0 else 0

calcular_consumo_gasolina_lambda = lambda distancia, rendimiento: distancia / rendimiento if rendimiento > 0 else 0

def demostracion_funcional(rendimiento: float):
    cfg = Configuracion()
    datos = cfg.obtener("gasolina", "distancias_prueba", [])
    minimo = cfg.obtener("gasolina", "consumo_minimo_filtro", 0)
    mapa = map(lambda d: round(d / rendimiento, 2) if rendimiento > 0 else 0, datos)
    tipo_map = type(mapa).__name__
    transformados = list(mapa)
    filtro = filter(lambda c: c >= minimo, transformados)
    tipo_filter = type(filtro).__name__
    seleccionados = list(filtro)
    total = reduce(lambda a, b: a + b, transformados, 0)
    return datos, transformados, seleccionados, round(total,2), tipo_map, tipo_filter
