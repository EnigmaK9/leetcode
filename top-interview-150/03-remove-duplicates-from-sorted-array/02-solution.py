from typing import List

class Solution:
    # Esta función elimina duplicados de una lista ordenada en su lugar
    def removeDuplicates(self, nums: List[int]) -> int:
        # Verifica si la lista está vacía
        if not nums:
            return 0  # Si la lista está vacía, retorna 0

        k = 1  # Inicializa el contador de elementos únicos en 1, ya que el primer elemento siempre es único

        # Recorre la lista desde el segundo elemento hasta el final
        for i in range(1, len(nums)):
            # Compara el elemento actual (nums[i]) con el elemento anterior (nums[i - 1])
            if nums[i] != nums[i - 1]:
                # Si los elementos son diferentes, copia el elemento actual a la posición k
                nums[k] = nums[i]
                # Incrementa k para la próxima posición única
                k += 1

        # Retorna el número de elementos únicos en la lista
        return k

# Ejemplo de uso
sol = Solution()  # Crea una instancia de la clase Solution
nums = [1, 1, 2]  # Define la lista de entrada con duplicados
k = sol.removeDuplicates(nums)  # Llama a la función para eliminar duplicados
print(f'k = {k}, nums = {nums[:k]}')  # Imprime el resultado, debe ser: k = 2, nums = [1, 2]

