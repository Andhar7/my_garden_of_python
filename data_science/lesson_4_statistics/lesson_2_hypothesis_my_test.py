

"""
🕉️ Checkpoint 2.3.2: Hypothesis Testing & P-Values 🕉️
=========================================================

The Most Powerful Question in Science:
"Is this result REAL or just random luck?"

This is where statistics meets TRUTH. 💎
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("\n" + "=" * 81)
print("Checkpoint 2.3.2 : Hypothesis Testing & P-Values" )
print("=" * 81)

# ===========================================================================
# Part 1: Understanding the problem
# ===========================================================================

print("\n" + "=" * 81)
print("Part 1: The Fundamental Question")
print("=" * 81)

print("""
SCENARIO: You're testing a new drug for depression.

Group A (with drug): Average mood improvement = 8.5 points
Group B (placebo): Average mood improvement = 7.2 points

DIFFERENCE: 1.3 points

Question: Is this difference REAL or just RANDOM LUCK?

This is where Hypothesis Testing comes in! 🔮
""")

# ============================================================================
# PART 2: HYPOTHESIS TESTING FRAMEWORK
# ============================================================================

print("\n" + "=" * 81)
print("PART 2: The Two Hypotheses")
print("=" * 81)

print("""
🔴 NULL HYPOTHESIS (H₀ - "Nothing happened")
   "The drug has NO effect. The difference is just random."

   H₀: mean(drug) = mean(placebo)
   H₀: The 1.3 point difference is LUCK, not the drug!

🟢 ALTERNATIVE HYPOTHESIS (H₁ - "Something happened!")
   "The drug DOES have an effect. The difference is REAL."

   H₁: mean(drug) ≠ mean(placebo)
   H₁: The 1.3 point difference is because the drug WORKS!

---

YOUR JOB: Use statistics to decide which is true!
""")

# ============================================================================
# PART 3: THE P-VALUE (Most Misunderstood Concept!)
# ============================================================================

print("\n" + "=" * 81)
print("PART 3: What is a P-Value? (The Sacred Knowledge)")
print("=" * 81)

print("""
❌ WRONG DEFINITION:
   "P-value is the probability that my hypothesis is true"

✅ CORRECT DEFINITION:
   "P-value is the probability of seeing THIS result (or more extreme)
    IF the null hypothesis is TRUE"

ANALOGY:
   Imagine flipping a coin 100 times and getting 85 heads.

   Null Hypothesis: "This is a fair coin"

   P-value answers: "If this IS a fair coin, what's the chance
                     I'd get 85+ heads by random luck?"

   Answer: EXTREMELY unlikely (p < 0.0001)

   Conclusion: This probably ISN'T a fair coin!

---

🎯 INTERPRETATION RULES:

p-value < 0.05  → Result is statistically significant ✅
                  Reject the null hypothesis
                  "The drug probably WORKS!"

p-value ≥ 0.05  → Result is NOT statistically significant ❌
                  Fail to reject the null hypothesis
                  "We can't prove the drug works"

""")

# ============================================================================
# PART 4: PRACTICAL EXAMPLE - T-TEST
# ============================================================================

print("\n" + "=" * 81)
print("PART 4: Two-Sample T-Test (Comparing Two Groups)")
print("=" * 81)

# Generate realistic data: Drug vs Placebo
print("\n📊 Creating realistic drug study data...")

# Drug group: slightly better improvement
drug_group = np.random.normal(loc=8.5, scale=2.0, size=50)

# Placebo group: some improvement (placebo effect)
placebo_group = np.random.normal(loc=7.2, scale=2.0, size=50)

print(f"\n🟢 Drug Group (n = 50):")
print("=" * 81)
print(f"   Mean: {np.mean(drug_group):.2f} ")
print(f"   Std Dev: {np.std(drug_group):.2f} ")
print(f"   Min:   {np.min(drug_group):2f},  Max:  {np.max(drug_group):.2f} ")

print(f"\n🔵 Placebo Group (n=50):")
print(f"   Mean: {np.mean(placebo_group):.2f} ")
print(f"   Std Dev: {np.std(placebo_group):.2f} ")
print(f"   Min:   {np.min(placebo_group):2f},  Max:  {np.max(placebo_group):.2f} ")

print(f"\n The Difference in means is: {np.mean(drug_group) - np.mean(placebo_group):.2f}")


# ============================================================================
# PART 5: PERFORM THE T-TEST
# ============================================================================

print("\n" + "="*80)
print("PART 5: Running the T-Test (The Statistical Test)")
print("="*80)

print("\nPerforming Independent Two-Sample T-Test...")

# Perform t-test
t_statistic, p_value = stats.ttest_ind(drug_group, placebo_group)

print(f"\n📊 T-Test Results:")
print(f"   T-Statistic: {t_statistic:.4f}")
print(f"   P-Value: {p_value:.6f}")

# ============================================================================
# PART 6: INTERPRET THE RESULT
# ============================================================================

print("\n" + "=" * 81)
print("Part 6: Interpretation")
print("=" * 81)

print(f"""
🎯 KEY RESULT: p-value = {p_value:.6f}

