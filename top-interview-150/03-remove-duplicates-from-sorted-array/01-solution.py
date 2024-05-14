from typing import List

class Solution:
    # Esta función elimina duplicados de una lista ordenada en su lugar
    def removeDuplicates(self, nums: List[int]) -> int:
        # Inicializa el índice para la próxima posición única en la lista
        j = 1

        # Recorre la lista desde el segundo elemento hasta el final
        for i in range(1, len(nums)):
            # Si el elemento actual es diferente del elemento anterior
            if nums[i] != nums[i - 1]:
                # Copia el elemento actual a la posición j
                nums[j] = nums[i]
                # Incrementa j para la próxima posición única
                j += 1

        # Retorna el número de elementos únicos en la lista
        return j

# Ejemplo de uso
sol = Solution()  # Crea una instancia de la clase Solution
nums = [1, 1, 2]  # Define la lista de entrada
k = sol.removeDuplicates(nums)  # Llama a la función para eliminar duplicados
print(f'k = {k}, nums = {nums[:k]}')  # Imprime el resultado, debe ser: k = 2, nums = [1, 2]

