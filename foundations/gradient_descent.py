class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        f_prime = lambda x : 2 * x
        x = init
        for i in range(iterations): 
            
            x = x - learning_rate * f_prime(x)

            if x == 0: 
                return 0.0

        return round(x, 5)