DECISION:
""")

if p_value < 0.05:
    print(f"✅ p-value ({p_value:.6f}) < 0.05")
    print(f"   → Result is STATISTICALLY SIGNIFICANT!")
    print(f"   → We REJECT the null hypothesis")
    print(f"   → The drug probably WORKS! 🎉")
    print(f"   → There's only a {p_value * 100:.2f}% chance this is random luck")
else:
    print(f"❌ p-value ({p_value:.6f}) ≥ 0.05")
    print(f"   → Result is NOT statistically significant")
    print(f"   → We FAIL TO REJECT the null hypothesis")
    print(f"   → We can't prove the drug works")
    print(f"   → The difference might just be random")


# ============================================================================
# PART 7: VISUALIZE THE T-TEST
# ============================================================================

print("\n" + "=" * 81)
print("Part 7: Creating Visualization")
print("=" * 81)

plt.figure(figsize=(14, 6))

# Plot 1: Box plot comparison
plt.subplot(1, 2, 1)
plt.boxplot([drug_group, placebo_group], label=['Drug', 'Placebo'])
plt.ylabel('Mood Improvement Score')
plt.title('Drug vs Placebo: Box Plot Comparison')
plt.grid(True, alpha=0.3)

# Plot 2: Distributions with means
plt.subplot(1, 2, 2)
plt.hist(drug_group, bins=15, alpha=0.6, label='Drug', color='green', edgecolor='red')
plt.hist(placebo_group, bins=15, alpha=0.6, label='Placebo', color='blue', edgecolor='yellow')
plt.axvline(np.mean(drug_group), color='green', linestyle='--', linewidth=2, label=f'Drug Mean: {np.mean(drug_group):.2f}')
plt.axvline(np.mean(placebo_group), color='blue', linestyle='--', linewidth=2, label=f'Placebo Mean: {np.mean(placebo_group):.2f}')
plt.xlabel('Mood Improvement Score')
plt.ylabel('Frequency')
plt.title('Distribution Comparison')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_4_statistics/hyp_1_ttest.png', dpi=150)
print("✅ Visualization saved: hyp_1_ttest.png")
plt.close()


# ============================================================================
# PART 8: UNDERSTANDING EFFECT SIZE
# ============================================================================

print("\n" + "=" * 81)
print("PART 8: Effect Size (Cohen's d - Practical Significance)")
print("=" * 81)

print("""
P-VALUE tells us: "Is the difference REAL?" (Statistical Significance)
EFFECT SIZE tells us: "How BIG is the difference?" (Practical Significance)

Example:
- P-value = 0.001 (Very significant statistically!)
- Cohen's d = 0.05 (But the actual difference is tiny)

This happens with LARGE samples! 💡
""")

# Calculate Cohen's d
pooled_std = np.sqrt(((len(drug_group) - 1) * np.std(drug_group, ddof=1) ** 2 + 
                      (len(placebo_group) - 1) * np.std(placebo_group, ddof=1) ** 2) / 
                     (len(drug_group) + len(placebo_group) - 2))

cohens_d = (np.mean(drug_group) - np.mean(placebo_group)) / pooled_std

print(f"\n📊 Effect Size (Cohen's d): {cohens_d:.4f}")

if abs(cohens_d) < 2:
   effect_interpretation = 'Small effect!'
elif abs(cohens_d) < 0.5:
   effect_interpretation = 'Small to medium effect'
elif abs(cohens_d) < 0.8:
   effect_interpretation = 'Medium effect'
else:
   effect_interpretation = 'Large effect'

print(f"   Interpretation: {effect_interpretation}")

print(f"""
Remember:
- Cohen's d = 0.2  → Small but real difference
- Cohen's d = 0.5  → Medium difference
- Cohen's d = 0.8  → Large difference

