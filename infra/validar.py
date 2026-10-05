#!/usr/bin/env python3
"""Recorre los laboratorios en esta máquina. Se lanza desde infra/."""
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
MODELO = RAIZ / "modelos" / "qwen2.5-0.5b-instruct-q4_k_m.gguf"
URL = (
    "https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/"
    "qwen2.5-0.5b-instruct-q4_k_m.gguf"
)


def run(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    print("+", " ".join(args), flush=True)
    resultado = subprocess.run(args, cwd=RAIZ)
    if check and resultado.returncode != 0:
        sys.exit(resultado.returncode)
    return resultado


def lab(comando: str) -> None:
    run(["docker", "compose", "--profile", "lab", "run", "--rm", "--no-deps", "lab", comando])


def esperar_http(url: str, intentos: int = 60) -> None:
    for _ in range(intentos):
        try:
            with urllib.request.urlopen(url, timeout=3) as resp:
                if resp.status < 500:
                    return
        except Exception:
            time.sleep(2)
    sys.exit(f"timeout esperando {url}")


def descargar_modelo() -> None:
    if MODELO.exists() and MODELO.stat().st_size > 10_000_000:
        print(f"= modelo ya está en {MODELO}")
        return
    MODELO.parent.mkdir(parents=True, exist_ok=True)
    print(f"+ descargando {URL}")
    urllib.request.urlretrieve(URL, MODELO)


def main() -> None:
    run(["docker", "compose", "build"])
    run(
        [
            "docker", "compose", "up", "-d", "--force-recreate",
            "mosquitto", "sensor", "archivador", "opcua", "modbus", "panel",
        ]
    )
    time.sleep(4)
    for comando in ("m01-01", "m01-02", "m02-01"):
        lab(comando)
    run(["docker", "compose", "stop", "sensor"])
    time.sleep(1)
    lab("m02-01-pausa")
    run(["docker", "compose", "start", "sensor"])
    time.sleep(2)
    for comando in ("m02-01", "m02-02", "m02-03", "m03-01", "m03-02", "m03-03", "m04-01", "m04-02", "m04-03"):
        lab(comando)
    descargar_modelo()
    run(["docker", "compose", "up", "-d", "llm"])
    esperar_http("http://127.0.0.1:8088/salud", intentos=90)
    for comando in ("m05-01", "m05-02", "m05-03", "m05-03-ausente", "m05-04"):
        lab(comando)
    for comando in ("m06-01", "m06-02"):
        lab(comando)
    run(["docker", "compose", "up", "-d", "api"])
    esperar_http("http://127.0.0.1:8000/salud")
    for comando in ("m07-01", "m07-02", "m08-01", "m08-02"):
        lab(comando)
    print("VALIDACION_COMPLETA")


if __name__ == "__main__":
    main()
