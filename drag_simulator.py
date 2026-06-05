import numpy as np
import matplotlib.pyplot as plt

# Car ke values
rho = 1.225        # Hawa ki density (kg/m³)
A = 2.2            # Car ka frontal area (m²)

# Normal car vs Graphene coated car
Cd_normal = 0.33   # Normal supercar
Cd_graphene = 0.27 # Graphene nanocoated car

# Speed range: 0 se 350 km/h
speed_kmh = np.linspace(0, 350, 100)
speed_ms = speed_kmh / 3.6  # km/h to m/s convert

# Drag force calculate karo
F_normal = 0.5 * rho * speed_ms**2 * Cd_normal * A
F_graphene = 0.5 * rho * speed_ms**2 * Cd_graphene * A

# Graph banao
plt.figure(figsize=(10, 6))
plt.plot(speed_kmh, F_normal, color='red', label='Normal Car (Cd=0.33)')
plt.plot(speed_kmh, F_graphene, color='blue', label='Graphene Coated (Cd=0.27)')
plt.xlabel('Speed (km/h)')
plt.ylabel('Drag Force (Newtons)')
plt.title('Supercar Drag Force: Normal vs Graphene Nanocoated')
plt.legend()
plt.grid(True)
plt.show()