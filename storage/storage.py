from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

class ResultInput(BaseModel):
    a: float
    b: float
    c: float
    d: float
    resultado: float

@app.post("/guardar")
def guardar_resultado(data: ResultInput):
    conn = mysql.connector.connect(
        host="mysql-service",
        user="user",
        password="password",
        database="microservicios_db"
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            a FLOAT, b FLOAT, c FLOAT, d FLOAT, resultado FLOAT
        )
    """)
    cursor.execute(
        "INSERT INTO resultados (a, b, c, d, resultado) VALUES (%s, %s, %s, %s, %s)",
        (data.a, data.b, data.c, data.d, data.resultado)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Resultado guardado exitosamente"}

@app.get("/resultados")
def obtener_resultados():
    conn = mysql.connector.connect(
        host="mysql-service",
        user="user",
        password="password",
        database="microservicios_db"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM resultados")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados
