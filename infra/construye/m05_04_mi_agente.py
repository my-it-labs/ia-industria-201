"""Constrúyelo tú (M05-04): tu propio agente con herramientas.

Lo construyes paso a paso: en cada PASO del lab te dan un bloque de código.
Pégalo debajo del comentario de ese paso, guarda y ejecuta desde infra/:

    docker compose --profile lab run --rm --no-deps --entrypoint python lab -W ignore /construye/m05_04_mi_agente.py
"""
import json
from datetime import datetime, timezone

import httpx

from linea.estado import leer                      # el último estado que publicó la estación

# --- Decisiones tuyas (las cambiarás en los pasos finales) -------------------
# PETICION = "¿Cómo está la estación EST-01 ahora?"
# PETICION = "¿Cuántas carcasas se han fabricado en el último minuto?"
PETICION = "¿Qué temperatura tiene la máquina?"

# --- PASO 1: la caja de herramientas (ya está hecho) -------------------------
def leer_estacion():
    """Lee la última carcasa de EST-01: pieza, temperatura, vibración y corriente. Solo lectura."""
    e = leer()
    return {"pieza": e["pieza_id"], "temperatura_c": e["temperatura_c"],
            "vibracion_mm_s": e["vibracion_mm_s"], "corriente_a": e["corriente_a"]}
def carcasas_ultimo_minuto():
    """Cuenta las carcasas guardadas en el histórico en el último minuto. Solo lectura."""
    import sqlite3
    with sqlite3.connect("file:/data/historial.sqlite?mode=ro", uri=True) as con:
        n = con.execute("SELECT COUNT(*) FROM lecturas WHERE ts >= strftime('%Y-%m-%dT%H:%M:%S', 'now', '-60 seconds')").fetchone()[0]
    return {"carcasas_ultimo_minuto": n}



HERRAMIENTAS = {"leer_estacion": leer_estacion}     # TODAS de lectura: no hay ninguna que escriba
HERRAMIENTAS["carcasas_ultimo_minuto"] = carcasas_ultimo_minuto
print("herramientas del agente:", list(HERRAMIENTAS))

# --- PASO 2: decidir qué herramienta hace falta --------------------------------
# (pega aquí el bloque del paso 2)
# PLAN = {"leer_estacion": ["cómo está", "temperatura", "estado", "vibración", "corriente"]}
PLAN = {"leer_estacion": ["cómo está", "temperatura", "estado", "vibración", "corriente"],
        "carcasas_ultimo_minuto": ["cuántas carcasas", "producción", "fabricado"]}
CAMBIOS = ["para ", "sube", "baja", "cambia", "escribe", "apaga"]

def elegir_herramienta(peticion):
    texto = peticion.lower()
    if any(palabra in texto for palabra in CAMBIOS):
        return None                                   # pedir un cambio: no hay herramienta para eso
    for herramienta, claves in PLAN.items():
        if any(clave in texto for clave in claves):
            return herramienta
    return None

herramienta = elegir_herramienta(PETICION)
print(f"petición: {PETICION}  ->  herramienta: {herramienta}")

# --- PASO 3: usar la herramienta y dejar traza ---------------------------------
# (pega aquí el bloque del paso 3)
dato = HERRAMIENTAS[herramienta]() if herramienta else None
with open("/data/mi_traza_agente.jsonl", "a") as traza:
    traza.write(json.dumps({"hora": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                            "peticion": PETICION, "herramienta": herramienta, "dato": dato}, ensure_ascii=False) + "\n")
print("dato de la herramienta:", dato)

# --- PASO 4: redactar la respuesta con el dato ---------------------------------
# (pega aquí el bloque del paso 4)
if dato is None:
    respuesta = "No puedo hacer eso: no tengo ninguna herramienta que cambie la estación. Avisa al responsable de turno."
else:
    mensajes = [{"role": "system", "content": "Redacta una frase para el supervisor. Copia los números exactamente."},
                {"role": "user", "content": f"Petición: {PETICION}\nDato de {herramienta}: {json.dumps(dato)}"}]
    r = httpx.post("http://llm:8088/v1/chat/completions", json={"messages": mensajes, "max_tokens": 60}, timeout=60)
    respuesta = r.json()["choices"][0]["message"]["content"].strip()
print("agente:", respuesta)

# --- PASO 5: comprobar que ha copiado bien el dato -----------------------------
# (pega aquí el bloque del paso 5)
if dato is not None:
    numeros = [str(v) for v in dato.values() if isinstance(v, (int, float))]   # los números que dio la herramienta
    faltan = [n for n in numeros if n not in respuesta]
    print("comprobación:", "OK, todos los números son los de la herramienta" if not faltan else f"NO: faltan o cambian {faltan}; no enseñar")