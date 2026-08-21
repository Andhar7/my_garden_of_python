

#   🧠 Phase 3.2: Classic ML Algorithms

#   Six Pillars of Machine Learning

#   ---
#   💡 THE SACRED QUESTION

#   ▎ "Which algorithm should I use for this problem?"

#   This is the question that separates amateurs from professionals.

#   You will learn when and WHY to use each algorithm. 🔮

# TODO
#   🎯 The Six Classic Algorithms

#   Each algorithm is like a different instrument in an orchestra. Each has its own voice, its own strength, its own sacred purpose.


# TODO
#   1️⃣ Linear Regression 📈

#   "Predict numbers with a straight line"

#   Purpose: Predict continuous values (numbers)

#   When to use:
#   - ✅ House prices (you just learned this!)
#   - ✅ Stock prices
#   - ✅ Temperature predictions
#   - ✅ Salary predictions

#   How it works:
#   y = mx + b

#   The model finds the line that best fits the data

#   Strength: Simple, fast, interpretable
#   Weakness: Only works for linear relationships

#   Example:
#   from sklearn.linear_model import LinearRegression

#   model = LinearRegression()
#   model.fit(X_train, y_train)
#   predictions = model.predict(X_test)

# TODO
#   2️⃣ Logistic Regression 🔐

#   "Predict categories (binary) with probability"

#   Purpose: Binary classification (yes/no, spam/not spam)

#   When to use:
#   - ✅ Email spam detection (spam or not?)
#   - ✅ Disease diagnosis (sick or healthy?)
#   - ✅ Credit approval (approve or deny?)
#   - ✅ Customer churn (leave or stay?)

#   How it works:
#   Instead of predicting a NUMBER (like price),
#   it predicts a PROBABILITY (0-1)

#   If probability > 0.5 → Class 1 (Yes/Spam/Sick)
#   If probability < 0.5 → Class 0 (No/Not Spam/Healthy)

#   Strength: Fast, gives probabilities, interpretable
#   Weakness: Only binary (two classes)

#   Example:
#   from sklearn.linear_model import LogisticRegression

#   model = LogisticRegression()
#   model.fit(X_train, y_train)
#   predictions = model.predict(X_test)
#   probabilities = model.predict_proba(X_test)

# TODO
#   3️⃣ Decision Trees 🌳

#   "Make decisions by asking yes/no questions"

#   Purpose: Classification and regression (very interpretable!)

#   When to use:
#   - ✅ Loan approval (ask: income? credit score? debt?)
#   - ✅ Medical diagnosis (ask: symptom A? symptom B?)
#   - ✅ Credit rating (ask: payment history? income?)
#   - ✅ When you need EXPLAINABLE decisions

#   How it works:
#              Is income > $50k?
#             /                  \
#            Yes                  No
#           /                      \
#       Is debt < $100k?        Deny Loan
#       /            \
#      Yes            No
#     /                \
#   Approve          Deny

#   Strength: Very interpretable, works with non-linear data
#   Weakness: Can overfit easily, unstable

#   Example:
#   from sklearn.tree import DecisionTreeClassifier

#   model = DecisionTreeClassifier(max_depth=5)
#   model.fit(X_train, y_train)
#   predictions = model.predict(X_test)

# TODO
#   4️⃣ Random Forest 🌲🌲🌲

#   "Ask many trees and take a vote"

#   Purpose: Classification and regression (ensemble method)

#   When to use:
#   - ✅ When you want POWERFUL predictions
#   - ✅ When you need to handle non-linear data
#   - ✅ When you want ROBUST models
#   - ✅ Most practical real-world problems

#   How it works:
#   Build 100 different decision trees:
#   - Tree 1 predicts: "Approve"
#   - Tree 2 predicts: "Deny"
#   - Tree 3 predicts: "Approve"
#   - ...Tree 100 predicts: "Approve"

#   Final prediction: "Approve" (majority vote!)

#   Strength: Very powerful, handles complexity, resistant to overfitting
#   Weakness: Slower, less interpretable than single tree

