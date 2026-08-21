

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

print("\n" + "=" * 72)
print("PHASE 3, CHECKPOINT 3.1: Machine Learning Concepts")
print("=" * 72)
# ============================================================================
# EXAMPLE 1: The Danger of Testing on Training Data
# ============================================================================
print("\n" + "=" * 72)
print("EXAMPLE 1: Training vs Testing Data")
print("=" * 72)


# Create synthetic data: House price based on size
np.random.seed(42)

X = np.random.rand(300, 1) * 200 + 100 # House sizes: 100 - 300 sq meters
y = X.flatten() * 5000 + np.random.rand(300) * 50000 + 100000 # Price = size * 5000 + noise

print(f"\nDataset: {len(X)} houses")

print(f"House sizes: {X.min():.0f}m2 to {X.max():.0f}m2")
print(f"Prices: ${y.min():,.0f} to ${y.max():,.0f}")

# ❌ WRONG WAY: Test on training data                                                                                                                                                                                 
print("\n" + "-" * 72)
print("WRONG: Testing on Training Data")                                                                                                                                                                              
print("-" * 72) 

model_wrong = LinearRegression()
wrong = model_wrong.fit(X, y)
print(wrong)

y_pred_wrong = model_wrong.predict(X) # Predict same data!
# print(y_pred_wrong)
accuracy_wrong = r2_score(y, y_pred_wrong)
print(f"R2 Score (on training data): {accuracy_wrong:.4f}")

print("This looks GREAT! But it's MISLEADING!")
# ✅ CORRECT WAY: Split first                                                                                                                                                                                        
print("\n" + "-" * 72)                                                                                                                                                                                                  
print("CORRECT: Train/Test Split (80/20)")                                                                                                                                                                            
print("-" * 72) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
print(f"\nTraining set: {len(X_train)} houses (60%)")

print(f"Testing set: {len(X_test)} houses (40%)")

model_correct = LinearRegression()
correct =  model_correct.fit(X_train, y_train)
print(f"Correct x_train, y_train: {correct}")

# Evaluate on different data
y_pred_train = model_correct.predict(X_train)
#print(y_pred_train)
y_pred_test = model_correct.predict(X_test)
# print(y_pred_test)

accuracy_train = r2_score(y_train, y_pred_train)
# print(accuracy_train)
accuracy_test = r2_score(y_test, y_pred_test)
# print(accuracy_test)
print(f"\nR² Score on Training data: {accuracy_train:.4f}")
print(f"R² Score on Testing data:  {accuracy_test:.4f}")                                                                                                                                                              
print("\nNotice: They're similar, which is GOOD!")
print("If test was much lower, the model would be OVERFITTING!")



# ============================================================================                                                                                                                                        
# EXAMPLE 2: Understanding Overfitting                                                                                                                                                                                
# ============================================================================                                                                                                                                        
                                                                                                                                                                                                                      
print("\n" + "=" * 72)
print("EXAMPLE 2: Overfitting vs Underfitting")                                                                                                                                                                       
print("=" * 72)
# Create data with clear pattern but some noise  
X_demo = np.linspace(0, 10, 50).reshape(-1, 1)

y_demo = np.sin(X_demo).flatten() + np.random.randn(50) * 0.2

# print(f"X_demo : {X_demo} and y_demo: {y_demo}")     

#   📊 The ML Workflow (SACRED PROCESS)

#   Every ML project follows this pattern:

#   1. DATA COLLECTION
#      ↓
#   2. DATA CLEANING
#      ↓
#   3. EXPLORATORY ANALYSIS (visualizations!)
#      ↓
#   4. FEATURE ENGINEERING (prepare data for learning)
#      ↓
#   5. CHOOSE ALGORITHM
#      ↓
#   6. TRAIN MODEL (let computer find patterns)
#      ↓
#   7. EVALUATE MODEL (did it learn well?)
#      ↓
#   8. TUNE PARAMETERS (improve performance)
#      ↓
#   9. TEST ON NEW DATA (final verification)
#      ↓
#   10. DEPLOY (use in real world)

#   You already know steps 1-3! ✅ (That's Phase 2!)

#   Now you'll master steps 4-10! 🔥

                                              
print("\n" + "=" * 72)                                                                                                                                                                                                  
print("EXAMPLE 3: Model Evaluation Metrics")                                                                                                                                                                          
print("=" * 72)                                                                                                                                                                                                         
# Use our original model
y_pred = model_correct.predict(X_test)                                                                                                                                                                                
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)                                                                                                                                                                              
rmse = np.sqrt(mse)                                                                                                                                                                                                   
r2 = r2_score(y_test, y_pred)

