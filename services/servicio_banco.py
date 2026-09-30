from functools import reduce
from services.configuracion import Configuracion

# REGLA DE NEGOCIO: depósitos deben ser positivos; un retiro no puede superar el saldo.
def depositar(saldo: float, cantidad: float) -> float:
    return saldo + cantidad if cantidad > 0 else saldo

def retirar(saldo: float, cantidad: float) -> float:
    return saldo - cantidad if cantidad > 0 and cantidad <= saldo else saldo

depositar_lambda=lambda saldo,cantidad: saldo+cantidad if cantidad>0 else saldo
retirar_lambda=lambda saldo,cantidad: saldo-cantidad if cantidad>0 and cantidad<=saldo else saldo

def demostracion_funcional(saldo: float):
    cfg=Configuracion(); movimientos=cfg.obtener("banco","movimientos_prueba",[])
    mapa=map(lambda m:saldo+m, movimientos); tipo_map=type(mapa).__name__; transformados=list(mapa)
    minimo=cfg.obtener("banco","deposito_minimo_filtro",0)
    filtro=filter(lambda m:m>=minimo, movimientos); tipo_filter=type(filtro).__name__; seleccionados=list(filtro)
    neto=reduce(lambda a,b:a+b, movimientos,0)
    return movimientos, transformados, seleccionados, neto, tipo_map, tipo_filter