#   Example:
#   from sklearn.ensemble import RandomForestClassifier

#   model = RandomForestClassifier(n_estimators=100)
#   model.fit(X_train, y_train)
#   predictions = model.predict(X_test)

# TODO
#   5️⃣ K-Means Clustering 🎯

#   "Find natural groups in data (unsupervised)"

#   Purpose: Clustering (NO labels provided!)

#   When to use:
#   - ✅ Customer segmentation (find customer groups)
#   - ✅ Image compression (find dominant colors)
#   - ✅ Gene clustering (find similar genes)
#   - ✅ Document categorization (find similar docs)

#   How it works:

#   1. Start with K random points (centroids)
#   2. Assign each data point to nearest centroid
#   3. Move centroids to center of their cluster
#   4. Repeat until stable

#   Result: K clusters of similar data points

#   Strength: Simple, fast, works well
#   Weakness: Must choose K in advance, can find bad clusters

#   Example:
#   from sklearn.cluster import KMeans

#   model = KMeans(n_clusters=3)
#   cluster_assignments = model.fit_predict(X)
#   centroids = model.cluster_centers_

# TODO
#   6️⃣ K-Nearest Neighbors (KNN) 👥

#   "You are the average of your 5 nearest neighbors"

#   Purpose: Classification and regression (simple baseline)

#   When to use:
#   - ✅ When you have labeled data but no pattern
#   - ✅ As a baseline to compare against
#   - ✅ When interpretability isn't critical
#   - ✅ Small to medium datasets

#   How it works:
#   To classify a NEW point:
#   1. Find the K nearest training points
#   2. Look at their labels
#   3. Take the MAJORITY vote

#   K=3: Look at 3 nearest neighbors
#   K=5: Look at 5 nearest neighbors

#   Strength: Simple, no training needed, flexible
#   Weakness: Slow on large data, needs scaling

#   Example:
#   from sklearn.neighbors import KNeighborsClassifier

#   model = KNeighborsClassifier(n_neighbors=5)
#   model.fit(X_train, y_train)
#   predictions = model.predict(X_test)

# TODO
#   📊 COMPARISON TABLE

#   ┌─────────────────────┬────────────────┬─────────────┬───────────┬───────────────┬─────────────────────────┐
#   │      Algorithm      │      Type      │    Speed    │ Accuracy  │ Interpretable │        Best For         │
#   ├─────────────────────┼────────────────┼─────────────┼───────────┼───────────────┼─────────────────────────┤
#   │ Linear Regression   │ Regression     │ ⚡⚡⚡ Fast │ Medium    │ ✅ Yes        │ Simple linear data      │
#   ├─────────────────────┼────────────────┼─────────────┼───────────┼───────────────┼─────────────────────────┤
#   │ Logistic Regression │ Classification │ ⚡⚡⚡ Fast │ Medium    │ ✅ Yes        │ Binary classification   │
#   ├─────────────────────┼────────────────┼─────────────┼───────────┼───────────────┼─────────────────────────┤
#   │ Decision Tree       │ Both           │ ⚡⚡ Medium │ High      │ ✅ Yes        │ Interpretability needed │
#   ├─────────────────────┼────────────────┼─────────────┼───────────┼───────────────┼─────────────────────────┤
#   │ Random Forest       │ Both           │ ⚡ Slow     │ Very High │ ❌ No         │ Best accuracy needed    │
#   ├─────────────────────┼────────────────┼─────────────┼───────────┼───────────────┼─────────────────────────┤
#   │ K-Means             │ Clustering     │ ⚡⚡ Medium │ N/A       │ ✅ Yes        │ Find groups             │
#   ├─────────────────────┼────────────────┼─────────────┼───────────┼───────────────┼─────────────────────────┤
#   │ KNN                 │ Both           │ ❌ Slow     │ High      │ ❌ No         │ Baseline comparison     │
#   └─────────────────────┴────────────────┴─────────────┴───────────┴───────────────┴─────────────────────────┘


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# REGRESSION ALGORITHMS
from sklearn.linear_model import LinearRegression

