"""
Creation Date: 2026-08-17
Last Modified: 2026-08-17
Description: calcula la longitud de la subsecuencia continua creciente mas larga dentro de una lista de enteros.
Author: enigmak9
"""


class Solucion(object):
    def encontrar_longitud_lcis(self, numeros):
        """
        :type numeros: list[int]
        :rtype: int
        """
        # verificamos si la lista esta vacia para evitar procesar una lista sin elementos
        if not numeros:
            return 0

        # inicializamos las variables en uno porque una lista no vacia tiene al menos longitud uno
        # longitud_maxima guarda el record historico de la subida mas larga
        longitud_maxima = 1
        # longitud_actual cuenta cuantos pasos seguidos hacia arriba llevamos en el tramo actual
        longitud_actual = 1

        # recorremos desde el segundo elemento (indice 1) hasta el final
        # esto nos permite comparar siempre la posicion actual con la posicion anterior sin salir del rango
        for i in range(1, len(numeros)):
            # comprobamos si el numero actual es estrictamente mayor que el anterior
            if numeros[i] > numeros[i - 1]:
                # la racha continua, incrementamos el contador actual
                longitud_actual += 1
                # usamos max para actualizar el record global si la racha actual lo supera
                longitud_maxima = max(longitud_maxima, longitud_actual)
            else:
                # si el numero actual es menor o igual, la racha se rompe
                # reiniciamos el contador a 1 para empezar una nueva cuenta desde este elemento
                longitud_actual = 1

        # retornamos la mayor longitud registrada
        return longitud_maxima
