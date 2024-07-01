class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Check if the prices list is empty. If it is, return 0 as there are no transactions to make.
        # Verifica si la lista de precios está vacía. Si lo está, devuelve 0 ya que no hay transacciones para hacer.
        if not prices:
            return 0

        # Initialize total profit to 0. This variable will store the cumulative profit from all transactions.
        # Inicializa el beneficio total a 0. Esta variable almacenará el beneficio acumulado de todas las transacciones.
        total_profit = 0

        # Iterate over the prices list starting from the second element.
        # Itera sobre la lista de precios comenzando desde el segundo elemento.
        for index in range(1, len(prices)):
            # If the current price is higher than the previous day's price, calculate the profit.
            # Si el precio actual es mayor que el precio del día anterior, calcula el beneficio.
            if prices[index] > prices[index - 1]:
                # Add the difference (current price - previous price) to the total profit.
                # Añade la diferencia (precio actual - precio anterior) al beneficio total.
                total_profit += prices[index] - prices[index - 1]

        # Return the total profit after iterating through the prices list.
        # Devuelve el beneficio total después de iterar a través de la lista de precios.
        return total_profit

# Test cases to validate the solution
# Casos de prueba para validar la solución

prices1 = [7, 1, 5, 3, 6, 4]
# Expected output: 7
# Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 3.
# Total profit = 4 + 3 = 7.
# Salida esperada: 7
# Compra en el día 2 (precio = 1) y vende en el día 3 (precio = 5), beneficio = 4.
# Luego compra en el día 4 (precio = 3) y vende en el día 5 (precio = 6), beneficio = 3.
# Beneficio total = 4 + 3 = 7.

prices2 = [1, 2, 3, 4, 5]
# Expected output: 4
# Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 4.
# Salida esperada: 4
# Compra en el día 1 (precio = 1) y vende en el día 5 (precio = 5), beneficio = 4.

prices3 = [7, 6, 4, 3, 1]
# Expected output: 0
# No transactions can be made to achieve a positive profit.
# Salida esperada: 0
# No se pueden realizar transacciones para obtener un beneficio positivo.

# Create an instance of the Solution class
# Crea una instancia de la clase Solution
sol = Solution()

# Print the results for the test cases
# Imprime los resultados para los casos de prueba
print(sol.maxProfit(prices1))  # Output: 7
print(sol.maxProfit(prices2))  # Output: 4
print(sol.maxProfit(prices3))  # Output: 0

