import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ============================================================================
# NEURAL NETWORK FROM SCRATCH
# ============================================================================


class NeuralNetworkFromScratch:
    """
    🧠 Neural Network using Forward Propagation and Backpropagation

    Architecture: [input_layer] → [hidden_layer] → [output_layer]

    Forward Propagation:
    1. z1 = X @ W1 + b1           (linear combination)
    2. a1 = relu(z1)              (activation function)
    3. z2 = a1 @ W2 + b2          (output linear)
    4. a2 = sigmoid(z2)           (output probability)

    Backpropagation:
    1. Calculate output error: dz2 = a2 - y
    2. Gradient for W2/b2: dW2 = a1.T @ dz2 / m
    3. Error for hidden: da1 = dz2 @ W2.T
    4. Apply ReLU gradient: dz1 = da1 * (a1 > 0)
    5. Gradient for W1/b1: dW1 = X.T @ dz1 / m
    6. Update weights: W = W - learning_rate * dW

    This is how PyTorch and TensorFlow work under the hood! 🚀
    """

    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        """Initialize network with random weights"""
        self.learning_rate = learning_rate

        # Layer 1: Input → Hidden
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))

        # Layer 2: Hidden → Output
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))

        # Store activations for backprop
        self.cache = {}
        self.loss_history = []
        
    def relu(self, z):
        """ReLU activation: max(0, z)"""
        return np.maximum(0, z)

    def relu_derivative(self, z):
        """ReLU gradient: 1 if z > 0, else 0"""
        return (z > 0).astype(float)

    def sigmoid(self, z):
        """Sigmoid activation: 1 / (1 + e^-z)"""
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))
    
    def forward(self, X):
        """
        Forward Propagation: Send data through network
        X → [Linear] → [ReLU] → [Linear] → [Sigmoid] → y_pred
        """
        # Layer 1: Input → Hidden (with ReLU)
        z1 = np.dot(X, self.W1) + self.b1
        a1 = self.relu(z1)

        # Layer 2: Hidden → Output (with Sigmoid)
        z2 = np.dot(a1, self.W2) + self.b2
        a2 = self.sigmoid(z2)

        # Store for backprop
        self.cache = {'X': X, 'z1': z1, 'a1': a1, 'z2': z2, 'a2': a2}

        return a2 
    
    def backward(self, y):
        """
        Backpropagation: Calculate gradients and update weights

        The chain rule in action:
        dL/dW = dL/da2 × da2/dz2 × dz2/dW
        """
        m = len(y)

        X = self.cache['X']
        a1 = self.cache['a1']
        a2 = self.cache['a2']
        z1 = self.cache['z1']

        # Output layer error
        dz2 = a2 - y  # (m, 1)

        # Gradients for layer 2
        dW2 = np.dot(a1.T, dz2) / m  # (hidden_size, 1)
        db2 = np.sum(dz2, axis=0, keepdims=True) / m  # (1, 1)

        # Error flowing back to hidden layer
        da1 = np.dot(dz2, self.W2.T)  # (m, hidden_size)

        # Apply ReLU gradient (dead neurons have 0 gradient)
        dz1 = da1 * self.relu_derivative(z1)  # (m, hidden_size)

        # Gradients for layer 1
        dW1 = np.dot(X.T, dz1) / m  # (input_size, hidden_size)
        db1 = np.sum(dz1, axis=0, keepdims=True) / m  # (1, hidden_size)

        # Update weights using gradient descent
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        
    def train(self, X_train, y_train, epochs=1000):
        """Train the network"""
        for epoch in range(epochs):
            # Forward pass
            y_pred = self.forward(X_train)

            # Calculate loss (binary cross-entropy)
            epsilon = 1e-7
            loss = -np.mean(y_train * np.log(y_pred + epsilon) +
                           (1 - y_train) * np.log(1 - y_pred + epsilon))
            self.loss_history.append(loss)

            # Backward pass
            self.backward(y_train)

            # Print progress
            if (epoch + 1) % 100 == 0:
                print(f"Epoch {epoch + 1}: Loss = {loss:.6f}")

    def predict(self, X):
        """Make predictions"""
        output = self.forward(X)
        return (output > 0.5).astype(int).flatten()

    def predict_proba(self, X):
        """Get probability predictions"""
        return self.forward(X).flatten()
    
    
# ============================================================================
# DEMONSTRATION
# ============================================================================

print("=" * 80)
print("🧠 PHASE 4.1: NEURAL NETWORK FROM SCRATCH")
print("=" * 80)

# Create a non-linearly separable dataset
print("\n🎯 Dataset: Non-linearly Separable (XOR-like)")
print("-" * 80)

