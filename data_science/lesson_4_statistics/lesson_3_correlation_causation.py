
# TODO
# Main Lesson! 
# Always look for the hidden story!!!
# TODO

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

print("\n" + "=" * 72)
print("Checkpoint 2.3.3: Correlation vs Causation")
print("=" * 72)

# ==========================================================================

# Example 1: The Classic Illusion - Ice Cream & Drowing

# ==========================================================================


print("\n" + "=" * 72)
print("Example 1 : The Fake Correlation")
print("Ice Cream Sales vs Drowing Deaths")
print("=" * 72)

# Create data for 12 months
months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
temperature = np.array([35, 38, 50, 65, 75, 85, 90, 88, 80, 65, 50, 38])

# Ice creame sales Increase in hot months
ice_cream_sales = 100 + (temperature - 35) * 2 + np.random.normal(0, 5, 12)
ice_cream_sales = np.clip(ice_cream_sales, 50, 300)

# Drowning deaths also increase in hot months (swimming season)
drowning_deaths = 5 + (temperature - 35) * 0.3 + np.random.normal(0, 0.5, 12)
drowning_deaths = np.clip(drowning_deaths, 1, 30)

# Calculate correlation
correlation = np.corrcoef(ice_cream_sales, drowning_deaths)[0, 1]

print(f"\nCorrelation between ice cream sales and drowing: {correlation:.4f}")
print(f"\nWould you conclude: 'Ice cream Causes drowning'? ⛔️ ")
print(f"\nThe Truth: Temperature causes Both!")
print(f"- Correlation: Temperature <-> Ice cream sales: {np.corrcoef(temperature, ice_cream_sales)[0, 1]:.4f}")
print(f"- Correlation: Temperature <-> Drowning deaths: {np.corrcoef(temperature, drowning_deaths)[0, 1]:.4f}")

# Visualise the illusion
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Ice cream vs Drowning (the illusion)
axes[0, 0].scatter(ice_cream_sales, drowning_deaths, s=100, alpha=0.6, color='red')
z = np.polyfit(ice_cream_sales, drowning_deaths, 1)

p = np.poly1d(z)

axes[0, 0].plot(ice_cream_sales, p(ice_cream_sales), "r--", linewidth=2)
axes[0, 0].set_xlabel('Ice Cream Sales ($100s)')
axes[0, 0].set_ylabel('Drowning Deaths')
axes[0, 0].set_title(f'The Illusion : Correlation = {correlation:.4f}\n(Ice cream causes drowning? No!)')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Temperature vs Ice Cream (the real cause)
axes[0, 1].scatter(temperature, ice_cream_sales, s=100, alpha=0.6, color='blue')

z = np.polyfit(temperature, ice_cream_sales, 1)
p = np.poly1d(z)

axes[0, 1].plot(temperature, p(temperature), "b--", linewidth=2)
corr_temp_ice = np.corrcoef(temperature, ice_cream_sales)[0, 1]

axes[0, 1].set_xlabel('Temperature (°F)')
axes[0, 1].set_ylabel('Ice Cream Sales ($100s)')
axes[0, 1].set_title(f'Real Cause #1: Correlation = {corr_temp_ice:.4f}\n(Temperature causes ice cream sales)')
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Temperature vs Drowning (the real cause)
axes[1, 0].scatter(temperature, drowning_deaths, s=100, alpha=0.6, color='green')

z = np.polyfit(temperature, drowning_deaths, 1)
p = np.poly1d(z)

axes[1, 0].plot(temperature, p(temperature), "g--", linewidth=2)

corr_temp_drown = np.corrcoef(temperature, drowning_deaths)[0, 1]

axes[1, 0].set_xlabel('Temperature (°F)')
axes[1, 0].set_ylabel('Drowning deaths')
axes[1, 0].set_title(f'Real Cause #2: Correlation = {corr_temp_drown:.4f}\n(Temperature causes drowning)')
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: The Hidden Confounder
axes[1, 1].plot(months, temperature, 'o-', linewidth=2, markersize=8, label='Temperature', color='orange')      
axes[1, 1].set_xlabel('Month')
axes[1, 1].set_ylabel('Temperature (°F)', color='orange')                                                       
axes[1, 1].tick_params(axis='y', labelcolor='orange')
ax2 = axes[1, 1].twinx()                                                                                        
ax2.plot(months, ice_cream_sales, 's--', linewidth=2, markersize=8, label='Ice Cream', color='red')
ax2.plot(months, drowning_deaths * 20, '^--', linewidth=2, markersize=8, label='Drowning (×20)', color='blue')
ax2.set_ylabel('Sales / Deaths')
axes[1, 1].set_title('The HIDDEN CONFOUNDER: Temperature drives both!')                                         
axes[1, 1].legend(loc='upper left')
ax2.legend(loc='upper right')                                                                                   
axes[1, 1].grid(True, alpha=0.3) 


plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_4_statistics/corr_1_ice_drow.png', dpi=150)
plt.close()

print("✅ Visualization saved!!!")
 

print("\n" + "="*70)
print("KEY INSIGHT: The Confounding Variable")
print("="*70)
print("\nTemperature is a CONFOUNDING VARIABLE:")
print("- It affects ice cream sales")
print("- It affects drowning deaths")
print("- It creates a FAKE correlation between the two")
print("\nThis is why we MUST look deeper than correlation!")


















