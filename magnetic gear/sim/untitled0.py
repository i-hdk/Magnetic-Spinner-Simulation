import re
import csv
import matplotlib.pyplot as plt

# Define the input and output file paths
logfile_path = 'Editor.log'
csvfile_path = 'output.csv'

# Define the regular expression pattern to match the desired lines
pattern = re.compile(r'Time:\s*(-?\d+\.\d+)\s*w1:\s*(-?\d+\.\d+)\s*w2:\s*(-?\d+\.\d+)\s*PE:\s*(-?\d+\.\d+)')

# Open the log file and the CSV file
with open(logfile_path, 'r') as logfile, open(csvfile_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(['Time', 'w1', 'w2','PE'])
    
    # Read the log file line by line
    for line in logfile:
        # Search for the pattern in each line
        match = pattern.search(line)
        if match:
            # Extract the matched groups
            time, w1, w2, PE = match.groups()
            # Write the extracted values to the CSV file
            writer.writerow([time, w1, w2, PE])

# Define the input CSV file path
csvfile_path = 'output.csv'

fig = plt.figure()
plt.figure().clear()
plt.close()

# Initialize lists to store the data
time = []
w1 = []
w2 = []
PE = []
s = []

# Read the CSV file
with open(csvfile_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header row
    next(reader)
    # Read each row and append the values to the respective lists
    for row in reader:
        time.append(float(row[0]))
        w1.append(float(row[1])) #370
        w2.append(float(row[2]))
        PE.append(float(row[3]))
        s.append(float(row[1]) + float(row[2]) )
        

# Plot the data
plt.plot(time, w1, color='red', label='w1')
plt.plot(time, w2, color='blue', label='w2')
#plt.plot(time,PE,color='green', label = 'PE')
#plt.plot(time, s, color='black', label='total momentum')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Angular Velocity vs Time')

# Add a legend
plt.legend()

# Show the plot
plt.show()
