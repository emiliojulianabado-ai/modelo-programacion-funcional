import json
from pathlib import Path

class Configuracion:
    """Carga valores inmutables de las prácticas desde un archivo JSON."""
    def __init__(self, archivo=None):
        base = Path(__file__).resolve().parent.parent
        self.archivo = Path(archivo) if archivo else base / "data" / "constantes.json"
        with self.archivo.open("r", encoding="utf-8") as f:
            self._datos = json.load(f)

    def obtener(self, seccion, clave, predeterminado=None):
        return self._datos.get(seccion, {}).get(clave, predeterminado)
