"""Base de datos de características por número numerológico."""

NUMEROS_CARACTERISTICAS = {
    1: {
        'nombre': 'El Líder',
        'descripcion': 'Ambicioso, independiente, pionero',
        'fortalezas': ['liderazgo', 'determinación', 'innovación'],
        'debilidades': ['arrogancia', 'impulsividad', 'competencia excesiva'],
        'tendencia_trabajo': 'Prefiere roles de liderazgo y responsabilidad',
        'nivel_energia': 9,
        'compatibilidad': [3, 5, 7, 9],
        'personalidad': 'Dominante, seguro de sí mismo',
        'comportamiento': 'Tomador de decisiones rápidas',
        'riesgo_conflicto': 'Bajo (pero puede ser autoritario)',
    },
    2: {
        'nombre': 'El Mediador',
        'descripcion': 'Cooperativo, sensible, diplomático',
        'fortalezas': ['empatía', 'cooperación', 'paciencia'],
        'debilidades': ['indecisión', 'sensibilidad extrema', 'pasividad'],
        'tendencia_trabajo': 'Sobresale en trabajos en equipo y relaciones',
        'nivel_energia': 5,
        'compatibilidad': [2, 4, 6, 8],
        'personalidad': 'Conciliador, sensible',
        'comportamiento': 'Busca armonía y balance',
        'riesgo_conflicto': 'Medio (evita confrontaciones)',
    },
    3: {
        'nombre': 'El Creativo',
        'descripcion': 'Expresivo, optimista, comunicativo',
        'fortalezas': ['creatividad', 'comunicación', 'optimismo'],
        'debilidades': ['dispersión', 'superficialidad', 'falta de disciplina'],
        'tendencia_trabajo': 'Ideal para roles de marketing, ventas, comunicación',
        'nivel_energia': 8,
        'compatibilidad': [1, 3, 5, 6, 9],
        'personalidad': 'Alegre, sociable, expresivo',
        'comportamiento': 'Disfruta de interacción social',
        'riesgo_conflicto': 'Bajo (pero puede ser impulsivo)',
    },
    4: {
        'nombre': 'El Constructo',
        'descripcion': 'Estable, confiable, metódico',
        'fortalezas': ['organización', 'fiabilidad', 'practicidad'],
        'debilidades': ['rigidez', 'falta de flexibilidad', 'lentitud'],
        'tendencia_trabajo': 'Excelente para gestión, operaciones, administración',
        'nivel_energia': 6,
        'compatibilidad': [2, 4, 6, 8],
        'personalidad': 'Serio, responsable, dedicado',
        'comportamiento': 'Sigue protocolos y reglas',
        'riesgo_conflicto': 'Bajo (pero puede ser obstinado)',
    },
    5: {
        'nombre': 'El Aventurero',
        'descripcion': 'Dinámico, curioso, versátil',
        'fortalezas': ['adaptabilidad', 'versatilidad', 'dinamismo'],
        'debilidades': ['inestabilidad', 'impulsividad', 'inconsistencia'],
        'tendencia_trabajo': 'Prefiere roles dinámicos con variedad',
        'nivel_energia': 10,
        'compatibilidad': [1, 3, 5, 7, 9],
        'personalidad': 'Inquieto, entusiasta, impulsivo',
        'comportamiento': 'Busca cambios y nuevas experiencias',
        'riesgo_conflicto': 'Alto (inquietud puede generar roces)',
    },
    6: {
        'nombre': 'El Sanador',
        'descripcion': 'Responsable, cuidadoso, armónico',
        'fortalezas': ['responsabilidad', 'cuidado', 'lealtad'],
        'debilidades': ['interferencia', 'preocupación excesiva', 'crítica'],
        'tendencia_trabajo': 'Brinda apoyo, mentoring, recursos humanos',
        'nivel_energia': 7,
        'compatibilidad': [2, 3, 4, 6, 9],
        'personalidad': 'Cuidador, protector, responsable',
        'comportamiento': 'Se preocupa por el bienestar del grupo',
        'riesgo_conflicto': 'Bajo (pero puede ser intrusivo)',
    },
    7: {
        'nombre': 'El Investigador',
        'descripcion': 'Analítico, introspectivo, espiritual',
        'fortalezas': ['análisis', 'intuición', 'investigación'],
        'debilidades': ['aislamiento', 'crítica', 'desconexión'],
        'tendencia_trabajo': 'Ideal para análisis, investigación, especialización',
        'nivel_energia': 5,
        'compatibilidad': [1, 5, 7, 9],
        'personalidad': 'Reflexivo, misterioso, profundo',
        'comportamiento': 'Prefiere observar y analizar antes de actuar',
        'riesgo_conflicto': 'Medio (puede ser aislado)',
    },
    8: {
        'nombre': 'El Materialista',
        'descripcion': 'Ejecutor, ambicioso, poderoso',
        'fortalezas': ['poder', 'eficiencia', 'determinación financiera'],
        'debilidades': ['obsesión con dinero', 'arrogancia', 'insensibilidad'],
        'tendencia_trabajo': 'Gestión financiera, dirección ejecutiva, negocios',
        'nivel_energia': 9,
        'compatibilidad': [2, 4, 6, 8],
        'personalidad': 'Ejecutor, ambicioso, controlador',
        'comportamiento': 'Enfocado en resultados y poder',
        'riesgo_conflicto': 'Medio (puede ser dominante)',
    },
    9: {
        'nombre': 'El Humanitario',
        'descripcion': 'Compasivo, universal, sabio',
        'fortalezas': ['compasión', 'sabiduría', 'universalidad'],
        'debilidades': ['soñador', 'falta de límites', 'idealismo ingenuo'],
        'tendencia_trabajo': 'Relaciones públicas, desarrollo comunitario, liderazgo visionario',
        'nivel_energia': 8,
        'compatibilidad': [1, 3, 5, 6, 7, 9],
        'personalidad': 'Compasivo, idealista, visionario',
        'comportamiento': 'Piensa en beneficio del grupo',
        'riesgo_conflicto': 'Bajo (busca el bien común)',
    },
}


def obtener_caracteristicas(numero: int) -> dict:
    """Retorna las características de un número."""
    return NUMEROS_CARACTERISTICAS.get(numero, {})


def obtener_compatibilidad(numero: int) -> list:
    """Retorna números con los que es compatible."""
    return NUMEROS_CARACTERISTICAS.get(numero, {}).get('compatibilidad', [])


def obtener_nombre_numero(numero: int) -> str:
    """Retorna el nombre/arquetipo del número."""
    return NUMEROS_CARACTERISTICAS.get(numero, {}).get('nombre', 'Desconocido')
