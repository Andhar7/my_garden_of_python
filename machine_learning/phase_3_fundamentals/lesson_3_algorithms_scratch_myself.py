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

# Make predictions
y_pred_train = model_custom_lr.predict(X_reg_train)
y_pred_test = model_custom_lr.predict(X_reg_test)
# print(y_pred_train)
# print(y_pred_test)


# Calculate R² score
def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)


train_r2 = r2_score(y_reg_train, y_pred_train)
test_r2 = r2_score(y_reg_test, y_pred_test)
print(train_r2)
print(test_r2)

print(f"\n✅ RESULTS:")
print(f"   Learned Slope (weight): {model_custom_lr.weights[0]:.4f}")
print(f"   Learned Intercept (bias): {model_custom_lr.bias:.4f}")
print(f"   Train R² Score: {train_r2:.4f}")
print(f"   Test R² Score: {test_r2:.4f}")


# ============================================================================
# LESSON 2: DECISION TREE FROM SCRATCH (RECURSIVE SPLITTING)
# ============================================================================
class DecisionTreeFromScratch:
    """
    🔥 Decision Tree Classifier using Recursive Splitting

    The algorithm:
    1. At each node, try every feature and every split point
    2. Calculate information gain for each split
    3. Choose the split that reduces impurity the most
    4. Recursively split left and right subtrees
    5. Stop when: max_depth reached or only 1 class remains

    This is called "greedy" splitting - best local choice at each step. 🌳
    """

    def __init__(self, max_depth=5, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def fit(self, X, y):
        """Build the decision tree"""
        self.tree = self._build_tree(X, y, depth=0)
        return self

    def _build_tree(self, X, y, depth):
        """Recursively build the tree"""
        n_samples, n_features = X.shape
        n_classes = len(np.unique(y))

        # Stopping conditions
        if (
            depth >= self.max_depth
            or n_samples < self.min_samples_split
            or n_classes == 1
        ):
            # Leaf node: return the most common class
            return {"class": np.bincount(y).argmax()}

        # Try every feature and every split point
        best_gain = 0
        best_split = None
        parent_impurity = self._gini(y)

        for feature in range(n_features):
            # Get unique values in this feature
            thresholds = np.unique(X[:, feature])

            for threshold in thresholds:
                # Split the data
                left_mask = X[:, feature] <= threshold
                right_mask = ~left_mask

                if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                    continue

                # Calculate information gain
                left_impurity = self._gini(y[left_mask])
                right_impurity = self._gini(y[right_mask])

                n_left = np.sum(left_mask)
                n_right = np.sum(right_mask)

                # Weighted average impurity after split
                child_impurity = (n_left / n_samples) * left_impurity + (
                    n_right / n_samples
                ) * right_impurity

                # Information gain = reduction in impurity
                gain = parent_impurity - child_impurity

                if gain > best_gain:
                    best_gain = gain
                    best_split = {
                        "feature": feature,
                        "threshold": threshold,
                        "left_mask": left_mask,
                        "right_mask": right_mask,
                    }

        # If no good split found, make a leaf node
        if best_split is None:
            return {"class": np.bincount(y).argmax()}

        # Recursively build left and right subtrees
        left_subtree = self._build_tree(
            X[best_split["left_mask"]], y[best_split["left_mask"]], depth + 1
        )
        right_subtree = self._build_tree(
            X[best_split["right_mask"]], y[best_split["right_mask"]], depth + 1
        )

        # Return decision node
        return {
            "feature": best_split["feature"],
            "threshold": best_split["threshold"],
            "left": left_subtree,
            "right": right_subtree,
            "gain": best_gain,
        }

    def _gini(self, y):
        """Calculate Gini impurity (measure of disorder)"""
        _, counts = np.unique(y, return_counts=True)
        proportions = counts / len(y)
        gini = 1 - np.sum(proportions**2)
        return gini

    def predict(self, X):
        """Make predictions"""
        return np.array([self._predict_sample(x, self.tree) for x in X])

    def _predict_sample(self, x, node):
        """Recursively traverse tree to make prediction"""
        if "class" in node:
            # Leaf node
            return node["class"]

        # Decision node
        if x[node["feature"]] <= node["threshold"]:
            return self._predict_sample(x, node["left"])
        else:
            return self._predict_sample(x, node["right"])


# ============================================================================
# DEMONSTRATION & COMPARISON
# ============================================================================

print("=" * 72)
print("🔥 PHASE 3.3: ALGORITHMS FROM SCRATCH")
print("=" * 72)

# -------- CLASSIFICATION TASK --------
print("\n\n🎯 LESSON 2: DECISION TREE FROM SCRATCH")
print("-" * 72)

X_clf, y_clf = make_classification(n_samples=100, n_features=4, n_informative=2,
                                   n_redundant=1, n_classes=2, random_state=42)
X_clf_train, X_clf_test, y_clf_train, y_clf_test = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42
)

