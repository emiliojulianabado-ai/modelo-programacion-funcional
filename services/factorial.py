from functools import reduce
from services.configuracion import Configuracion

# REGLA DE NEGOCIO: el factorial solo se calcula para enteros no negativos.
def factorial(n: int) -> int:
    if n < 0: return 0
    if n == 0: return 1
    resultado = 1
    for i in range(1,n+1): resultado *= i
    return resultado

factorial_lambda = lambda n: 0 if n < 0 else (1 if n == 0 else reduce(lambda x,y:x*y, range(1,n+1),1))

def demostracion_funcional(n: int):
    cfg=Configuracion(); base=cfg.obtener("factorial","numeros_prueba",[])
    datos=[x for x in base if x <= max(n,1)] or [1]
    mapa=map(lambda x:x*x, datos); tipo_map=type(mapa).__name__; transformados=list(mapa)
    minimo=cfg.obtener("factorial","minimo_filtro",1)
    filtro=filter(lambda x:x>=minimo, datos); tipo_filter=type(filtro).__name__; seleccionados=list(filtro)
    acumulado=reduce(lambda a,b:a*b, range(1,n+1),1)
    return datos, transformados, seleccionados, acumulado, tipo_map, tipo_filter
