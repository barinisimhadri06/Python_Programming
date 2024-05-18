# Author: Barini Simhadri
# Date: 21-03-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/i3i4QiX1MbA

import math
import random
import matplotlib.pyplot as plt

class Planet:
    """Class to represent a planet in the solar system."""

    def __init__(self, radius, year_length):
        """
        This function Initialize a planet object with its radius and year length.
        """
        self.radius = radius
        self.year_length = year_length

    def position(self, day):
        """
        this function Calculates the position of the planet on a specific day.
        """
        # Calculate angle
        angle = 2 * math.pi * day / self.year_length
        # Calculate x and y coordinates using trigonometry
        x = self.radius * math.cos(angle)
        y = self.radius * math.sin(angle)
        return x, y

def distance(planet1, planet2, day):
    """
    it calculates the Euclidean distance between two planets on a specific day.
    """
    x1, y1 = planet1.position(day)
    x2, y2 = planet2.position(day)
    # Euclidean distance formula
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def generate_noisy_distance(planet1, planet2, day, std):
    """
    Generate a noisy version of the distance between two planets on a specific day.
    """
    true_dist = distance(planet1, planet2, day)
    # Add noise to the true distance
    noisy_dist = true_dist + random.gauss(0, std)
    return noisy_dist

def simulate(days, std):
    """
    it Simulate the distances between Earth and other planets over a certain number of days.
    """
    # Create planet objects
    earth = Planet(9.3, 365)
    mercury = Planet(3.5, 88)
    venus = Planet(6.7, 225)
    mars = Planet(14.2, 687)

    # Lists to store distances
    earth_mercury_distances = []
    earth_venus_distances = []
    earth_mars_distances = []

    for day in range(days):
        # Generate noisy distances
        earth_mercury_dist = generate_noisy_distance(earth, mercury, day, std)
        earth_venus_dist = generate_noisy_distance(earth, venus, day, std)
        earth_mars_dist = generate_noisy_distance(earth, mars, day, std)

        # Append distances to lists
        earth_mercury_distances.append(earth_mercury_dist)
        earth_venus_distances.append(earth_venus_dist)
        earth_mars_distances.append(earth_mars_dist)

    # Plotting
    plt.plot(range(days), earth_mercury_distances, label='Earth-Mercury')
    plt.plot(range(days), earth_venus_distances, label='Earth-Venus')
    plt.plot(range(days), earth_mars_distances, label='Earth-Mars')

    # Plotting average distances as horizontal lines
    plt.axhline(y=sum(earth_mercury_distances)/len(earth_mercury_distances), color='blue', linestyle='--', label='Avg Earth-Mercury')
    plt.axhline(y=sum(earth_venus_distances)/len(earth_venus_distances), color='orange', linestyle='--', label='Avg Earth-Venus')
    plt.axhline(y=sum(earth_mars_distances)/len(earth_mars_distances), color='green', linestyle='--', label='Avg Earth-Mars')

    plt.xlabel('Days')
    plt.ylabel('Distance')
    plt.legend()
    plt.title('Distances between Earth and Planets over Time')
    plt.show()

    # Return the average distances for further analysis
    return (
        sum(earth_mercury_distances)/len(earth_mercury_distances),
        sum(earth_venus_distances)/len(earth_venus_distances),
        sum(earth_mars_distances)/len(earth_mars_distances)
    )

def generate_1000_year_simulation():
    """
    this Generate a 1000-year simulation and compute the average daily distances for all pairs of planets.
    Prints an 8x8 array showing the average distance between all pairs of planets.
    """
    num_simulations = 1000
    total_distances = {
        'Mercury': 0,
        'Venus': 0,
        'Mars': 0
    }

    # Simulate 1000 years
    for _ in range(num_simulations):
        distances = simulate(365, 0)  # Run simulation for 365 days (1 year)
        # Accumulate distances
        total_distances['Mercury'] += distances[0]
        total_distances['Venus'] += distances[1]
        total_distances['Mars'] += distances[2]

    # Calculate average distances
    for planet, total_distance in total_distances.items():
        total_distances[planet] = total_distance / num_simulations

    # Print the 8x8 matrix
    print("Average distances between planets (in CM):")
    for planet1, dist1 in total_distances.items():
        row = []
        for planet2, dist2 in total_distances.items():
            # Calculate the average distance between planet1 and planet2
            avg_dist = (dist1 + dist2) / 2
            row.append(avg_dist)
        print(row)

    # Find the planet closest to Earth on average
    closest_planet = min(total_distances, key=total_distances.get)
    print(f"\nPlanet closest to Earth on average: {closest_planet}")

#Distance between Earth and Mars on day 732
earth = Planet(9.3, 365)
mars = Planet(14.2, 687)
distance_732 = distance(earth, mars, 732)
print(f"Distance between Earth and Mars on day 732: {distance_732:.2f}")

# simulation
simulate(1000, 0.5)

# 1000-year simulation
generate_100