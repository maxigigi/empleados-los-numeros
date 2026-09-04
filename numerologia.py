"""Sistema de Numerología para análisis de fechas de nacimiento."""

from datetime import datetime
from typing import Dict, Tuple


class Numerologia:
    """Calcula números de vida, destino y personalidad basados en fecha de nacimiento."""

    @staticmethod
    def reducir_numero(numero: int) -> int:
        """Reduce un número a un dígito (1-9)."""
        while numero >= 10:
            numero = sum(int(d) for d in str(numero))
        return numero

    @staticmethod
    def numero_vida(fecha_nacimiento: str) -> int:
        """
        Calcula el Número de Vida (Life Path Number).
        Formato de entrada: 'DD/MM/YYYY'
        """
        try:
            fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            dia = fecha.day
            mes = fecha.month
            anio = fecha.year
            
            suma = dia + mes + anio
            return Numerologia.reducir_numero(suma)
        except ValueError:
            raise ValueError(f"Formato de fecha inválido: {fecha_nacimiento}. Use DD/MM/YYYY")

    @staticmethod
    def numero_destino(fecha_nacimiento: str) -> int:
        """
        Calcula el Número de Destino (basado en fecha completa reducida).
        """
        fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        dia = Numerologia.reducir_numero(fecha.day)
        mes = Numerologia.reducir_numero(fecha.month)
        anio = Numerologia.reducir_numero(fecha.year)
        
        suma = dia + mes + anio
        return Numerologia.reducir_numero(suma)

    @staticmethod
    def numero_personalidad(fecha_nacimiento: str) -> int:
        """
        Calcula el Número de Personalidad (basado en consonantes del día).
        Simplificación: usamos el día del mes.
        """
        fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        return Numerologia.reducir_numero(fecha.day)

    @staticmethod
    def analizar_fecha_completa(fecha_nacimiento: str) -> Dict[str, int]:
        """
        Retorna un análisis completo numerológico de la fecha de nacimiento.
        """
        return {
            'numero_vida': Numerologia.numero_vida(fecha_nacimiento),
            'numero_destino': Numerologia.numero_destino(fecha_nacimiento),
            'numero_personalidad': Numerologia.numero_personalidad(fecha_nacimiento),
            'dia': int(fecha_nacimiento.split('/')[0]),
            'mes': int(fecha_nacimiento.split('/')[1]),
            'anio': int(fecha_nacimiento.split('/')[2]),
        }


# Ejemplos de uso
if __name__ == "__main__":
    fecha = "15/03/1985"
    analisis = Numerologia.analizar_fecha_completa(fecha)
    print(f"Análisis de {fecha}:")
    for clave, valor in analisis.items():
        print(f"  {clave}: {valor}")
