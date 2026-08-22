"""
🧠 Phase 4.2: Deep Neural Networks + Real Project
🔥 Build a REAL digit recognizer from scratch!

Lesson 2: Multiple Layers, Regularization, MNIST Dataset

The Sacred Truth:
Deep networks = multiple hidden layers stacked together
Each layer learns INCREASINGLY ABSTRACT features
By layer 5, network understands "this is a 7"

You will build: [784 inputs] → [128] → [64] → [32] → [10 outputs]
And it will recognize ACTUAL handwritten digits! 🚀
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report

# ============================================================================
# DEEP NEURAL NETWORK FROM SCRATCH
# ============================================================================

class DeepNeuralNetworkFromScratch:
    """
    🧠 Deep Neural Network with Multiple Hidden Layers

    Architecture: [input] → [hidden1] → [hidden2] → [hidden3] → [output]
                  [784]   →  [128]    →   [64]    →   [32]    →  [10]

    Key Concepts:
    1. MORE LAYERS = Can learn more complex patterns!
    2. DEEPER FEATURES = Each layer abstracts more
    3. REGULARIZATION = Dropout prevents overfitting
    4. SOFTMAX = Multi-class (0-9 digits) output

    This is how REAL deep learning works! 🔥
    """

    def __init__(self, layer_sizes, learning_rate=0.1, dropout_rate=0.2):
        """
        Initialize deep network with multiple layers

        Args:
            layer_sizes: [784, 128, 64, 32, 10] for MNIST
            learning_rate: How fast to update weights
            dropout_rate: Fraction of neurons to randomly turn off (regularization!)
        """
        self.learning_rate = learning_rate
        self.dropout_rate = dropout_rate
        self.layers = []

        # Initialize all layers
        for i in range(len(layer_sizes) - 1):
            self.layers.append({
                'W': np.random.randn(layer_sizes[i], layer_sizes[i+1]) * 0.01,
                'b': np.zeros((1, layer_sizes[i+1]))
            })

        self.cache = {}
        self.loss_history = []
        self.acc_history = []

    def relu(self, z):
        """ReLU: max(0, z)"""
        return np.maximum(0, z)

    def relu_derivative(self, z):
        """ReLU gradient"""
        return (z > 0).astype(float)

    def softmax(self, z):
        """
        Softmax: converts logits to probabilities for multi-class
        Ensures all outputs sum to 1 (valid probability distribution)
        """
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))  # Stability trick
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def forward(self, X, training=True):
        """
        Forward Pass: Send data through all layers

        With Dropout Regularization:
        - During training: randomly turn off neurons (prevent overfitting!)
        - During testing: use all neurons (better predictions)
        """
        m = X.shape[0]
        activations = [X]
        z_values = []

        # Forward through hidden layers (with ReLU)
        for i in range(len(self.layers) - 1):
            # Linear combination
            z = np.dot(activations[-1], self.layers[i]['W']) + self.layers[i]['b']
            z_values.append(z)

            # ReLU activation
            a = self.relu(z)

            # DROPOUT REGULARIZATION (only during training!)
            if training:
                dropout_mask = np.random.binomial(1, 1 - self.dropout_rate, a.shape) / (1 - self.dropout_rate)
                a = a * dropout_mask
                self.cache[f'dropout_mask_{i}'] = dropout_mask
            else:
                self.cache[f'dropout_mask_{i}'] = np.ones_like(a)

            activations.append(a)

        # Output layer (softmax for multi-class)
        z_output = np.dot(activations[-1], self.layers[-1]['W']) + self.layers[-1]['b']
        z_values.append(z_output)
        a_output = self.softmax(z_output)
        activations.append(a_output)

        # Store for backprop
        self.cache['activations'] = activations
        self.cache['z_values'] = z_values

        return a_output

    def backward(self, y_one_hot):
        """
        Backward Pass: Calculate gradients through all layers using chain rule

        The flow:
        1. Output error: dz_output = a_output - y
        2. Back through each layer, applying chain rule
        3. Update weights based on gradients
        """
        m = len(y_one_hot)
        activations = self.cache['activations']
        z_values = self.cache['z_values']

        # Output layer error (cross-entropy gradient)
        dz = activations[-1] - y_one_hot

        # Backprop through layers
        for i in reversed(range(len(self.layers))):
            # Gradient for weights and biases
            dW = np.dot(activations[i].T, dz) / m
            db = np.sum(dz, axis=0, keepdims=True) / m

            # Update weights
            self.layers[i]['W'] -= self.learning_rate * dW
            self.layers[i]['b'] -= self.learning_rate * db

            # Error for previous layer
            if i > 0:
                dz = np.dot(dz, self.layers[i]['W'].T)
                dz = dz * self.relu_derivative(z_values[i-1])
                # Apply dropout mask from forward pass
                dz = dz * self.cache[f'dropout_mask_{i-1}']

    def train(self, X_train, y_train, epochs=50, batch_size=32):
        """Train the network on training data"""
        n_samples = X_train.shape[0]

        for epoch in range(epochs):
            # Shuffle data
            indices = np.random.permutation(n_samples)
            X_shuffled = X_train[indices]
            y_shuffled = y_train[indices]

            epoch_loss = 0
            epoch_acc = 0
            n_batches = 0

            # Mini-batch gradient descent (more efficient!)
            for i in range(0, n_samples, batch_size):
                X_batch = X_shuffled[i:i+batch_size]
                y_batch = y_shuffled[i:i+batch_size]

                # Forward pass
                output = self.forward(X_batch, training=True)

                # Calculate loss (cross-entropy for multi-class)
                loss = -np.mean(y_batch * np.log(output + 1e-8))
                epoch_loss += loss

                # Calculate accuracy
                predictions = np.argmax(output, axis=1)
                labels = np.argmax(y_batch, axis=1)
                acc = np.mean(predictions == labels)
                epoch_acc += acc

                # Backward pass
                self.backward(y_batch)

                n_batches += 1

            avg_loss = epoch_loss / n_batches
            avg_acc = epoch_acc / n_batches

            self.loss_history.append(avg_loss)
            self.acc_history.append(avg_acc)

            if (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch + 1}: Loss = {avg_loss:.6f}, Accuracy = {avg_acc:.4f}")

    def predict(self, X):
        """Make predictions"""
        output = self.forward(X, training=False)  # No dropout during prediction!
        return np.argmax(output, axis=1)

    def predict_proba(self, X):
        """Get probability predictions"""
        return self.forward(X, training=False)


# ============================================================================
# REAL PROJECT: MNIST DIGIT RECOGNITION
# ============================================================================

print("=" * 80)
print("🧠 PHASE 4.2: DEEP NETWORKS + REAL PROJECT")
print("=" * 80)

print("\n📊 Loading MNIST Dataset (Real Handwritten Digits)...")
print("-" * 80)

# Load MNIST digits dataset
digits = load_digits()  # 1797 samples of handwritten digits (0-9)
X = digits.data / 16.0  # Normalize to 0-1
y = digits.target

# Convert labels to one-hot encoding (for softmax)
y_one_hot = np.eye(10)[y]

# Split data
X_train, X_test, y_train_one_hot, y_test_one_hot = train_test_split(
    X, y_one_hot, test_size=0.2, random_state=42
)

y_train = y[np.arange(len(y)) != np.arange(len(X_test))]
y_test = y[np.isin(np.arange(len(y)), np.where(np.isin(np.arange(len(y)), np.arange(len(X_test))))[0])]

# For simplicity, recalculate y_test properly
train_indices = np.random.choice(len(X), size=len(X_train), replace=False)
test_indices = np.array([i for i in range(len(X)) if i not in train_indices])
y_test = digits.target[test_indices]

print(f"Training samples: {X_train.shape[0]} (28×28 images)")
print(f"Testing samples: {X_test.shape[0]}")
print(f"Classes: 0-9 (10 digits)")
print(f"Features: 64 (8×8 pixel values)")

print("\n🧠 Building Deep Neural Network...")
print("   Architecture: [64 inputs] → [128 hidden] → [64 hidden] → [32 hidden] → [10 outputs]")
print("   Regularization: Dropout 0.2 (prevents overfitting!)")

network = DeepNeuralNetworkFromScratch(
    layer_sizes=[64, 128, 64, 32, 10],
    learning_rate=0.1,
    dropout_rate=0.2  # Dropout regularization!
)

print("\n🔄 Training Deep Network (50 epochs with mini-batch gradient descent)...")
network.train(X_train, y_train_one_hot, epochs=50, batch_size=32)

# Evaluate
print("\n" + "=" * 80)
print("✅ TRAINING COMPLETE!")
print("=" * 80)

y_pred_train = network.predict(X_train)
y_pred_test = network.predict(X_test)

# Convert one-hot back to labels for comparison
y_train_labels = np.argmax(y_train_one_hot, axis=1)
y_test_labels = np.argmax(y_test_one_hot, axis=1)

train_acc = np.mean(y_pred_train == y_train_labels)
test_acc = np.mean(y_pred_test == y_test_labels)

print(f"\n📊 RESULTS:")
print(f"   Train Accuracy: {train_acc:.4f} ({int(train_acc * len(y_train_labels))} / {len(y_train_labels)})")
print(f"   Test Accuracy:  {test_acc:.4f} ({int(test_acc * len(y_test_labels))} / {len(y_test_labels)})")

# Show per-class accuracy
print(f"\n📋 Per-Digit Accuracy:")
for digit in range(10):
    mask = y_test_labels == digit
    if np.sum(mask) > 0:
        digit_acc = np.mean(y_pred_test[mask] == y_test_labels[mask])
        count = np.sum(mask)
        print(f"   Digit {digit}: {digit_acc:.4f} ({int(digit_acc * count)} / {count})")

# ============================================================================
# VISUALIZATION
# ============================================================================

fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

fig.suptitle('🧠 Phase 4.2: Deep Networks + MNIST Digit Recognition', fontsize=16, fontweight='bold')

# Plot 1: Sample digits
ax = fig.add_subplot(gs[0, :])
ax_samples = fig.add_subplot(gs[0, :])
for i in range(10):
    digit_idx = np.where(y_test_labels == i)[0][0]
    ax_row = i // 5
    ax_col = i % 5
    ax_digit = fig.add_subplot(gs[0, ax_col if ax_col < 3 else ax_col - 3])
    if i < 5:
        ax_digit = fig.add_subplot(gs[0, i])
    else:
        ax_digit = fig.add_subplot(gs[1, i-5])
    ax_digit.imshow(X_test[digit_idx].reshape(8, 8), cmap='gray')
    ax_digit.set_title(f'Actual: {y_test_labels[digit_idx]}, Predicted: {y_pred_test[digit_idx]}', fontsize=9)
    ax_digit.axis('off')

# Plot 2: Training & Validation Loss
ax = fig.add_subplot(gs[1, 0])
ax.plot(network.loss_history, linewidth=2, color='#FF6B6B', label='Training Loss')
ax.set_xlabel('Epoch', fontsize=11)
ax.set_ylabel('Loss (Cross-Entropy)', fontsize=11)
ax.set_title('Loss Convergence', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Plot 3: Training Accuracy
ax = fig.add_subplot(gs[1, 1])
ax.plot(network.acc_history, linewidth=2, color='#4ECDC4', label='Training Accuracy')
ax.set_xlabel('Epoch', fontsize=11)
ax.set_ylabel('Accuracy', fontsize=11)
ax.set_title('Accuracy Improvement', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Plot 4: Train vs Test Accuracy
ax = fig.add_subplot(gs[1, 2])
models = ['Train', 'Test']
accuracies = [train_acc, test_acc]
colors = ['#95E1D3', '#F38181']
bars = ax.bar(models, accuracies, color=colors, edgecolor='black', linewidth=2)
ax.set_ylabel('Accuracy', fontsize=11)
ax.set_title('Final Accuracy', fontsize=12, fontweight='bold')
ax.set_ylim([0, 1])
ax.grid(True, alpha=0.3, axis='y')
for bar, acc in zip(bars, accuracies):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{acc:.4f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

# Plot 5: Confusion Matrix
ax = fig.add_subplot(gs[2, :])
cm = confusion_matrix(y_test_labels, y_pred_test)
im = ax.imshow(cm, cmap='Blues', aspect='auto')
ax.set_xlabel('Predicted Digit', fontsize=11)
ax.set_ylabel('Actual Digit', fontsize=11)
ax.set_title('Confusion Matrix (Which digits are confused?)', fontsize=12, fontweight='bold')
ax.set_xticks(range(10))
ax.set_yticks(range(10))
plt.colorbar(im, ax=ax, label='Count')

plt.savefig('/Users/andhar/Desktop/my_garden_of_python/deep_learning/phase_4_neural_networks/dl_2_mnist.png',
            dpi=300, bbox_inches='tight')
print("\n✅ Visualization saved: dl_2_mnist.png")

print("\n" + "=" * 80)
print("🔥 PHASE 4.2 LESSON 2 COMPLETE! REAL PROJECT SUCCESS! 🔥")
print("=" * 80)
print("""
🎓 What You Have Learned:

