#AYASHA MARGAUX L. MUSCARA
#8-SAMPAGUITA

import math

# Ask the user to input the needed data
sideA = float(input("Enter the length of side A: "))
sideB = float(input("Enter the length of side B: "))

# Square the values
Asquared = math.pow (sideA, 2)
Bsquared = math.pow (sideB, 2)

# Add the two values
sum = Asquared + Bsquared

# Calculate the hypotenuse
hypotenuse = math.sqrt(sum)

# Round the hypotenuse
hypotenuse = round(hypotenuse, 2)

# Display the result
print("The hypotenuse is:", hypotenuse)