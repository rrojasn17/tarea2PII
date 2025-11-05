Tarea 2 — Sistema de Multas y Préstamos de Biblioteca

Curso: Programación II
Profesora: Ing. Lenin A. Ortega Jiménez
Estudiantes: Nicole Sánchez Gómez Y Reymond Rojas Nuñez
Fecha: 29 de octubre de 2025

1. Introducción
El proyecto Sistema de Multas y Préstamos de Biblioteca fue desarrollado en Python aplicando los principios de la programación orientada a objetos (POO), junto con los principios SOLID y la Ley de Deméter.
Su propósito es gestionar préstamos de materiales de biblioteca, calcular multas vencidas según diferentes políticas y aplicar descuentos según la categoría del usuario.

2. Estructura del sistema
Tarea 2 Biblioteca/
│
├── domain/
│   ├── modelos.py              # Usuario, Material, Prestamo, ReciboMulta
│   └── politicas.py            # Políticas FijaPorDia, Escalonada, ConTope, ConDescuento
│
├── services/
│   └── multas.py               # ServicioMultas: orquestador del flujo
│
├── ports/
│   ├── repositorios.py         # Protocol RepositorioRecibos
│   └── formateo.py             # Protocol FormateadorRecibo
│
├── adapters/
│   ├── repo_archivo.py         # Implementación del repositorio en archivo
│   └── formateador_texto.py    # Formateador de recibos en texto
│
├── ui/
│   └── cli.py                  # Interfaz de línea de comandos
│
└── utils/
    └── validacion.py           # Validaciones y conversión segura de entradas

3. Diagramas Mermaid
3.1 Diagrama de Arquitectura
3.2 Diagrama de Secuencia


