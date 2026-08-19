

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

from data_science.lesson_4_statistics.lesson_2_hypothesis_testing import drug_group

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























