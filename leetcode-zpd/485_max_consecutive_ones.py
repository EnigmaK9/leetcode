# fecha de creacion: 2026-07-28
# ultima modificacion: 2026-07-28
# descripcion: encuentra el numero maximo de unos consecutivos en un arreglo binario usando una ventana deslizante
# autor: carlos


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # inicializar el puntero izquierdo l y la variable output para el conteo maximo
        l, output = 0, 0

        # recorrer el arreglo guardando el indice r y el valor n
        for r, n in enumerate(nums):
            # modificacion insertada en la linea 10: se cambio '=' por '==' para realizar la comparacion
            if n == 0:
                # al encontrar un cero, movemos el puntero l mas alla del indice r actual
                l = r + 1
            # actualizar la variable output con la longitud de la ventana actual (r - l + 1)
            output = max(output, r - l + 1)

        # modificacion insertada en la linea 13: se desidento el return para ejecutarlo al terminar el ciclo
        return output
