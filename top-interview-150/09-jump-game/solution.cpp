#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        // Algoritmo Greedy - Empezar desde el final
        // Tiempo: O(n)
        // Espacio: O(1)

        int n = nums.size(); //obtiene el tamanio del vector
        int meta = n - 1; //ultima posicion del vector menos 1

        for (int i = n - 1; i >= 0; --i) {
            int saltoMaximo = nums[i];
            if (i + saltoMaximo >= meta) {
                meta = i;
            }
        }

        return meta == 0;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 3, 1, 1, 4}; // Ejemplo de entrada
    bool resultado = sol.canJump(nums);

    cout << (resultado ? "Se puede alcanzar el último índice" : "No se puede alcanzar el último índice") << endl;

    return 0;
}

