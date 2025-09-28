#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

# Libraries used for slow print
import sys
import time

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Big Hero 6"


def print_slow(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.05)
  print()


print_slow("My favorite movie is " + favMovie)

#Part 3 Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])

#Part 4 Filter data
print_slow("\nThe data for my favorite movie is:\n")

#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
#print(favMovieBooleanList)

favMovieData = movieData.loc[favMovieBooleanList]
print_slow(str(favMovieData) + "\n")

#Create a new variable to store a new data set with a certain genre
animationMovieBooleanList = movieData["genres"].str.contains("Animation")
animationMovieData = movieData.loc[animationMovieBooleanList]

numOfMovies = animationMovieData.shape[0]

print_slow("We will be comparing " + favMovie +
           " to other movies under the genre Animation in the data set.\n")
print_slow("There are " + str(numOfMovies) +
           " movies under the category Animation.")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print_slow("Press enter to see more information about how " + favMovie +
           " compares to other movies in this genre.\n")
input()

#Part 5 Describe data
#This variable will be used for comparison
movieRating = int(favMovieData["audience_rating"])
animationRatings = animationMovieData["audience_rating"]

#min
min = animationRatings.min()
print_slow("The min audience rating of the data set is: " + str(min))

minDiff = movieRating - min

print_slow(favMovie + " is rated " + str(minDiff) +
           " points higher than the lowest rated movie.\n")

#find max
max = animationRatings.max()
print_slow("The max audience rating of the data set is: " + str(max))

maxDiff = int(max - movieRating)

print_slow(favMovie + " is rated " + str(maxDiff) +
           " points lower than the highest rated movie.\n")

#function to compare mean and median
comparison = ""


def compare(movie, data):
  global comparison
  if movie < data:
    comparison = "lower than"
  elif movie > data:
    comparison = "higher than"
  else:
    comparison = "the same as"


#find mean
mean = animationRatings.mean()
print_slow("The mean audience rating of the data set is: " + str(mean))

compare(movieRating, mean)

print_slow(favMovie + " is " + comparison + " the mean movie rating.")

#find median
median = animationRatings.median()
print_slow("The median audience rating of the data set is: " + str(median))

compare(movieRating, mean)

print_slow(favMovie + " is " + comparison + " the median movie rating.")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print_slow("Press enter to see data visualizations.")
input()

#Part 6 Create graphs
#Create histogram
plt.rcParams['toolbar'] = 'None'
plt.hist(animationRatings, range=(0, 100), bins=20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Animation Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Animation Movies")

plt.show(block=False)
plt.pause(1)

#Prints interpretation of histogram
print_slow(
    "Click the square on the top right corner to fit the graph to the screen.\n"
)
print_slow("Press enter to see the interpretation of the histogram.")
input()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

print_slow(
    "According to the histogram, the mode (or the audience rating that appears the most) is between 75 to 80. The data appears to skew left with no outliers.\n"
)

print_slow("Close the graph by pressing the 'X' in the top right corner.\n")

plt.show()

#Create scatterplot
plt.rcParams['toolbar'] = 'None'
plt.scatter(data=animationMovieData,
            x="audience_rating",
            y="critic_rating",
            label="Animation Movies")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating versus Critic Rating in Animation Movies")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Plots favorite movie
plt.scatter(data=favMovieData,
            x="audience_rating",
            y="critic_rating",
            label="favMovie")
plt.legend()

plt.show(block=False)
plt.pause(1)

#Prints interpretation of scatterplot
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print_slow(
    "Click the square on the top right corner to fit the graph to the screen.\n"
)
print_slow("Press enter to see the interpretation of the scatter plot.")
input()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

print_slow(
    "According to the scatter plot, there is a moderate positive correlation with no outliers."
)
print_slow(
    favMovie +
    " follows the overall pattern of the plot. The audience rating and critic rating appears to be similar.\n"
)

print_slow("Close the graph by pressing the 'X' in the top right corner.")

plt.show()

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

print_slow("Thank you for reading through my data analysis!")