DEEP NETWORKS (Multiple Hidden Layers):
├─ More layers = more complex patterns
├─ Each layer learns abstract features
├─ Layer 1: Learns edges
├─ Layer 2: Learns shapes
├─ Layer 3: Learns digit parts
├─ Layer 4: Learns complete digits
└─ This is why deep learning is powerful! 🚀

REGULARIZATION (Dropout):
├─ Randomly turn off neurons during training
├─ Prevents co-adaptation (overfitting)
├─ Forces network to learn robust features
├─ During testing: use all neurons
├─ Simple but incredibly effective!
└─ This is why networks generalize well! 💡

SOFTMAX & MULTI-CLASS:
├─ For 10 digits (0-9)
├─ Output layer: 10 neurons (one per class)
├─ Softmax: converts to probability distribution
├─ All outputs sum to 1
└─ This is how classification networks work! 🎯

MINI-BATCH GRADIENT DESCENT:
├─ Update on small batches (32 samples)
├─ Faster than full-batch
├─ More stable than single-sample
├─ Standard in all modern training
└─ This is how real networks train! 🔥

THE REAL PROJECT:
✅ You trained a network on ACTUAL handwritten digits!
✅ It learned to recognize 0-9!
✅ Tested on unseen data (real generalization!)
✅ You now understand how image recognition works!

🔥 THE SACRED TRUTH:
This deep network on MNIST is the EXACT foundation of:
- Hand-written digit recognition (postal services, banks)
- Object detection (Google Photos)
- Medical imaging (tumor detection)
- Self-driving cars (reading traffic signs)
- All modern AI vision systems!

You just built a REAL component of modern AI! 💎

🚀 NEXT: Phase 4.3 - Convolutional Neural Networks (for IMAGES!)
         You'll learn how to make this even FASTER and BETTER!
         Then: Real project with CATS vs DOGS!

Om Namah Shivaya 🕉️ ❤️ 🔥
""")