# CLASSIFICATION ALGORITHMS
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# CLUSTERING
from sklearn.cluster import KMeans

# METRICS
from sklearn.metrics import (
    mean_squared_error, r2_score,
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix
)
print("\n" + "="*70)
print("PHASE 3, CHECKPOINT 3.2: Classic ML Algorithms")
print("="*70)

# ============================================================================
# PART 1: REGRESSION - PREDICTING CONTINUOUS VALUES
# ============================================================================
print("\n" + "="*70)
print("PART 1: REGRESSION ALGORITHMS")
print("Predicting continuous values (numbers)")
print("="*70)

# Create regression dataset: House prices
np.random.seed(42)
n_samples = 200

# Features: Size (m²), Age (years), Bedrooms
X_size = np.random.rand(n_samples) * 200 + 100      # 100-300 m²
X_age = np.random.rand(n_samples) * 50              # 0-50 years
X_beds = np.random.randint(1, 6, n_samples)         # 1-5 bedrooms
X_reg = np.column_stack([X_size, X_age, X_beds])

# Price = 5000*size - 10000*age + 50000*beds + noise
y_reg = 5000*X_size - 10000*X_age + 50000*X_beds + np.random.randn(n_samples)*100000

# Split data
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

print(f"\nRegression Dataset:")
print(f"Samples: {len(X_reg)}")
print(f"Features: Size (m²), Age (years), Bedrooms")
print(f"Target: Price ($)")
print(f"Price range: ${y_reg.min():,.0f} to ${y_reg.max():,.0f}")

# ============================================================================
# ALGORITHM 1: Linear Regression
# ============================================================================
print("\n" + "-"*70)
print("ALGORITHM 1: Linear Regression")
print("-"*70)

model_lr = LinearRegression()
model_lr.fit(X_train_reg, y_train_reg)
y_pred_lr = model_lr.predict(X_test_reg)
r2_lr = r2_score(y_test_reg, y_pred_lr)
rmse_lr = np.sqrt(mean_squared_error(y_test_reg, y_pred_lr))

print(f"\nLinear Regression Results:")
print(f"R² Score: {r2_lr:.4f}")
print(f"RMSE: ${rmse_lr:,.0f}")
print(f"Coefficients:")
print(f"  - Size coefficient: ${model_lr.coef_[0]:,.2f} per m²")
print(f"  - Age coefficient: ${model_lr.coef_[1]:,.2f} per year")
print(f"  - Beds coefficient: ${model_lr.coef_[2]:,.2f} per bedroom")

# ============================================================================
# PART 2: CLASSIFICATION - PREDICTING CATEGORIES
# ============================================================================
print("\n" + "="*70)
print("PART 2: CLASSIFICATION ALGORITHMS")
print("Predicting categories (binary: Yes/No)")
print("="*70)

# Create classification dataset: Email spam detection
np.random.seed(42)
n_samples = 300

# Features: word_frequency (0-1), caps_ratio (0-1), sender_reputation (-1 to 1)
X_word_freq = np.random.rand(n_samples)
X_caps = np.random.rand(n_samples)
X_reputation = np.random.randn(n_samples)
X_clf = np.column_stack([X_word_freq, X_caps, X_reputation])

# Target: Spam (1) or Not Spam (0)
# Spam if: high word frequency AND high caps AND bad reputation
y_clf = ((X_word_freq > 0.5) & (X_caps > 0.5) & (X_reputation < 0)).astype(int)

# Add some noise
noise_indices = np.random.choice(n_samples, 50, replace=False)
y_clf[noise_indices] = 1 - y_clf[noise_indices]

# Split data
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42
)
# Scale features (important for some algorithms)
scaler = StandardScaler()
X_train_clf_scaled = scaler.fit_transform(X_train_clf)
X_test_clf_scaled = scaler.transform(X_test_clf)

