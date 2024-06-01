#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;

        int min_price = prices[0];
        int max_profit = 0;

        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] < min_price) {
                min_price = prices[i];
            } else {
                int current_profit = prices[i] - min_price;
                if (current_profit > max_profit) {
                    max_profit = current_profit;
                }
            }
        }

        return max_profit;
    }
};

int main() {
    Solution solution;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    cout << "Max Profit: " << solution.maxProfit(prices) << endl;
    return 0;
}