X, y = make_moons(n_samples=200, noise=0.1, random_state=42)
X = (X - X.mean(axis=0)) / X.std(axis=0)  # Normalize
y = y.reshape(-1, 1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training data: {X_train.shape[0]} samples, {X_train.shape[1]} features")
print(f"Testing data: {X_test.shape[0]} samples")
print(f"Classes: Binary (0 or 1)")

# Create and train network
print("\n🔄 Building Neural Network from Scratch...")
print("   Architecture: [2 inputs] → [16 hidden] → [1 output]")

network = NeuralNetworkFromScratch(
    input_size=2,
    hidden_size=16,
    output_size=1,
    learning_rate=0.1
)

print("\n🧠 Training Network (1000 epochs)...")
network.train(X_train, y_train, epochs=1000)

# Evaluate
print("\n" + "=" * 80)
print("✅ TRAINING COMPLETE!")
print("=" * 80)

y_pred_train = network.predict(X_train)
y_pred_test = network.predict(X_test)

train_acc = np.mean(y_pred_train == y_train.flatten())
test_acc = np.mean(y_pred_test == y_test.flatten())

print(f"\n📊 RESULTS:")
print(f"   Train Accuracy: {train_acc:.4f} ({int(train_acc * len(y_train))} / {len(y_train)})")
print(f"   Test Accuracy:  {test_acc:.4f} ({int(test_acc * len(y_test))} / {len(y_test)})")

# ============================================================================
# VISUALIZATION
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('🧠 Phase 4.1: Neural Network from Scratch', fontsize=16, fontweight='bold')

# Plot 1: Training Data
axes[0, 0].scatter(X_train[y_train.flatten() == 0, 0], X_train[y_train.flatten() == 0, 1],
                   c='#FF6B6B', label='Class 0', s=50, alpha=0.7)
axes[0, 0].scatter(X_train[y_train.flatten() == 1, 0], X_train[y_train.flatten() == 1, 1],
                   c='#4ECDC4', label='Class 1', s=50, alpha=0.7)
axes[0, 0].set_xlabel('Feature 1', fontsize=11)
axes[0, 0].set_ylabel('Feature 2', fontsize=11)
axes[0, 0].set_title('Lesson 1: Non-Linear Dataset (Moon Pattern)', fontsize=12, fontweight='bold')
axes[0, 0].legend(fontsize=10)
axes[0, 0].grid(True, alpha=0.3)


# Plot 2: Loss Convergence
axes[0, 1].plot(network.loss_history, linewidth=2, color='#95E1D3')
axes[0, 1].set_xlabel('Epoch', fontsize=11)
axes[0, 1].set_ylabel('Loss (Binary Cross-Entropy)', fontsize=11)
axes[0, 1].set_title('Lesson 1: Training Loss Convergence', fontsize=12, fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].set_yscale('log')  # Log scale to see early improvement

# Plot 3: Decision Boundary
h = 0.02
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

Z = network.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

axes[1, 0].contourf(xx, yy, Z, levels=[0, 0.5, 1], colors=['#FFE66D', '#A8E6CF'], alpha=0.6)
axes[1, 0].scatter(X_train[y_train.flatten() == 0, 0], X_train[y_train.flatten() == 0, 1],
                   c='#FF6B6B', label='Class 0', s=50, edgecolors='black', linewidth=1)
axes[1, 0].scatter(X_train[y_train.flatten() == 1, 0], X_train[y_train.flatten() == 1, 1],
                   c='#4ECDC4', label='Class 1', s=50, edgecolors='black', linewidth=1)
axes[1, 0].set_xlabel('Feature 1', fontsize=11)
axes[1, 0].set_ylabel('Feature 2', fontsize=11)
axes[1, 0].set_title(f'Lesson 1: Decision Boundary (Train Acc = {train_acc:.4f})',
                     fontsize=12, fontweight='bold')
axes[1, 0].legend(fontsize=10)
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Accuracy Comparison
models = ['Train', 'Test']
accuracies = [train_acc, test_acc]
colors = ['#95E1D3', '#F38181']
bars = axes[1, 1].bar(models, accuracies, color=colors, edgecolor='black', linewidth=2)
axes[1, 1].set_ylabel('Accuracy', fontsize=11)
axes[1, 1].set_title('Lesson 1: Neural Network Accuracy', fontsize=12, fontweight='bold')
axes[1, 1].set_ylim([0, 1])
axes[1, 1].grid(True, alpha=0.3, axis='y')
for bar, acc in zip(bars, accuracies):
    height = bar.get_height()
    axes[1, 1].text(bar.get_x() + bar.get_width()/2., height,
                    f'{acc:.4f}', ha='center', va='bottom', fontsize=11, fontweight='bold')



plt.tight_layout()
plt.savefig('/Users/andhar/Desktop/my_garden_of_python/deep_learning/phase_4_neural_networks/dl_1_neural_network.png',
            dpi=300, bbox_inches='tight')
print("\n✅ Visualization saved: dl_1_neural_network.png")