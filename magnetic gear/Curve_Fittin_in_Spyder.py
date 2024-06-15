import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

plt.close('all')

# Load data
data = np.genfromtxt('forcedata(2cm).csv', delimiter=',')
data = data[1:, :]
x = data[:,   0]
y = data[:,   1]

# Plot original data
plt.figure()
plt.scatter(x, y, color='red', label='Data')

# Define the model function
def fcn(x, a,b,d):
    return a* (x)**b+d

# Initial guess for parameters
initial_guess = (-0.3,-1,0)  # Adjust this if necessary

# Perform curve fitting with bounds and initial guess
popt, pcov = op.curve_fit(fcn, x, y, p0=initial_guess)


# Calculate errors
err = np.sqrt(np.diag(pcov))

# Generate x values for plotting
xx = np.linspace(0.1, x.max(),   100)



# Plot fitted curve
plt.plot(xx, fcn(xx, *popt) , 'b-')#, label='Fit: a=%5.3f, b=%5.3f b=%5.3f' % tuple(popt))

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Display the plot
plt.show()

# Print the optimized parameters and their uncertainties
print("Optimized parameters: ", popt)
print("Uncertainties: ", err)