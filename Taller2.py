# -*- coding: utf-8 -*-
"""
Taller de Laboratorio: Motor de Fraude Bancario
Sesion 2 - Motor de Inferencia y Modus Ponens
"""

# 1. Base de Conocimientos Estructurada
hechos = {
    "monto": 6000,
    "pais_extranjero": True
}

reglas = [
    {"id": "R1",
     "descripcion": "Si el monto supera 5000, es una transaccion inusual",
     "condiciones": {},  # se evalua aparte porque es un > y no una igualdad
     "conclusion": {"transaccion_inusual": True}},

    {"id": "R2",
     "descripcion": "Si es inusual y viene de pais extranjero, se bloquea la tarjeta",
     "condiciones": {"transaccion_inusual": True, "pais_extranjero": True},
     "conclusion": {"bloquear_tarjeta": True}},

    {"id": "R3",
     "descripcion": "Si se bloquea la tarjeta, se notifica al cliente",
     "condiciones": {"bloquear_tarjeta": True},
     "conclusion": {"notificar_cliente": True}},

    {"id": "R4",
     "descripcion": "Si es inusual pero NO es de pais extranjero, va a revision manual",
     "condiciones": {"transaccion_inusual": True, "pais_extranjero": False},
     "conclusion": {"revision_manual": True}},
]

# 2. Motor de Inferencia Forward Chaining
nuevos_hechos = True
while nuevos_hechos:
    nuevos_hechos = False
    for regla in reglas:

        # R1 es especial: usa una comparacion (monto > 5000), no una igualdad
        if regla["id"] == "R1":
            condiciones_cumplidas = hechos.get("monto", 0) > 5000
        else:
            condiciones_cumplidas = all(
                hechos.get(k) == v for k, v in regla["condiciones"].items()
            )

        if condiciones_cumplidas:
            for clave, valor in regla["conclusion"].items():
                if clave not in hechos:
                    hechos[clave] = valor
                    nuevos_hechos = True
                    print(f"[{regla['id']}] {regla['descripcion']}")
                    print(f"     -> Nuevo hecho: {clave} = {valor}\n")

# 3. Resultado final
print("=" * 50)
print("Memoria final de hechos:", hechos)