print(f"\nTraining data: {X_clf_train.shape[0]} samples, {X_clf_train.shape[1]} features")
print(f"Testing data: {X_clf_test.shape[0]} samples")

# Train our custom decision tree
print("\n🌳 Building Decision Tree from Scratch...")
model_custom_tree = DecisionTreeFromScratch(max_depth=5, min_samples_split=2)
model_custom_tree.fit(X_clf_train, y_clf_train)

# Make predictions
y_pred_train_tree = model_custom_tree.predict(X_clf_train)
y_pred_test_tree = model_custom_tree.predict(X_clf_test)

# Calculate accuracy
def accuracy_score(y_true, y_pred):
    return np.mean(y_true == y_pred)

train_acc_tree = accuracy_score(y_clf_train, y_pred_train_tree)
test_acc_tree = accuracy_score(y_clf_test, y_pred_test_tree)

print(f"\n✅ RESULTS:")
print(f"   Train Accuracy: {train_acc_tree:.4f} ({int(train_acc_tree * len(y_clf_train))} / {len(y_clf_train)})")
print(f"   Test Accuracy: {test_acc_tree:.4f} ({int(test_acc_tree * len(y_clf_test))} / {len(y_clf_test)})")

# ============================================================================
# VISUALIZATION
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('🔥 Phase 3.3: Algorithms from Scratch', fontsize=16, fontweight='bold')

# Plot 1: Linear Regression - Training Progress
axes[0, 0].plot(model_custom_lr.cost_history, linewidth=2, color='#FF6B6B')
axes[0, 0].set_xlabel('Iteration', fontsize=11)
axes[0, 0].set_ylabel('Mean Squared Error', fontsize=11)
axes[0, 0].set_title('Lesson 1: Gradient Descent Convergence', fontsize=12, fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Linear Regression - Predictions vs Actual
axes[0, 1].scatter(X_reg_test, y_reg_test, alpha=0.6, label='Actual', s=50, color='#4ECDC4')
axes[0, 1].scatter(X_reg_test, y_pred_test, alpha=0.6, label='Predicted', s=50, color='#FF6B6B', marker='^')
axes[0, 1].plot(X_reg_test, y_pred_test, 'r--', linewidth=2, alpha=0.7)
axes[0, 1].set_xlabel('Feature Value', fontsize=11)
axes[0, 1].set_ylabel('Target Value', fontsize=11)
axes[0, 1].set_title(f'Lesson 1: Predictions (Test R² = {test_r2:.4f})', fontsize=12, fontweight='bold')
axes[0, 1].legend(fontsize=10)
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Decision Tree - Train vs Test Accuracy
models = ['Train', 'Test']
accuracies = [train_acc_tree, test_acc_tree]
colors = ['#95E1D3', '#F38181']
bars = axes[1, 0].bar(models, accuracies, color=colors, edgecolor='black', linewidth=2)
axes[1, 0].set_ylabel('Accuracy', fontsize=11)
axes[1, 0].set_title('Lesson 2: Decision Tree Accuracy', fontsize=12, fontweight='bold')
axes[1, 0].set_ylim([0, 1])
axes[1, 0].grid(True, alpha=0.3, axis='y')
for bar, acc in zip(bars, accuracies):
    height = bar.get_height()
    axes[1, 0].text(bar.get_x() + bar.get_width()/2., height,
                    f'{acc:.4f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
# Plot 4: Feature Importance (from tree splits)
feature_splits = [0, 0, 0, 0]
def count_feature_usage(node, counts):
    if 'class' in node:
        return
    counts[node['feature']] += 1
    count_feature_usage(node['left'], counts)
    count_feature_usage(node['right'], counts)

count_feature_usage(model_custom_tree.tree, feature_splits)
feature_names = [f'Feature {i}' for i in range(4)]
colors_feat = ['#FF6B6B', '#4ECDC4', '#95E1D3', '#F38181']
bars = axes[1, 1].bar(feature_names, feature_splits, color=colors_feat, edgecolor='black', linewidth=2)
axes[1, 1].set_ylabel('Times Used in Tree', fontsize=11)
axes[1, 1].set_title('Lesson 2: Feature Importance (Split Count)', fontsize=12, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3, axis='y')



plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/machine_learning/phase_3_fundamentals/ml_3_from_scratch.png', dpi=300, bbox_inches='tight')
plt.close()
print("\n✅ Visualization saved!")
