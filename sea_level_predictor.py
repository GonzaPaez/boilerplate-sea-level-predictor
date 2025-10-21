import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.arange(df['Year'].min(), 2051)
    y = line.slope * x + line.intercept
    ax.plot(x, y, color='red')

    # Create second line of best fit
    line_2000 = linregress(
        df[df['Year'] >= 2000]['Year'],
        df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    )
    x_2000 = np.arange(2000, 2051)
    y_2000 = line_2000.slope * x_2000 + line_2000.intercept
    ax.plot(x_2000, y_2000, color='green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()