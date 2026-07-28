# fecha de creacion: 2026-07-28
# ultima modificacion: 2026-07-28
# descripcion: calcula el tiempo total de envenenamiento de ashe sumando lapsos minimos entre ataques consecutivos
# autor: carlos


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # caso limite: si la lista esta vacia o la duracion es cero, el tiempo total es cero
        if not timeSeries or duration == 0:
            return 0

        # acumulador para sumar el tiempo total envenenado
        total_time = 0

        # iterar hasta el penultimo elemento comparando el tiempo entre ataques
        for i in range(len(timeSeries) - 1):
            # la duracion efectiva del ataque actual es el minimo entre duration y la diferencia con el siguiente ataque
            total_time += min(duration, timeSeries[i + 1] - timeSeries[i])

        # el ultimo ataque siempre aplica la duracion completa porque no hay mas ataques despues
        return total_time + duration