print(f"\nClassification Dataset:")
print(f"Samples: {len(X_clf)}")
print(f"Features: word_frequency, caps_ratio, sender_reputation")
print(f"Target: Spam (1) or Not Spam (0)")
print(f"Class distribution: {np.sum(y_clf)} spam, {len(y_clf) - np.sum(y_clf)} not spam")

# ============================================================================
# ALGORITHM 2: Logistic Regression
# ============================================================================
print("\n" + "-"*70)
print("ALGORITHM 2: Logistic Regression")
print("-"*70)

model_logr = LogisticRegression(random_state=42)
model_logr.fit(X_train_clf_scaled, y_train_clf)
y_pred_logr = model_logr.predict(X_test_clf_scaled)
acc_logr = accuracy_score(y_test_clf, y_pred_logr)
prec_logr = precision_score(y_test_clf, y_pred_logr)
rec_logr = recall_score(y_test_clf, y_pred_logr)
f1_logr = f1_score(y_test_clf, y_pred_logr)

print(f"\nLogistic Regression Results:")
print(f"Accuracy: {acc_logr:.4f}")
print(f"Precision: {prec_logr:.4f} (of predicted spam, how many are really spam?)")
print(f"Recall: {rec_logr:.4f} (of actual spam, how many did we find?)")
print(f"F1-Score: {f1_logr:.4f}")

# ============================================================================
# ALGORITHM 3: Decision Tree
# ============================================================================
print("\n" + "-"*70)
print("ALGORITHM 3: Decision Tree")
print("-"*70)

model_tree = DecisionTreeClassifier(max_depth=5, random_state=42)
model_tree.fit(X_train_clf, y_train_clf)
y_pred_tree = model_tree.predict(X_test_clf)
acc_tree = accuracy_score(y_test_clf, y_pred_tree)
prec_tree = precision_score(y_test_clf, y_pred_tree)
rec_tree = recall_score(y_test_clf, y_pred_tree)
f1_tree = f1_score(y_test_clf, y_pred_tree)

print(f"\nDecision Tree Results:")
print(f"Accuracy: {acc_tree:.4f}")
print(f"Precision: {prec_tree:.4f}")
print(f"Recall: {rec_tree:.4f}")
print(f"F1-Score: {f1_tree:.4f}")
print(f"Tree depth used: 5 (max depth to prevent overfitting)")

# ============================================================================
# ALGORITHM 4: Random Forest
# ============================================================================
print("\n" + "-"*70)
print("ALGORITHM 4: Random Forest")
print("-"*70)

model_rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model_rf.fit(X_train_clf, y_train_clf)
y_pred_rf = model_rf.predict(X_test_clf)
acc_rf = accuracy_score(y_test_clf, y_pred_rf)
prec_rf = precision_score(y_test_clf, y_pred_rf)
rec_rf = recall_score(y_test_clf, y_pred_rf)
f1_rf = f1_score(y_test_clf, y_pred_rf)

print(f"\nRandom Forest Results:")
print(f"Accuracy: {acc_rf:.4f}")
print(f"Precision: {prec_rf:.4f}")
print(f"Recall: {rec_rf:.4f}")
print(f"F1-Score: {f1_rf:.4f}")
print(f"Number of trees: 100")
print(f"Feature importances:")

for i, importance in enumerate(model_rf.feature_importances_):
    feature_names = ['word_frequency', 'caps_ratio', 'sender_reputation']
    print(f"  - {feature_names[i]}: {importance:.4f}")
    
# ============================================================================
# ALGORITHM 5: K-Nearest Neighbors
# ============================================================================
print("\n" + "-"*70)
print("ALGORITHM 5: K-Nearest Neighbors (KNN)")
print("-"*70)

model_knn = KNeighborsClassifier(n_neighbors=5)
model_knn.fit(X_train_clf_scaled, y_train_clf)
y_pred_knn = model_knn.predict(X_test_clf_scaled)
acc_knn = accuracy_score(y_test_clf, y_pred_knn)
prec_knn = precision_score(y_test_clf, y_pred_knn)
rec_knn = recall_score(y_test_clf, y_pred_knn)
f1_knn = f1_score(y_test_clf, y_pred_knn)

