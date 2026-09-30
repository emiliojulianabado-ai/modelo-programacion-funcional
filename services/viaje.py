from functools import reduce
from services.configuracion import Configuracion

# REGLA DE NEGOCIO: la velocidad debe ser mayor que cero para calcular el tiempo.
def calcular_tiempo_viaje(distancia: float, velocidad: float):
    if velocidad <= 0: return 0,0
    total=round((distancia/velocidad)*60)
    return total//60,total%60

calcular_tiempo_viaje_lambda=lambda distancia,velocidad: ((round((distancia/velocidad)*60)//60, round((distancia/velocidad)*60)%60) if velocidad>0 else (0,0))

def demostracion_funcional(velocidad: float):
    cfg=Configuracion(); distancias=cfg.obtener("viaje","distancias_prueba",[]); minimo=cfg.obtener("viaje","minutos_minimos_filtro",0)
    mapa=map(lambda d:round((d/velocidad)*60) if velocidad>0 else 0, distancias); tipo_map=type(mapa).__name__; transformados=list(mapa)
    filtro=filter(lambda m:m>=minimo, transformados); tipo_filter=type(filtro).__name__; seleccionados=list(filtro)
    total=reduce(lambda a,b:a+b, transformados,0)
    return distancias, transformados, seleccionados, total, tipo_map, tipo_filter
