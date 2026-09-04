"""Clase Empleado con rol, fecha de nacimiento y numerología."""

from datetime import datetime
from typing import Dict, List, Tuple
from numerologia import Numerologia
from roles import Rol
import random


class Empleado:
    """Representa un empleado con rol, fecha y numerología."""

    def __init__(self, nombre: str, fecha_nacimiento: str, rol: Rol):
        """
        Args:
            nombre: Nombre del empleado
            fecha_nacimiento: En formato DD/MM/YYYY
            rol: Objeto Rol con su posición en la jerarquía
        """
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.rol = rol
        
        # Análisis numerológico (TENDENCIAS CIRCULARES CONSTANTES)
        self.numeros = Numerologia.analizar_fecha_completa(fecha_nacimiento)
        self.personalidad_diaria = self.numeros['personalidad_diaria']  # DIA
        self.tendencia_mensual = self.numeros['tendencia_mensual']      # MES
        self.karma_anual = self.numeros['karma_anual']                  # AÑO
        self.don_especial = self.numeros['don_especial']                # ÚLTIMOS 2 DÍGITOS
        self.numero_destino = self.numeros['numero_destino']            # SUMA TOTAL
        
        # Estado del empleado
        self.energia = 100
        self.animo = 75
        self.productividad = random.randint(60, 100)
        self.dinero_en_caja = 0.0
        self.ventas_totales = 0
        
        # Ubicación actual
        self.ubicacion_actual = "Mostrador"
        self.turnos_descanso = 0
        
        # Comportamiento basado en números (CONSTANTES)
        # La personalidad diaria influye en la tendencia de descanso
        self.tendencia_descanso = self.personalidad_diaria * 10  # 10-90
        self.es_rebelde = (self.numero_destino in [5, 8]) and random.random() < 0.3
        self.pide_aumento = (self.numero_destino in [8, 9]) and random.random() < 0.4
        
        # Relaciones
        self.relaciones: Dict[str, int] = {}  # {nombre_empleado: simpatía (-100 a 100)}
        
        # Registro de comportamiento
        self.comportamiento_log: List[str] = []
    
    def __str__(self) -> str:
        return f"{self.nombre} ({self.rol.nombre}) - Numero {self.numero_destino}"
    
    def __repr__(self) -> str:
        return f"Empleado({self.nombre}, {self.rol.nombre})"
    
    def obtener_info_completa(self) -> Dict:
        """Retorna información completa del empleado."""
        return {
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento,
            'rol': self.rol.nombre,
            'nivel_rol': self.rol.nivel,
            'salario_base': self.rol.salario_base,
            'personalidad_diaria': self.personalidad_diaria,
            'tendencia_mensual': self.tendencia_mensual,
            'karma_anual': self.karma_anual,
            'don_especial': self.don_especial,
            'numero_destino': self.numero_destino,
            'energia': self.energia,
            'animo': self.animo,
            'productividad': self.productividad,
            'dinero_en_caja': self.dinero_en_caja,
            'ventas_totales': self.ventas_totales,
            'ubicacion': self.ubicacion_actual,
            'es_rebelde': self.es_rebelde,
            'pide_aumento': self.pide_aumento,
        }
    
    def trabajar(self, horas: int = 8) -> Tuple[float, int]:
        """
        El empleado trabaja. Retorna (venta_realizada, energia_gastada).
        """
        if self.energia < 20:
            self.comportamiento_log.append(f"{self.nombre} está muy cansado")
            return 0, 0
        
        # Energía base según personalidad diaria
        energia_gastada = horas * (self.tendencia_descanso / 2)
        
        # Venta según productividad, energía y rol
        venta_base = self.productividad * horas * self.rol.salario_base * 0.5
        
        # Modificadores por estado
        if self.animo > 80:
            venta_base *= 1.3
        elif self.animo < 40:
            venta_base *= 0.7
        
        # Rebeldes a veces no trabajan bien
        if self.es_rebelde and random.random() < 0.15:
            venta_base *= 0.5
        
        self.energia -= energia_gastada
        self.energia = max(0, self.energia)
        self.dinero_en_caja += venta_base
        self.ventas_totales += venta_base
        
        return venta_base, energia_gastada
    
    def descansar(self, horas: int = 8) -> int:
        """
        El empleado descansa. Retorna energía recuperada.
        """
        recuperacion = horas * 15
        self.energia = min(100, self.energia + recuperacion)
        self.animo = min(100, self.animo + horas * 5)
        self.turnos_descanso += 1
        
        return recuperacion
    
    def evaluar_compatibilidad(self, otro_empleado: 'Empleado') -> Tuple[int, str]:
        """
        Evalúa compatibilidad con otro empleado basada en números.
        Retorna (puntuación -100 a 100, descripción).
        """
        score = 0
        razon = []
        
        # Compatibilidad por número destino
        diff_destino = abs(self.numero_destino - otro_empleado.numero_destino)
        if diff_destino == 0:
            score += 40
            razon.append("Mismo destino")
        elif diff_destino <= 1:
            score += 20
            razon.append("Destinos cercanos")
        elif diff_destino >= 4:
            score -= 30
            razon.append("Destinos muy diferentes")
        
        # Compatibilidad por nivel de rol
        diff_nivel = abs(self.rol.nivel - otro_empleado.rol.nivel)
        if diff_nivel == 0:
            score += 10  # Mismo nivel
        elif diff_nivel == 1:
            score += 5   # Nivel adyacente
        else:
            score -= 10  # Niveles muy diferentes
        
        # Añadir ruido
        score += random.randint(-20, 20)
        score = max(-100, min(100, score))
        
        if score > 50:
            tipo = "Alta compatibilidad"
        elif score > 0:
            tipo = "Compatibilidad media"
        elif score > -50:
            tipo = "Baja compatibilidad"
        else:
            tipo = "Conflicto potencial"
        
        return score, tipo
    
    def obtener_permisos(self) -> Dict[str, bool]:
        """
        Retorna qué acciones puede hacer según su rol.
        """
        permisos = {
            'supervisar': self.rol.nivel >= 2,
            'manejar_caja': self.rol.nivel >= 2 or 'cajero' in self.rol.nombre.lower(),
            'despedir': self.rol.nivel == 3,
            'contratar': self.rol.nivel == 3,
            'dar_aumento': self.rol.nivel >= 2,
            'trasladar_empleado': self.rol.nivel >= 2,
            'tomar_decisiones': self.rol.nivel >= 2,
            'atender_cliente': True,  # Todos pueden
            'trabajar': True,          # Todos pueden
        }
        return permisos
    
    def mostrar_numerologia(self) -> str:
        """
        Retorna un resumen formateado de la numerología del empleado.
        """
        texto = f"""
 NUMEROLOGIA: {self.nombre}
 
 Fecha: {self.fecha_nacimiento}
 
 PERSONALIDAD DIARIA (DIA {self.numeros['dia']}): {self.personalidad_diaria}
   {Numerologia.obtener_descripcion_numero(self.personalidad_diaria, 'personalidad')}
 
 TENDENCIA MENSUAL (MES {self.numeros['mes']}): {self.tendencia_mensual}
   {Numerologia.obtener_descripcion_numero(self.tendencia_mensual, 'tendencia')}
 
 KARMA ANUAL (AÑO {self.numeros['anio']}): {self.karma_anual}
   {Numerologia.obtener_descripcion_numero(self.karma_anual, 'karma')}
 
 DON ESPECIAL (ULTIMOS 2 DIGITOS): {self.don_especial}
   {Numerologia.obtener_descripcion_numero(self.don_especial, 'don')}
 
 NUMERO DESTINO (SUMA TOTAL): {self.numero_destino}
   {Numerologia.obtener_descripcion_numero(self.numero_destino, 'destino')}
        """
        return texto
