import matplotlib.pyplot as plt

# Define the weight (mass) of each planet in the solar system in yottagrams (10^24 kg)
planet_weights = {
    'Mercury': 0.33,
    'Venus': 4.87,
    'Earth': 5.97,
    'Mars': 0.64,
    'Jupiter': 1898,
    'Saturn': 568,
    'Uranus': 86.8,
    'Neptune': 102,
}

# Plotting the weights of the planets
fig, ax = plt.subplots()
ax.bar(planet_weights.keys(), planet_weights.values(), color='skyblue')
ax.set_xlabel('Planet')
ax.set_ylabel('Mass (yottagrams, 10^24 kg)')
ax.set_title('Mass of Planets in the Solar System')

# Display the plot
plt.xticks(rotation=45)
plt.show()
