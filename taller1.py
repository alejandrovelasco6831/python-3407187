from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Base de datos falsa
facturas = []
transacciones = []

# MODELOS

class Factura(BaseModel):
    id: int
    fecha: str
    valor_total: float
    cliente: str

class Transaccion(BaseModel):
    id: int
    vr_unitario: float
    cantidad: int
    factura_id: int

# INICIO

@app.get("/")
def inicio():
    return {"mensaje": "CRUD con FastAPI"}

# =====================
# FACTURAS
# =====================

@app.get("/facturas")
def obtener_facturas():
    return facturas

@app.post("/facturas")
def crear_factura(factura: Factura):
    facturas.append(factura)
    return {
        "mensaje": "Factura agregada",
        "factura": factura
    }

@app.put("/facturas/{id}")
def actualizar_factura(id: int, factura_actualizada: Factura):

    for index, factura in enumerate(facturas):
        if factura.id == id:
            facturas[index] = factura_actualizada

            return {
                "mensaje": "Factura actualizada",
                "factura": factura_actualizada
            }

    return {"mensaje": "Factura no encontrada"}

@app.delete("/facturas/{id}")
def eliminar_factura(id: int):

    for index, factura in enumerate(facturas):
        if factura.id == id:
            eliminada = facturas.pop(index)

            return {
                "mensaje": "Factura eliminada",
                "factura": eliminada
            }

    return {"mensaje": "Factura no encontrada"}

# =====================
# TRANSACCIONES
# =====================

@app.get("/transacciones")
def obtener_transacciones():
    return transacciones

@app.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):
    transacciones.append(transaccion)

    return {
        "mensaje": "Transacción agregada",
        "transaccion": transaccion
    }

@app.put("/transacciones/{id}")
def actualizar_transaccion(id: int, transaccion_actualizada: Transaccion):

    for index, transaccion in enumerate(transacciones):
        if transaccion.id == id:
            transacciones[index] = transaccion_actualizada

            return {
                "mensaje": "Transacción actualizada",
                "transaccion": transaccion_actualizada
            }

    return {"mensaje": "Transacción no encontrada"}

@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):

    for index, transaccion in enumerate(transacciones):
        if transaccion.id == id:
            eliminada = transacciones.pop(index)

            return {
                "mensaje": "Transacción eliminada",
                "transaccion": eliminada
            }

    return {"mensaje": "Transacción no encontrada"}