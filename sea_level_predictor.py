import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(14,6))
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', color='b')

    # Create first line of best fit
    slope, intercept = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[:2]
    years = pd.Series(range(df['Year'].min(), 2051))

    predicted_levels = slope * years + intercept
    plt.plot(years, predicted_levels, label='Best Fit Line', color='r')

    # Create second line of best fit
    recent = df[df['Year'] >= 2000]
    r_slope, r_intercent = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])[:2]

    r_years = pd.Series(range(2000, 2051))
    predicted_recent = r_slope * r_years + r_intercent
    plt.plot(r_years, predicted_recent, label='Best Fit Line(2000-2050)', color='purple')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.xticks(range(1850, 2051, 25))
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()