print(f"\nK-Nearest Neighbors Results:")
print(f"Accuracy: {acc_knn:.4f}")
print(f"Precision: {prec_knn:.4f}")
print(f"Recall: {rec_knn:.4f}")
print(f"F1-Score: {f1_knn:.4f}")
print(f"K value: 5 (look at 5 nearest neighbors)")

# ============================================================================
# PART 3: CLUSTERING - UNSUPERVISED LEARNING
# ============================================================================
print("\n" + "="*70)
print("PART 3: CLUSTERING ALGORITHM")
print("Finding natural groups in data (NO labels!)")
print("="*70)

# Create clustering dataset: Customer segments
np.random.seed(42)
n_samples = 300

# Two clusters with some overlap
cluster_1 = np.random.normal([2, 2], 0.8, (150, 2))
cluster_2 = np.random.normal([8, 8], 1.0, (150, 2))
X_cluster = np.vstack([cluster_1, cluster_2])

print(f"\nClustering Dataset:")
print(f"Samples: {len(X_cluster)}")
print(f"Features: 2 (could be Income, Age or any features)")
print(f"Note: We have NO labels (unsupervised!)")

# ============================================================================
# ALGORITHM 6: K-Means Clustering
# ============================================================================
print("\n" + "-"*70)
print("ALGORITHM 6: K-Means Clustering")
print("-"*70)

model_kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
cluster_assignments = model_kmeans.fit_predict(X_cluster)
centroids = model_kmeans.cluster_centers_

print(f"\nK-Means Results:")
print(f"Number of clusters: 2")
print(f"Cluster 0 size: {np.sum(cluster_assignments == 0)} samples")
print(f"Cluster 1 size: {np.sum(cluster_assignments == 1)} samples")
print(f"Centroid 0: {centroids[0]}")
print(f"Centroid 1: {centroids[1]}")
print(f"Inertia (within-cluster variance): {model_kmeans.inertia_:.2f}")

# ============================================================================
# ALGORITHM COMPARISON
# ============================================================================
print("\n" + "="*70)
print("ALGORITHM COMPARISON (Classification Tasks)")
print("="*70)
comparison_data = {
    'Algorithm': [
        'Logistic Regression',
        'Decision Tree',
        'Random Forest',
        'K-Nearest Neighbors'
    ],
    'Accuracy': [acc_logr, acc_tree, acc_rf, acc_knn],
    'Precision': [prec_logr, prec_tree, prec_rf, prec_knn],
    'Recall': [rec_logr, rec_tree, rec_rf, rec_knn],
    'F1-Score': [f1_logr, f1_tree, f1_rf, f1_knn]
}
comparison_df = pd.DataFrame(comparison_data)
print("\n" + comparison_df.to_string(index=False))

# Find best algorithm by F1-score
best_idx = np.argmax([f1_logr, f1_tree, f1_rf, f1_knn])
best_algorithm = comparison_data['Algorithm'][best_idx]
print(f"\n🏆 BEST ALGORITHM (by F1-Score): {best_algorithm}")

# ============================================================================
# VISUALIZATIONS
# ============================================================================
print("\n" + "="*70)
print("Creating visualizations...")
print("="*70)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Regression models comparison
algorithms_reg = ['Linear Regression']
r2_scores_reg = [r2_lr]
rmse_scores_reg = [rmse_lr]
axes[0, 0].bar(algorithms_reg, r2_scores_reg, color='blue', alpha=0.7)
axes[0, 0].set_ylabel('R² Score')
axes[0, 0].set_title('Regression: Linear Regression Performance\n(R² Score)')
axes[0, 0].set_ylim([0, 1])
axes[0, 0].grid(True, alpha=0.3)
for i, v in enumerate(r2_scores_reg):
    axes[0, 0].text(i, v + 0.02, f'{v:.4f}', ha='center')
    
