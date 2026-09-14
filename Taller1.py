# 1. MEMORIA DE TRABAJO (Base de Hechos)
servidor_estado = {
    "cpu_uso": 95,
    "memoria_libre": 10,
    "ping_respuesta": 200,
    "temperatura": 85,
    "ventilador": "encendido"
}

# 2. MOTOR DE INFERENCIA (Base de Reglas)
def diagnosticar_servidor(hechos):
    # Regla 1: Estado CRÍTICO
    if hechos["temperatura"] > 80 and hechos["ventilador"] == "apagado":
        return "CRÍTICO: Riesgo de daño físico por sobrecalentamiento."

    # Regla 2: Estado de ADVERTENCIA
    elif hechos["cpu_uso"] > 90 or hechos["memoria_libre"] < 15:
        return "ADVERTENCIA: Servidor con carga alta, monitorear de cerca."

    # Regla 3: Estado NORMAL
    elif hechos["ping_respuesta"] < 100:
        return "NORMAL: Servidor operando correctamente."

    # Regla por defecto (Fallback)
    else:
        return "REVISIÓN MANUAL: No cumple ningún criterio automático."

# 3. EJECUCIÓN
diagnostico = diagnosticar_servidor(servidor_estado)
print("Diagnóstico:", diagnostico)