import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression, make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ============================================================================
# LESSON 1: LINEAR REGRESSION FROM SCRATCH (GRADIENT DESCENT)
# ============================================================================


class LinearRegressionFromScratch:
    """
    🔥 Linear Regression using Gradient Descent

    The algorithm:
    1. Start with random weights (slope, intercept)
    2. Calculate predictions: y_pred = w*x + b
    3. Calculate error: MSE = mean((y_pred - y_true)^2)
    4. Calculate gradients (how to improve)
    5. Update weights: w = w - learning_rate * dw
    6. Repeat until convergence

    This is EXACTLY how neural networks work! 🧠
    """

    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None
        self.cost_history = []

    def fit(self, X, y):
        # Learn from training data
        n_samples, n_features = X.shape

        # Initialize weights to small random values
        self.weights = np.random.normal(0, 0.01, n_features)
        self.bias = 0

        # Gradient Descent Loop
        for iteration in range(self.iterations):
            # Step 1: Make predictions
            y_pred = np.dot(X, self.weights) + self.bias

            # Step 2: Calculate error
            mse = np.mean((y_pred - y) ** 2)
            self.cost_history.append(mse)

            # Step 3: Calculate gradients
            dw = (2 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (2 / n_samples) * np.sum(y_pred - y)

            # Step 4: Update weights
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            # Print progress every 100 iterations
            if (iteration + 1) % 100 == 0:
                print(f"Iteration {iteration + 1}: MSE = {mse:.4f}")

    def predict(self, X):
        """Make predictions on new data"""
        return np.dot(X, self.weights) + self.bias

# ============================================================================
# DEMONSTRATION & COMPARISON
# ============================================================================

print("=" * 72)
print("🔥 PHASE 3.3: ALGORITHMS FROM SCRATCH")
print("=" * 72)

# -------- REGRESSION TASK --------
print("\n🎯 LESSON 1: LINEAR REGRESSION FROM SCRATCH")
print("-" * 72)

X_reg, y_reg = make_regression(n_samples=100, n_features=1, noise=20, random_state=42)
X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

print(f"\nTraining data: {X_reg_train.shape[0]} samples")
print(f"Testing data: {X_reg_test.shape[0]} samples")

# Train our custom model
print("\n🔄 Training Linear Regression from Scratch...")
model_custom_lr = LinearRegressionFromScratch(learning_rate=0.01, iterations=500)
model_custom_lr.fit(X_reg_train, y_reg_train)

