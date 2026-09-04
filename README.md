# Empleados: Los Números

Sistema de simulación y predicción empresarial basado en numerología. Gestiona empleados de una empresa de venta de materiales (caños, tubos, inodoros, tanques de agua, etc.) usando análisis de fechas de nacimiento.

## Características

- **Análisis Numerológico**: Calcula el número de vida, destino y personalidad de cada empleado
- **Simulación de Empleados**: Rasgos de personalidad, comportamientos y necesidades
- **Gestión Empresarial**: Depósitos, caja, oficinas y espacios de trabajo
- **Dinámica Social**: Relaciones interpersonales, compatibilidad entre empleados
- **Predicción y Optimización**: Sugiere mejores posiciones y detecta empleados clave
- **Jefe del Negocio**: Modo interactivo para navegar depósitos y áreas

## Estructura del Proyecto

```
emplados-los-numeros/
├── numerologia.py          # Cálculo de números de vida, destino, etc.
├── empleado.py             # Clase Empleado con rasgos y personalidad
├── empresa.py              # Gestión de la empresa y empleados
├── relaciones.py           # Sistema de relaciones interpersonales
├── ubicaciones.py          # Depósitos, oficinas y espacios
├── predictor.py            # Análisis predictivo y optimización
├── main.py                 # Interfaz principal (CLI)
└── data/
    └── numeros_db.py       # Base de datos de características por número
```

## Cómo Usar

```bash
python main.py
```

## Requisitos

- Python 3.8+
- No hay dependencias externas (usa solo librerías estándar)

---

**Versión**: 0.1.0