# STIDes

# Here you can find a python implementation of the STIDes algorithm

# This project will be updated as soon as new functions for the methods are researched and implemented

# Structure:

  # 1. In the folder methods the basic functionality can be found. From generating the distance Matrix and extract the shifting factors
  #     from two time interval data sets to calculating the similarity using the generated distance Matrix.
  # 2. The settings.py in the Methods folder stores all the used weighting factors as well as some other settings.
  #    So this is the only file to change if you want to change the overlapping distance for example.
  # 3. The STIDes.py in the Main folder is the general STIDes approach using a mode variable (for enabling shifting factors) as well as two time interval data sets to function.


# Next steps (selection):

  # We are working on updates for different methods, e.g. new functions to handle cardinality differences will be added as soon as they are developed.
  # To Speed up the approach while searching within huge amount of data sets, lower and upper bounds for the similarity will be introduced and implemented as soon they are researched.