Your effect size: {cohens_d:.4f} ({effect_interpretation})
""")

# ============================================================================
# PART 9: TYPE I AND TYPE II ERRORS
# ============================================================================

print("\n" + "=" * 81)
print("Part 9: The Two Types of Errors (Important!)")
print("=" * 81)

print("""
🚨 TYPE I ERROR (False Positive - "Crying wolf!")
   You claim the drug works (reject H₀)
   But actually, it doesn't (H₀ is true)

   The p-value threshold (0.05) is designed to limit this!
   If you use p < 0.05, you have only 5% chance of Type I error

🚨 TYPE II ERROR (False Negative - "Missing the wolf!")
   You claim the drug doesn't work (fail to reject H₀)
   But actually, it does work (H₁ is true)

   This happens with small samples!
   With n=20, you might miss a real effect

---

THE TRADEOFF:
Make the threshold stricter (p < 0.01) → Reduce Type I error but increase Type II
Make the threshold looser (p < 0.10) → Reduce Type II error but increase Type I

Professional standard: p < 0.05 (good balance)
Medical studies: p < 0.01 (stricter, more certain)
Exploratory research: p < 0.10 (looser, find possibilities)
""")


# ============================================================================
# PART 10: REAL WORLD CAUTION
# ============================================================================

print("\n" + "=" * 81)
print("Part 10: Important Cautions (The Truth About P-Values)")
print("=" * 81)

print("""
⚠️ COMMON MISCONCEPTIONS:

1️⃣ "P-value < 0.05 means there's only 5% chance I'm wrong"
   ❌ WRONG! It's about the probability of the DATA, not your conclusion

2️⃣ "Non-significant result (p > 0.05) means the effect doesn't exist"
   ❌ WRONG! It might exist, but you need more data to detect it

3️⃣ "You should report only p-values"
   ❌ WRONG! Always report effect size, confidence intervals, and sample size

4️⃣ "The smaller the p-value, the bigger the effect"
   ❌ WRONG! Small p-value just means the effect is real, not how big it is

---

✅ THE CORRECT WAY:

1. Report p-value (Is it real?)
2. Report effect size (How big is it?)
3. Report confidence intervals (What's the range?)
4. Report sample size (Did we have enough data?)
5. Check assumptions (Is the test valid?)
""")


# ============================================================================
# PART 11: SAVE YOUR WORK
# ============================================================================

print("\n" + "=" * 81)
print("===Summary===")
print("=" * 81)

summary = f"""
🎯 WHAT YOU LEARNED:

1. ✅ Null Hypothesis (H₀): Assume nothing happened
2. ✅ Alternative Hypothesis (H₁): We want to prove something happened
3. ✅ P-Value: Probability of the data IF null is true
4. ✅ Statistical Significance: p < 0.05 means result is real
5. ✅ Effect Size (Cohen's d): How big is the actual difference?
6. ✅ Type I & II Errors: False positives and false negatives

---

📊 YOUR TEST RESULTS:
   T-Statistic: {t_statistic:.4f}
   P-Value: {p_value:.6f}
   Cohen's d: {cohens_d:.4f}

   Conclusion: {"✅ Drug works!" if p_value < 0.05 else "❌ Not proven"}

---

🔥 NEXT CHECKPOINT:
   Correlation & Causation
   - Can we say drug CAUSED the improvement?
   - Or was it just correlation?
"""

print(summary)

# Save summary to file
with open('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_4_statistics/hyp_summary.txt', 'w') as f:
    f.write(summary)

print("\n✅ CHECKPOINT 2.3.2 COMPLETE!")
print("🙏 Om Namah Shivaya 🕉️")






