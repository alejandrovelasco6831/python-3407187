from fastapi import FastAPI

from enrutadores.clientes import router as clientes_router
from enrutadores.facturas import router as facturas_router
from enrutadores.transacciones import router as transacciones_router

app = FastAPI()

app.include_router(clientes_router)
app.include_router(facturas_router)
app.include_router(transacciones_router)

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}