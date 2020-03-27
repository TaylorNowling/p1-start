import matplotlib.pyplot as plt
import numpy as np
import sys
filename = sys.argv[1]
Material = filename[9:-4]
#filename = "raw-data/glass.raw" 
#filename = "raw-data/aluminum.raw"  
#filename = "raw-data/steel.raw"  
#filename = "raw-data/tungsten.raw"  
#filename = "raw-data/ultem.raw"

print(sys.argv)        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
data = np.loadtxt(filename,skiprows=32,delimiter=',')   #uAttempts to load filename into local variable data.
print(data)
## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!
# plt.plot(xdata,ydata, arguments-to-make-plot-pretty)
Stress = -data[:,3]
Strain = -data[:,7]
plt.plot(Strain, Stress, color='k', linestyle='-', label='square')
plt.xlabel('Strain(%)') # adds x axis label 
plt.ylabel('Stress (Mpa)') # adds y axis label 
plt.title('Stress vs Strain Data of '+ Material) # adds the title for the graph

plt.grid()


## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)
m1,b1=np.polyfit(Strain,Stress,1)
Reg=b1+m1*Strain
linearf=np.poly1d(m1,b1)
plt.plot(Strain,Reg,"g--", linestyle='dashed',label="Linear fit")
plt.savefig(filename+ '.pdf')
print(" Modulus of Elasticicty : " + str(m1) + str(' Mpa'))
plt.show()
## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.