print(f"\nMetrics on Test Data:")                                                                                                                                                                                     
print(f"\nMean Absolute Error (MAE): ${mae:,.0f}")                                                                                                                                                                    
print(f"  → On average, predictions are off by ${mae:,.0f}")                                                                                                                                                          
print(f"\nMean Squared Error (MSE): {mse:,.0f}")
print(f"  → Penalizes large errors more")                                                                                                                                                                             
print(f"\nRoot Mean Squared Error (RMSE): ${rmse:,.0f}")
print(f"  → Square root of MSE, back to dollars")                                                                                                                                                                     
print(f"\nR² Score: {r2:.4f}")                                                                                                                                                                                        
print(f"  → Model explains {r2*100:.2f}% of price variance")   


# TODO
print("\n" + "="*70)
print("PHASE 3, CHECKPOINT 3.1: Machine Learning Concepts")
print("="*70)
# ============================================================================
# EXAMPLE 1: The Danger of Testing on Training Data
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 1: Training vs Testing Data")
print("="*70)

# Create synthetic data: House prices based on size
np.random.seed(42)

X = np.random.rand(100, 1) * 200 + 100  # House sizes: 100-300 sq meters
y = X.flatten() * 5000 + np.random.randn(100) * 50000 + 100000  # Price = size * 5000 + noise

print(f"\nDataset: {len(X)} houses")
print(f"House sizes: {X.min():.0f}m² to {X.max():.0f}m²")
print(f"Prices: ${y.min():,.0f} to ${y.max():,.0f}")

# ❌ WRONG WAY: Test on training data
print("\n" + "-"*70)
print("WRONG: Testing on Training Data")
print("-"*70)

model_wrong = LinearRegression()
model_wrong.fit(X, y)
y_pred_wrong = model_wrong.predict(X)  # Predict on SAME data!
accuracy_wrong = r2_score(y, y_pred_wrong)

print(f"R² Score (on training data): {accuracy_wrong:.4f}")
print("This looks GREAT! But it's MISLEADING!")

# ✅ CORRECT WAY: Split first
print("\n" + "-"*70)
print("CORRECT: Train/Test Split (80/20)")
print("-"*70)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining set: {len(X_train)} houses (80%)")
print(f"Testing set: {len(X_test)} houses (20%)")

model_correct = LinearRegression()
model_correct.fit(X_train, y_train)

# Evaluate on DIFFERENT data
y_pred_train = model_correct.predict(X_train)
y_pred_test = model_correct.predict(X_test)
accuracy_train = r2_score(y_train, y_pred_train)
accuracy_test = r2_score(y_test, y_pred_test)

print(f"\nR² Score on Training data: {accuracy_train:.4f}")
print(f"R² Score on Testing data:  {accuracy_test:.4f}")
print("\nNotice: They're similar, which is GOOD!")
print("If test was much lower, the model would be OVERFITTING!")

# ============================================================================
# EXAMPLE 2: Understanding Overfitting
# ============================================================================

print("\n" + "="*70)
print("EXAMPLE 2: Overfitting vs Underfitting")
print("="*70)

# Create data with clear pattern but some noise
X_demo = np.linspace(0, 10, 50).reshape(-1, 1)
y_demo = np.sin(X_demo).flatten() + np.random.randn(50) * 0.2
X_train_demo, X_test_demo, y_train_demo, y_test_demo = train_test_split(
    X_demo, y_demo, test_size=0.2, random_state=42
)

print(f"\nDemo dataset: {len(X_demo)} points")
print(f"Pattern: Sine wave with noise")
print(f"Train size: {len(X_train_demo)}, Test size: {len(X_test_demo)}")

# Try different model complexities
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

print("\n" + "-"*70)
print("Testing Different Model Complexities")
print("-"*70)

complexities = [1, 3, 9]
results = []
for degree in complexities:
    # Create polynomial model
    model = Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('lr', LinearRegression())
    ])
    model.fit(X_train_demo, y_train_demo)
    train_score = model.score(X_train_demo, y_train_demo)
    test_score = model.score(X_test_demo, y_test_demo)
    results.append({
        'degree': degree,
        'train': train_score,
        'test': test_score,
        'gap': train_score - test_score
    })
    print(f"\nDegree {degree} polynomial:")
    print(f"  Training R²: {train_score:.4f}")
    print(f"  Testing R²:  {test_score:.4f}")
    print(f"  Overfitting gap: {train_score - test_score:.4f}")

print("\n" + "-"*70)
print("INTERPRETATION:")
print("-"*70)

