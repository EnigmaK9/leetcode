"""
Este código define una clase llamada Solution con un método llamado removeDuplicates.
El método removeDuplicates elimina los duplicados en una lista ordenada de números
de tal manera que cada elemento aparezca como máximo dos veces. La lista se modifica
in situ y el método devuelve la nueva longitud de la lista.

La solución utiliza dos punteros: uno lento (slow) y uno rápido (fast). La idea es
recorrer la lista con el puntero rápido y usar el puntero lento para reescribir
la lista sin los elementos duplicados adicionales.
"""

class Solution:
    def removeDuplicates(self, nums):
        # Comprobar si la lista tiene menos de 2 elementos
        # Si es así, simplemente devolver la longitud de la lista
        if len(nums) < 2:
            return len(nums)

        # Inicializar los punteros lento (slow) y rápido (fast)
        # Ambos comenzando en el índice 2 porque permitimos hasta dos duplicados
        slow, fast = 2, 2

        # Iterar sobre la lista usando el puntero rápido
        while fast < len(nums):
            # Verificar si el número en la posición fast es diferente
            # del número en la posición slow - 2
            if nums[slow - 2] != nums[fast]:
                # Si es diferente, actualizar la posición del puntero lento
                # con el valor del puntero rápido
                nums[slow] = nums[fast]
                # Mover el puntero lento hacia adelante
                slow += 1
            # Mover siempre el puntero rápido hacia adelante
            fast += 1

        # La posición del puntero lento representa la nueva longitud de la lista
        return slow

# Ejemplo de uso del método removeDuplicates
sol = Solution()
# Llamar al método con una lista de números con duplicados
print(sol.removeDuplicates([1,1,1,2,2,3]))  # Debería imprimir 5, lista modificada: [1, 1, 2, 2, 3]