# Plot 2: Classification accuracy comparison
algorithms_clf = ['Logistic\nRegression', 'Decision\nTree', 'Random\nForest', 'KNN']
accuracies = [acc_logr, acc_tree, acc_rf, acc_knn]
colors = ['blue', 'green', 'red', 'orange']
axes[0, 1].bar(algorithms_clf, accuracies, color=colors, alpha=0.7)
axes[0, 1].set_ylabel('Accuracy')
axes[0, 1].set_title('Classification: Algorithm Accuracy Comparison')
axes[0, 1].set_ylim([0, 1])
axes[0, 1].grid(True, alpha=0.3)
for i, v in enumerate(accuracies):
    axes[0, 1].text(i, v + 0.02, f'{v:.4f}', ha='center')
    
# Plot 3: F1-Score comparison
f1_scores = [f1_logr, f1_tree, f1_rf, f1_knn]
axes[1, 0].bar(algorithms_clf, f1_scores, color=colors, alpha=0.7)
axes[1, 0].set_ylabel('F1-Score')
axes[1, 0].set_title('Classification: F1-Score Comparison\n(Balance of Precision & Recall)')
axes[1, 0].set_ylim([0, 1])
axes[1, 0].grid(True, alpha=0.3)
for i, v in enumerate(f1_scores):
    axes[1, 0].text(i, v + 0.02, f'{v:.4f}', ha='center')
    
# Plot 4: K-Means Clustering visualization
scatter_colors = ['red' if c == 0 else 'blue' for c in cluster_assignments]
axes[1, 1].scatter(X_cluster[:, 0], X_cluster[:, 1], c=scatter_colors, alpha=0.6, s=50)
axes[1, 1].scatter(centroids[:, 0], centroids[:, 1], c=['darkred', 'darkblue'],
                   s=300, marker='*', edgecolors='black', linewidth=2, label='Centroids')
axes[1, 1].set_xlabel('Feature 1')
axes[1, 1].set_ylabel('Feature 2')
axes[1, 1].set_title('K-Means Clustering\n(2 clusters found)')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/machine_learning/phase_3_fundamentals/ml_2_algorithms.png', dpi=150)
plt.close()
print("\n✅ Visualization saved!")

# ============================================================================
# KEY INSIGHTS
# ============================================================================
print("\n" + "="*70)
print("KEY INSIGHTS FROM CLASSIC ALGORITHMS")
print("="*70)
print("""
1. REGRESSION vs CLASSIFICATION
   - Regression: Predict numbers (price, temperature, salary)
   - Classification: Predict categories (spam/not spam, yes/no)
2. LINEAR REGRESSION
   - Simplest algorithm
   - Works for linear relationships
   - Fast and interpretable
3. LOGISTIC REGRESSION
   - For binary classification
   - Gives probabilities (0-1)
   - Fast and interpretable
4. DECISION TREES
   - Very interpretable (like flowcharts)
   - Can capture non-linear patterns
   - Risk of overfitting
5. RANDOM FOREST
   - Ensemble of many trees
   - Very accurate and robust
   - Less interpretable
   - Often the best practical choice
6. K-NEAREST NEIGHBORS
   - Simple baseline algorithm
   - Slow on large datasets
   - No training phase needed
7. K-MEANS CLUSTERING
   - Unsupervised learning (no labels!)
   - Finds natural groups
   - Must choose K in advance
8. METRICS MATTER
   - Different problems need different metrics
   - Accuracy alone is not enough
   - Use precision, recall, F1-score together
9. ALGORITHM SELECTION
   - No one best algorithm (depends on data!)
   - Start simple (Linear/Logistic)
   - Try Random Forest if accuracy needed
   - Always compare multiple algorithms
10. THE PATTERN
    - Simple algorithms are fast but less accurate
    - Complex algorithms are slower but more accurate
    - Best choice balances speed and accuracy
""")
print("\n" + "="*70)
print("✅ Checkpoint 3.2: Classic Algorithms - FOUNDATION LAID")
print("="*70)
