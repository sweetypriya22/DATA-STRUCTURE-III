'''
Temperature Extremes Summary
A weather app collects daily temperature readings over a period of time. 
These are stored as a tuple of integers, where each value represents the recorded temperature for a specific day.
Your task is to write a function report_temperature(temps) that:
Identifies the lowest recorded temperature in the tuple
Identifies the highest recorded temperature in the tuple
This function helps summarise temperature extremes, which is useful for analytics dashboards tracking temperature trends.

Input Format
A tuple where each value (int or float) represents the temperature reading for a day. The tuple can contain any number of temperature readings.
'''
# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
temps = literal_eval(input())

def report_temperature(temps):
    # Write your code here
    if temps == ():
        print("No temperature data available")
    else:
        return  (min(temps), max(temps))
 
# Print the output
result = report_temperature(temps)
if result:
    print(result)
