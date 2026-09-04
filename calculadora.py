"""Calculadora Numerológica Simple - Desglose completo paso a paso."""

import os
from datetime import datetime


class CalculadoraNumerologia:
    """Calcula números numerológicos con desglose visual."""
    
    @staticmethod
    def limpiar():
        os.system('clear' if os.name != 'nt' else 'cls')
    
    @staticmethod
    def linea(caracter="=", largo=70):
        return caracter * largo
    
    @staticmethod
    def titulo(texto):
        print(f"\n{CalculadoraNumerologia.linea()}")
        print(f" {texto}")
        print(f"{CalculadoraNumerologia.linea()}\n")
    
    @staticmethod
    def reducir(numero: int) -> int:
        """Reduce un número a dígito único (1-9)."""
        while numero >= 10:
            numero = sum(int(d) for d in str(numero))
        return numero
    
    @staticmethod
    def desglose_suma(numero: int) -> str:
        """Muestra el desglose de la suma de dígitos."""
        if numero < 10:
            return str(numero)
        
        digitos = [int(d) for d in str(numero)]
        suma = " + ".join(str(d) for d in digitos)
        resultado = sum(digitos)
        
        return f"{suma} = {resultado}"
    
    @staticmethod
    def calcular_fecha(fecha_str: str) -> dict:
        """
        Calcula todos los números a partir de una fecha.
        Formato: DD/MM/YYYY
        
        Retorna:
        - DÍA (dágitos del día)
        - MES (dágitos del mes)
        - AÑO COMPLETO (suma de todos los dígitos del año)
        - DON ESPECIAL (suma de últimos 2 dígitos del año)
        - PERSONALIDAD DIARIA (día reducido)
        - TENDENCIA MENSUAL (mes reducido)
        - KARMA ANUAL (año reducido)
        - DON (don reducido)
        - NUMERO DESTINO (suma total de todos los dígitos)
        """
        try:
            fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
        except ValueError:
            return None
        
        dia = fecha_obj.day
        mes = fecha_obj.month
        anio = fecha_obj.year
        
        # ===== CALCULOS =====
        
        # PASO 1: DÍA
        dia_digitos = [int(d) for d in str(dia)]
        dia_suma = sum(dia_digitos)
        personalidad_diaria = CalculadoraNumerologia.reducir(dia_suma)
        
        # PASO 2: MES
        mes_digitos = [int(d) for d in str(mes)]
        mes_suma = sum(mes_digitos)
        tendencia_mensual = CalculadoraNumerologia.reducir(mes_suma)
        
        # PASO 3: AÑO
        anio_digitos = [int(d) for d in str(anio)]
        anio_suma = sum(anio_digitos)
        karma_anual = CalculadoraNumerologia.reducir(anio_suma)
        
        # PASO 4: DON ESPECIAL (ultimos 2 dígitos del año)
        ultimos_dos = anio % 100
        don_digitos = [int(d) for d in str(ultimos_dos)]
        don_suma = sum(don_digitos)
        don_especial = CalculadoraNumerologia.reducir(don_suma)
        
        # PASO 5: NUMERO DESTINO (suma total)
        total_digitos = dia_digitos + mes_digitos + anio_digitos
        total_suma = sum(total_digitos)
        numero_destino = CalculadoraNumerologia.reducir(total_suma)
        
        return {
            'fecha': fecha_str,
            'dia': dia,
            'mes': mes,
            'anio': anio,
            'dia_digitos': dia_digitos,
            'mes_digitos': mes_digitos,
            'anio_digitos': anio_digitos,
            'ultimos_dos': ultimos_dos,
            'don_digitos': don_digitos,
            'dia_suma': dia_suma,
            'mes_suma': mes_suma,
            'anio_suma': anio_suma,
            'don_suma': don_suma,
            'total_suma': total_suma,
            'personalidad_diaria': personalidad_diaria,
            'tendencia_mensual': tendencia_mensual,
            'karma_anual': karma_anual,
            'don_especial': don_especial,
            'numero_destino': numero_destino,
        }
    
    @staticmethod
    def mostrar_calculo(resultado: dict) -> str:
        """Muestra el cálculo de forma clara y visual."""
        if not resultado:
            return "Fecha inválida. Usa formato DD/MM/YYYY"
        
        texto = []
        texto.append(f"\nFECHA: {resultado['fecha']}")
        texto.append(f"DÍA: {resultado['dia']} | MES: {resultado['mes']} | AÑO: {resultado['anio']}\n")
        
        # DÍA
        texto.append(f"{CalculadoraNumerologia.linea('-')}")
        texto.append(" PERSONALIDAD DIARIA (DÍA)\n")
        dia_digitos_str = " + ".join(str(d) for d in resultado['dia_digitos'])
        texto.append(f" DÍgitos del día {resultado['dia']}: {dia_digitos_str} = {resultado['dia_suma']}")
        if resultado['dia_suma'] >= 10:
            texto.append(f" Reducir: {CalculadoraNumerologia.desglose_suma(resultado['dia_suma'])}")
        texto.append(f" >> PERSONALIDAD DIARIA: {resultado['personalidad_diaria']} <<\n")
        
        # MES
        texto.append(f"{CalculadoraNumerologia.linea('-')}")
        texto.append(" TENDENCIA MENSUAL (MES)\n")
        mes_digitos_str = " + ".join(str(d) for d in resultado['mes_digitos'])
        texto.append(f" Dígitos del mes {resultado['mes']}: {mes_digitos_str} = {resultado['mes_suma']}")
        if resultado['mes_suma'] >= 10:
            texto.append(f" Reducir: {CalculadoraNumerologia.desglose_suma(resultado['mes_suma'])}")
        texto.append(f" >> TENDENCIA MENSUAL: {resultado['tendencia_mensual']} <<\n")
        
        # AÑO
        texto.append(f"{CalculadoraNumerologia.linea('-')}")
        texto.append(" KARMA ANUAL (AÑO)\n")
        anio_digitos_str = " + ".join(str(d) for d in resultado['anio_digitos'])
        texto.append(f" Dígitos del año {resultado['anio']}: {anio_digitos_str} = {resultado['anio_suma']}")
        if resultado['anio_suma'] >= 10:
            texto.append(f" Reducir: {CalculadoraNumerologia.desglose_suma(resultado['anio_suma'])}")
        texto.append(f" >> KARMA ANUAL: {resultado['karma_anual']} <<\n")
        
        # DON ESPECIAL
        texto.append(f"{CalculadoraNumerologia.linea('-')}")
        texto.append(" DON ESPECIAL (ÚLTIMOS 2 DÍGITOS DEL AÑO)\n")
        don_digitos_str = " + ".join(str(d) for d in resultado['don_digitos'])
        texto.append(f" ÚLTIMOS 2 DÍGITOS: {resultado['ultimos_dos']} ({don_digitos_str}) = {resultado['don_suma']}")
        if resultado['don_suma'] >= 10:
            texto.append(f" Reducir: {CalculadoraNumerologia.desglose_suma(resultado['don_suma'])}")
        texto.append(f" >> DON ESPECIAL: {resultado['don_especial']} <<\n")
        
        # NÚMMERO DESTINO
        texto.append(f"{CalculadoraNumerologia.linea('=')}")
        texto.append(" NUMERO DESTINO (SUMA TOTAL DE TODOS LOS DIGITOS)\n")
        
        # Mostrar todos los dígitos
        todos_digitos = resultado['dia_digitos'] + resultado['mes_digitos'] + resultado['anio_digitos']
        digitos_str = " + ".join(str(d) for d in todos_digitos)
        texto.append(f" {resultado['dia']} + {resultado['mes']} + {resultado['anio']}")
        texto.append(f" = {digitos_str}")
        texto.append(f" = {resultado['total_suma']}")
        
        if resultado['total_suma'] >= 10:
            texto.append(f" Reducir: {CalculadoraNumerologia.desglose_suma(resultado['total_suma'])}")
        
        texto.append(f"\n >> NUMERO DESTINO FINAL: {resultado['numero_destino']} <<\n")
        
        # RESUMEN
        texto.append(f"{CalculadoraNumerologia.linea('=')}")
        texto.append(" RESUMEN\n")
        texto.append(f" Personalidad Diaria (Día):    {resultado['personalidad_diaria']}")
        texto.append(f" Tendencia Mensual (Mes):      {resultado['tendencia_mensual']}")
        texto.append(f" Karma Anual (Año):           {resultado['karma_anual']}")
        texto.append(f" Don Especial (Últimos 2):    {resultado['don_especial']}")
        texto.append(f" NUMERO DESTINO (Total):       {resultado['numero_destino']}\n")
        
        return "\n".join(texto)


def main():
    """Función principal."""
    while True:
        CalculadoraNumerologia.limpiar()
        CalculadoraNumerologia.titulo("CALCULADORA NUMEROLOGICA")
        
        print(" 1. Calcular fecha")
        print(" 2. Salir\n")
        
        try:
            opcion = int(input(" Elige: "))
            
            if opcion == 1:
                CalculadoraNumerologia.limpiar()
                CalculadoraNumerologia.titulo("INGRESA UNA FECHA")
                
                fecha = input(" Formato DD/MM/YYYY: ").strip()
                
                resultado = CalculadoraNumerologia.calcular_fecha(fecha)
                
                CalculadoraNumerologia.limpiar()
                print(CalculadoraNumerologia.mostrar_calculo(resultado))
                
                input(" [Enter para continuar]")
            
            elif opcion == 2:
                print("\n¡Hasta luego!\n")
                break
        
        except (ValueError, KeyError):
            pass


if __name__ == "__main__":
    main()
