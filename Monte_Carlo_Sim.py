import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Training algorithm
#processing historical data
historic_prices=[14.67,14.73,14.72,14.63,14.6,14.71]
changes=[]
for i in range(len(historic_prices)-1):
    current_period_price=historic_prices[i]
    next_period_price=historic_prices[i+1]
    change=math.log(current_period_price/next_period_price)
    changes.append(change) 
#print(changes)

#Prediction algorithm
MPNXP = 20
num_simulations = 2000
initial_price = 14.70
simulation_matrix = np.empty((MPNXP+1, num_simulations))
e=math.e

simulation_matrix[0, :] = initial_price

for row in range(1, MPNXP+1):
    random_changes = np.random.choice(changes, size=num_simulations)
    simulation_matrix[row, :] = simulation_matrix[row - 1, :] * e**random_changes
medians = np.median(simulation_matrix, axis=1)
    
pd.options.display.float_format = "{:.2f}".format
print(pd.DataFrame(simulation_matrix))
print(pd.DataFrame(medians))



num_rows, num_columns = simulation_matrix.shape
fig, ax = plt.subplots(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0, 1, num_columns))
for col in range(num_columns):
    ax.plot(range(num_rows), simulation_matrix[:, col], label=f'Simulation {col+1}', color=colors[col])
ax.plot(range(num_rows), medians, label='Medians', color='red', linewidth=2)
ax.legend()
ax.set_xlabel('Period')
ax.set_ylabel('Price')
ax.set_title('Line Plot of Each Simulation')
plt.show()
