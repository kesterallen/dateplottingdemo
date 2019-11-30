"""Simple plot of units allowed per county vs year"""

from collections import defaultdict
import csv
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# Read the data into arrays:
#  years: a list of datetime objects from column 1 of the file
#  units_allowed: a dict of county to units allowed per year from columns 2-4
#
years = []
units_allowed = defaultdict(list)
with open('darrell_demo.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        for county, units in row.items():
            if county == 'year':
                year = dt.datetime.strptime(units, '%Y')
                years.append(year)
            else:
                units_allowed[county].append(float(units))

# Make plot
#
plt.style.use('fivethirtyeight') # Optional plot style
fig, axis = plt.subplots() # create figure and data-axis objects

# Draw the series:
for county, units in units_allowed.items():
    axis.plot(years, units, marker='o', linestyle='--', linewidth=0.9, label=county)

# Legend and axis labels (subtitle's a little tricky)
axis.xaxis.set_major_formatter(mdates.DateFormatter('%Y')) # print only year on x-axis
axis.legend(loc='best') # put the legend in a good place
axis.set_xlabel('Year')
axis.set_ylabel('Units Permitted')
axis.set_title('Bay Area County Housing Production')
plt.suptitle('Units Permitted by County', y=0.88) # hacky subtitle

# Force a fullscreen display, and draw to the screen
plt.get_current_fig_manager().full_screen_toggle()
plt.show()
