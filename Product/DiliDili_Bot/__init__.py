import matplotlib.pyplot as plt
import numpy as np

# Set up the figure
plt.figure(figsize=(8, 6))

# Define data for supply and demand curves
quantity = np.linspace(0, 100, 100)
demand = 100 - quantity  # D_dom: downward sloping
supply_domestic = 20 + 0.5 * quantity  # S_dom: upward sloping
supply_world = 30 * np.ones_like(quantity)  # S_world: horizontal
supply_world_tariff = 50 * np.ones_like(quantity)  # S_world + tariff

# Plot the curves
plt.plot(quantity, demand, label='D_dom', color='blue')
plt.plot(quantity, supply_domestic, label='S_dom', color='red')
plt.plot(quantity, supply_world, label='S_world', color='green', linestyle='--')
plt.plot(quantity, supply_world_tariff, label='S_world + Tariff', color='orange')

# Equilibrium points
plt.axvline(x=50, ymin=0, ymax=0.5, color='black', linestyle=':', alpha=0.5)  # Q1
plt.axvline(x=70, ymin=0, ymax=0.3, color='black', linestyle=':', alpha=0.5)  # Q_free
plt.axhline(y=50, xmin=0, xmax=0.5, color='black', linestyle=':', alpha=0.5)  # P1
plt.axhline(y=30, xmin=0, xmax=0.7, color='black', linestyle=':', alpha=0.5)  # P_world

# Calculate intersection points for DWL
# S_dom at P_world (30): 20 + 0.5Q = 30 => Q = 20
q_dom = 20  # Where S_dom intersects S_world
p_dom_at_q_dom = 30  # S_dom at Q=20
# D_dom at Q1 (50): 100 - 50 = 50 (already P1)
# D_dom at Q_free (70): 100 - 70 = 30 (already P_world)

# DWL1: Production inefficiency (S_dom to S_world, Q_dom to Q1)
plt.fill([20, 50, 50, 20], [30, 50, 30, 30], color='gray', alpha=0.3, label='Deadweight Loss')
# DWL2: Consumption inefficiency (D_dom to S_world, Q1 to Q_free)
plt.fill([50, 70, 70, 50], [50, 30, 30, 50], color='gray', alpha=0.3)

# Labels and annotations
plt.text(50, 55, 'P1', horizontalalignment='center')
plt.text(70, 35, 'P_world', horizontalalignment='center')
plt.text(50, 10, 'Q1', verticalalignment='center')
plt.text(70, 10, 'Q_free', verticalalignment='center')
plt.text(35, 35, 'DWL1', horizontalalignment='center', alpha=0.7)  # Production DWL
plt.text(60, 35, 'DWL2', horizontalalignment='center', alpha=0.7)  # Consumption DWL

# Axes and title (no numbers)
plt.xlabel('Quantity of EV Components')
plt.ylabel('Price')
plt.title('Figure 1: Tariff Impact on Serbia’s EV Component Market Pre-FTA')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks([])  # Remove x-axis numbers
plt.yticks([])  # Remove y-axis numbers

# Caption
plt.figtext(0.5, -0.05, 'Figure Caption: Tariffs raise prices and limit imports.',
            wrap=True, horizontalalignment='center', fontsize=10)

# Show plot
plt.tight_layout()
plt.show()