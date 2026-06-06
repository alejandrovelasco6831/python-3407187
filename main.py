from fastapi import FastAPI
from pydantic import BaseModel
from modelos.clientes import Cliente
from modelos.facturas import Factura
from modelos.transacciones import Transaccion

app = FastAPI()

# ==========================
# RUTA PRINCIPAL
# ==========================

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}

# ==========================
# MODELOS
# ==========================








# ==========================
# LISTAS TEMPORALES
# ==========================

clientes = []
facturas = []
transacciones = []

# ==========================
# CLIENTES
# ==========================

@app.get("/clientes")
def ver_clientes():
    return clientes


@app.post("/clientes")
def agregar_cliente(cliente: Cliente):
    clientes.append(cliente)
    return {
        "mensaje": "Cliente agregado",
        "datos": cliente
    }


@app.put("/clientes/{id}")
def actualizar_cliente(id: int, cliente: Cliente):

    for i in range(len(clientes)):
        if clientes[i].id == id:
            clientes[i] = cliente

            return {
                "mensaje": "Cliente actualizado",
                "datos": cliente
            }

    return {"mensaje": "Cliente no encontrado"}


@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):

    for i in range(len(clientes)):
        if clientes[i].id == id:
            eliminado = clientes.pop(i)

            return {
                "mensaje": "Cliente eliminado",
                "datos": eliminado
            }

    return {"mensaje": "Cliente no encontrado"}

# ==========================
# FACTURAS
# ==========================

@app.get("/facturas")
def ver_facturas():
    return facturas


@app.post("/facturas")
def agregar_factura(factura: Factura):
    facturas.append(factura)
    return {
        "mensaje": "Factura agregada",
        "datos": factura
    }


@app.put("/facturas/{id}")
def actualizar_factura(id: int, factura: Factura):

    for i in range(len(facturas)):
        if facturas[i].id == id:
            facturas[i] = factura
            return {
                "mensaje": "Factura actualizada",
                "datos": factura
            }

    return {"mensaje": "Factura no encontrada"}


@app.delete("/facturas/{id}")
def eliminar_factura(id: int):

    for i in range(len(facturas)):
        if facturas[i].id == id:
            eliminada = facturas.pop(i)
            return {
                "mensaje": "Factura eliminada",
                "datos": eliminada
            }

    return {"mensaje": "Factura no encontrada"}

# ==========================
# TRANSACCIONES
# ==========================

@app.get("/transacciones")
def ver_transacciones():
    return transacciones


@app.post("/transacciones")
def agregar_transaccion(transaccion: Transaccion):

    transacciones.append(transaccion)

    return {
        "mensaje": "Transacción agregada",
        "datos": transaccion
    }


@app.put("/transacciones/{id}")
def actualizar_transaccion(id: int, transaccion: Transaccion):

    for i in range(len(transacciones)):
        if transacciones[i].id == id:
            transacciones[i] = transaccion

            return {
                "mensaje": "Transacción actualizada",
                "datos": transaccion
            }

    return {"mensaje": "Transacción no encontrada"}


@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):

    for i in range(len(transacciones)):
        if transacciones[i].id == id:
            eliminada = transacciones.pop(i)

            return {
                "mensaje": "Transacción eliminada",
                "datos": eliminada
            }

    return {"mensaje": "Transacción no encontrada"}