print("\nDegree 1: Simple (may UNDERFIT)")
print("Degree 3: Balanced (probably JUST RIGHT)")
print("Degree 9: Complex (likely OVERFITTING)")
print("\nNotice how the gap between train and test grows!")

# ============================================================================
# EXAMPLE 3: Key Metrics
# ============================================================================

print("\n" + "="*70)
print("EXAMPLE 3: Model Evaluation Metrics")
print("="*70)

# Use our original model
y_pred = model_correct.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\nMetrics on Test Data:")
print(f"\nMean Absolute Error (MAE): ${mae:,.0f}")
print(f"  → On average, predictions are off by ${mae:,.0f}")
print(f"\nMean Squared Error (MSE): {mse:,.0f}")
print(f"  → Penalizes large errors more")
print(f"\nRoot Mean Squared Error (RMSE): ${rmse:,.0f}")
print(f"  → Square root of MSE, back to dollars")
print(f"\nR² Score: {r2:.4f}")
print(f"  → Model explains {r2*100:.2f}% of price variance")

# ============================================================================
# VISUALIZATION
# ============================================================================
print("\n" + "="*70)
print("Creating visualizations...")
print("="*70)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Training vs Testing Performance
axes[0, 0].scatter(X_train, y_train, alpha=0.5, label='Training data', color='blue')
axes[0, 0].scatter(X_test, y_test, alpha=0.5, label='Testing data', color='red')

X_all = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_pred_all = model_correct.predict(X_all)

axes[0, 0].plot(X_all, y_pred_all, 'g-', linewidth=2, label='Model prediction')
axes[0, 0].set_xlabel('House Size (m²)')
axes[0, 0].set_ylabel('Price ($)')
axes[0, 0].set_title('Training vs Testing Data\n(Notice: model fits BOTH well)')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Overfitting comparison
axes[0, 1].plot([r['degree'] for r in results], [r['train'] for r in results], 'o-', label='Training', linewidth=2)
axes[0, 1].plot([r['degree'] for r in results], [r['test'] for r in results], 's-', label='Testing', linewidth=2)
axes[0, 1].set_xlabel('Model Complexity (Polynomial Degree)')
axes[0, 1].set_ylabel('R² Score')
axes[0, 1].set_title('Overfitting: The Gap Between Train and Test')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)

# Plot 3: Residuals (prediction errors)
residuals = y_test - y_pred
axes[1, 0].scatter(y_pred, residuals, alpha=0.6)
axes[1, 0].axhline(y=0, color='r', linestyle='--', linewidth=2)
axes[1, 0].set_xlabel('Predicted Price ($)')
axes[1, 0].set_ylabel('Residual (Actual - Predicted) ($)')
axes[1, 0].set_title(f'Residuals Plot\n(Good: randomly scattered around 0)')
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Prediction accuracy
axes[1, 1].scatter(y_test, y_pred, alpha=0.6)

min_price, max_price = y_test.min(), y_test.max()

axes[1, 1].plot([min_price, max_price], [min_price, max_price], 'r--', linewidth=2, label='Perfect prediction')
axes[1, 1].set_xlabel('Actual Price ($)')
axes[1, 1].set_ylabel('Predicted Price ($)')
axes[1, 1].set_title(f'Predictions vs Actual\nR² = {r2:.4f}')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/machine_learning/phase_3_fundamentals/ml_1_concepts.png', dpi=150)
plt.close()
print("\n✅ Visualization saved!")

# ============================================================================
# KEY INSIGHTS
# ============================================================================
print("\n" + "="*70)
print("KEY INSIGHTS FROM THIS LESSON")
print("="*70)
print("""
1. TRAIN/TEST SPLIT IS ESSENTIAL
   - Always split data BEFORE training
   - Test on data the model has NEVER seen
   - This reveals true performance
2. OVERFITTING IS THE ENEMY
   - Complex models memorize training data
   - They perform poorly on new data
   - Watch the gap between train and test R²
  3. METRICS TELL THE STORY
     - MAE: Average error (dollars off)
     - RMSE: Penalizes large errors
     - R²: How much variance explained
     - Use ALL of them together!

  4. RESIDUALS REVEAL PATTERNS
     - Should be randomly scattered
     - If they show patterns, model missed something
     - Always visualize residuals!

  5. THE GOAL
     - Generalization: Work well on NEW data
     - Not memorization: Perfect on training data
     - This is the art and science of ML!
  """)

print("\n" + "="*70)
print("✅ Checkpoint 3.1: ML Concepts - FOUNDATION LAID")
print("="*70)
                                                                           
                                       
