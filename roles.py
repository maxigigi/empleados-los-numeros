"""Definición de roles y jerarquía laboral según tipo de negocio."""

from typing import List, Dict


class Rol:
    """Define un rol laboral con sus características."""
    
    def __init__(self, nombre: str, nivel: int, descripcion: str, 
                 responsabilidades: List[str], salario_base: float):
        """
        nivel: 1 = bajo escalón, 2 = autoridad media, 3 = autoridad mayor
        """
        self.nombre = nombre
        self.nivel = nivel
        self.descripcion = descripcion
        self.responsabilidades = responsabilidades
        self.salario_base = salario_base
    
    def __str__(self):
        return self.nombre
    
    def obtener_nivel_texto(self):
        niveles = {1: "Bajo escalón", 2: "Autoridad media", 3: "Autoridad mayor"}
        return niveles.get(self.nivel, "Desconocido")


class EstructuraRoles:
    """Define la estructura de roles según tipo de negocio."""
    
    ROLES_FERRETERIA = {
        "gerente": Rol(
            nombre="Gerente",
            nivel=3,
            descripcion="Autoridad máxima del local",
            responsabilidades=[
                "Tomar decisiones importantes",
                "Manejar caja",
                "Contratar/despedir",
                "Supervisar a todos"
            ],
            salario_base=300
        ),
        "supervisor": Rol(
            nombre="Supervisor",
            nivel=2,
            descripcion="Autoridad media, supervisa operarios",
            responsabilidades=[
                "Supervisar operarios",
                "Controlar inventario",
                "Manejar caja",
                "Reportar al gerente"
            ],
            salario_base=200
        ),
        "vendedor": Rol(
            nombre="Vendedor",
            nivel=1,
            descripcion="Atiende clientes y vende",
            responsabilidades=[
                "Atender clientes",
                "Vender productos",
                "Mantener orden en mostrador",
                "Seguir instrucciones"
            ],
            salario_base=120
        ),
        "operario": Rol(
            nombre="Operario",
            nivel=1,
            descripcion="Maneja depósito y logística",
            responsabilidades=[
                "Cargar/descargar productos",
                "Ordenar depósito",
                "Inventario",
                "Entregas"
            ],
            salario_base=110
        ),
        "variado": Rol(
            nombre="Variado",
            nivel=1,
            descripcion="Ayudante con varias tareas",
            responsabilidades=[
                "Limpiar",
                "Abastecer mostrador",
                "Atender clientes",
                "Lo que se necesite"
            ],
            salario_base=90
        )
    }
    
    ROLES_ESTACION = {
        "gerente": Rol(
            nombre="Gerente",
            nivel=3,
            descripcion="Autoridad máxima",
            responsabilidades=["Decisiones", "Caja", "Supervisar"],
            salario_base=350
        ),
        "encargado_turno": Rol(
            nombre="Encargado de Turno",
            nivel=2,
            descripcion="Responsable del turno",
            responsabilidades=["Supervisar surtidores", "Control de caja", "Reportes"],
            salario_base=220
        ),
        "operario_surtidor": Rol(
            nombre="Operario Surtidor",
            nivel=1,
            descripcion="Atiende surtidores",
            responsabilidades=["Cargar combustible", "Limpiar", "Cobrar"],
            salario_base=130
        ),
        "variado": Rol(
            nombre="Variado",
            nivel=1,
            descripcion="Ayudante general",
            responsabilidades=["Limpiar", "Ayudar", "Lo que se necesite"],
            salario_base=100
        )
    }
    
    ROLES_COMIDA_RAPIDA = {
        "gerente": Rol(
            nombre="Gerente",
            nivel=3,
            descripcion="Autoridad del local",
            responsabilidades=["Decisiones", "Caja", "Calidad"],
            salario_base=280
        ),
        "cocinero_jefe": Rol(
            nombre="Cocinero Jefe",
            nivel=2,
            descripcion="Lidera la cocina",
            responsabilidades=["Cocinar", "Supervisar cocina", "Calidad comida"],
            salario_base=200
        ),
        "cajero": Rol(
            nombre="Cajero",
            nivel=1,
            descripcion="Atiende caja",
            responsabilidades=["Cobrar", "Tomar pedidos", "Caja limpia"],
            salario_base=110
        ),
        "cocinero": Rol(
            nombre="Cocinero",
            nivel=1,
            descripcion="Prepara comida",
            responsabilidades=["Cocinar", "Seguir recetas", "Limpiar cocina"],
            salario_base=115
        ),
        "variado": Rol(
            nombre="Variado",
            nivel=1,
            descripcion="Ayudante multitarea",
            responsabilidades=["Limpiar", "Ayudar cocina", "Ayudar caja"],
            salario_base=100
        )
    }
    
    ROLES_SUPERMERCADO = {
        "gerente": Rol(
            nombre="Gerente",
            nivel=3,
            descripcion="Autoridad del supermercado",
            responsabilidades=["Decisiones", "Finanzas", "Personal"],
            salario_base=400
        ),
        "supervisor_piso": Rol(
            nombre="Supervisor de Piso",
            nivel=2,
            descripcion="Supervisa reponedores",
            responsabilidades=["Supervisar piso", "Inventario", "Calidad"],
            salario_base=250
        ),
        "cajero": Rol(
            nombre="Cajero",
            nivel=1,
            descripcion="Atiende caja",
            responsabilidades=["Cobrar", "Cambio", "Atender"],
            salario_base=110
        ),
        "reponedor": Rol(
            nombre="Reponedor",
            nivel=1,
            descripcion="Repone estanterías",
            responsabilidades=["Reponer", "Ordenar", "Inventario"],
            salario_base=105
        ),
        "variado": Rol(
            nombre="Variado",
            nivel=1,
            descripcion="Ayudante general",
            responsabilidades=["Limpiar", "Ayudar", "Lo que se necesite"],
            salario_base=95
        )
    }
    
    CONFIGURACIONES = {
        "ferretera_sanitarios": ROLES_FERRETERIA,
        "estacion_de_servicio": ROLES_ESTACION,
        "comida_rapida": ROLES_COMIDA_RAPIDA,
        "supermercado": ROLES_SUPERMERCADO,
    }
    
    @staticmethod
    def obtener_roles(tipo_negocio: str) -> Dict[str, Rol]:
        """Obtiene los roles disponibles para un tipo de negocio."""
        tipo_key = tipo_negocio.lower().replace(" ", "_")
        return EstructuraRoles.CONFIGURACIONES.get(tipo_key, EstructuraRoles.ROLES_FERRETERIA)
    
    @staticmethod
    def obtener_lista_roles(tipo_negocio: str) -> List[str]:
        """Obtiene lista de nombres de roles disponibles."""
        roles = EstructuraRoles.obtener_roles(tipo_negocio)
        return list(roles.keys())
    
    @staticmethod
    def generar_estructura_inicial(tipo_negocio: str, cantidad: int) -> List[Rol]:
        """
        Genera una estructura de roles inicial según cantidad de empleados:
        
        1: variado
        2: gerente + variado
        3+: gerente + supervisor/autoridad media + variados/bajo escalón
        """
        roles_disponibles = EstructuraRoles.obtener_roles(tipo_negocio)
        estructura = []
        
        if cantidad == 1:
            estructura.append(roles_disponibles["variado"])
        elif cantidad == 2:
            estructura.append(roles_disponibles["gerente"])
            estructura.append(roles_disponibles["variado"])
        else:  # 3 o más
            estructura.append(roles_disponibles["gerente"])
            
            # Agregar autoridad media si existe
            if "supervisor" in roles_disponibles:
                estructura.append(roles_disponibles["supervisor"])
            elif "encargado_turno" in roles_disponibles:
                estructura.append(roles_disponibles["encargado_turno"])
            elif "cocinero_jefe" in roles_disponibles:
                estructura.append(roles_disponibles["cocinero_jefe"])
            elif "supervisor_piso" in roles_disponibles:
                estructura.append(roles_disponibles["supervisor_piso"])
            
            # Llenar el resto con otros roles
            for _ in range(cantidad - len(estructura)):
                # Alternar entre diferentes roles
                if "vendedor" in roles_disponibles:
                    estructura.append(roles_disponibles["vendedor"])
                elif "operario_surtidor" in roles_disponibles:
                    estructura.append(roles_disponibles["operario_surtidor"])
                elif "cocinero" in roles_disponibles:
                    estructura.append(roles_disponibles["cocinero"])
                elif "reponedor" in roles_disponibles:
                    estructura.append(roles_disponibles["reponedor"])
                else:
                    estructura.append(roles_disponibles["variado"])
        
        return estructura
