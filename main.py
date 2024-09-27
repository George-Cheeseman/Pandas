import pandas as pd
import math
import numpy

""" #Task 1
worldPop = pd.read_csv("world_population.csv")

totalPopulation = worldPop["2022 Population"].sum()

print("Total World Population:",totalPopulation) """

""" #Task 2
worldPop = pd.read_csv("world_population.csv")

totalPopulation = worldPop["2022 Population"].sum()
totalCountries = len(worldPop["2022 Population"])

avgPopulation = totalPopulation//totalCountries

print("Average World Population:",avgPopulation) """

""" #Task 3
worldPop = pd.read_csv("world_population.csv")

population = worldPop["2022 Population"]

minPopulation = int(min(population))
maxPopulation = int(max(population))

population25 = population.quantile(0.25)
population50 = population.quantile(0.50)
population75 = population.quantile(0.75)


print("Lowest Population:",minPopulation)
print("Highest Population:",maxPopulation)
print("Median Population:",int(population50))
print("25% Quartile:",int(population25))
print("75% Quartile:",int(population75)) """

"""#Task 4
worldPop = pd.read_csv("world_population.csv")

pd.set_option('display.float_format', '{:.0f}'.format) #Displays numbers with no decimals

population = worldPop[["Country","2022 Population"]]

top10Population = population.nlargest(10,"2022 Population")
print(top10Population.to_string(index=False)) #Prints the result without index on the left """

""" #Task 5
worldPop = pd.read_csv("world_population.csv")

pd.set_option('display.float_format', '{:.0f}'.format) #Displays numbers with no decimals

population = worldPop[["Country","2022 Population"]]

bottom10Population = population.nsmallest(10,"2022 Population")v 
print(bottom10Population.to_string(index=False)) #Prints the result without index on the left """

#Task 6
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

worldPop = pd.read_csv("world_population.csv")

totalPopulation = worldPop["2022 Population"].sum()

worldPop['Percentage Share'] = (worldPop['2022 Population'] / totalPopulation) * 100

print(worldPop[["Country","2022 Population","Percentage Share"]].sort_values("Percentage Share",ascending=False))