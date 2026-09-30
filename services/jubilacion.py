from functools import reduce
from services.configuracion import Configuracion

# REGLA DE NEGOCIO: pensión y años de retiro deben ser mayores que cero.
def calcular_dinero_jubilacion(pension_mensual: float, anios_retiro: int) -> float:
    return pension_mensual * 12 * anios_retiro if pension_mensual > 0 and anios_retiro > 0 else 0

calcular_dinero_jubilacion_lambda = lambda pension_mensual, anios_retiro: pension_mensual * 12 * anios_retiro if pension_mensual > 0 and anios_retiro > 0 else 0

def demostracion_funcional(pension_mensual: float):
    cfg=Configuracion(); anios=cfg.obtener("jubilacion","anios_prueba",[]); meses=cfg.obtener("jubilacion","meses_anio",12)
    mapa=map(lambda a:pension_mensual*meses*a, anios); tipo_map=type(mapa).__name__; transformados=list(mapa)
    minimo=cfg.obtener("jubilacion","monto_minimo_filtro",0)
    filtro=filter(lambda m:m>=minimo, transformados); tipo_filter=type(filtro).__name__; seleccionados=list(filtro)
    total=reduce(lambda a,b:a+b, transformados,0)
    return anios, transformados, seleccionados, total, tipo_map, tipo_filter
