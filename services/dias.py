from datetime import date, timedelta
from functools import reduce
from services.configuracion import Configuracion

# REGLA DE NEGOCIO: la fecha de nacimiento no puede ser posterior a la fecha actual.
def calcular_dias_vividos(fecha_nacimiento: date) -> int:
    return (date.today() - fecha_nacimiento).days if fecha_nacimiento <= date.today() else 0

calcular_dias_vividos_lambda = lambda fecha_nacimiento: (date.today() - fecha_nacimiento).days if fecha_nacimiento <= date.today() else 0

def demostracion_funcional():
    cfg = Configuracion()
    anios = cfg.obtener("dias_vividos", "anios_referencia", [])
    minimo = cfg.obtener("dias_vividos", "dias_minimos_filtro", 0)
    fechas = list(map(lambda a: date.today() - timedelta(days=a*365), anios))
    mapa = map(lambda f: (date.today()-f).days, fechas)
    tipo_map = type(mapa).__name__
    transformados = list(mapa)
    filtro = filter(lambda d: d >= minimo, transformados)
    tipo_filter = type(filtro).__name__
    seleccionados = list(filtro)
    total = reduce(lambda a,b: a+b, transformados, 0)
    return [f.isoformat() for f in fechas], transformados, seleccionados, total, tipo_map, tipo_filter
