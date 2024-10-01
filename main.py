import pandas as pd
import math
import numpy
import matplotlib.pyplot as plt

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

""" 
#Task 6
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

worldPop = pd.read_csv("world_population.csv")

totalPopulation = worldPop["2022 Population"].sum()

worldPop['Percentage Share'] = (worldPop['2022 Population'] / totalPopulation) * 100

print(worldPop[["Country","2022 Population","Percentage Share"]].sort_values("Percentage Share",ascending=False)) """

""" #Task 7
pd.set_option('display.float_format', '{:.0f}'.format) #Displays numbers with no decimals

worldPop = pd.read_csv("world_population.csv")

population_per_continent = worldPop.groupby('Continent')['2022 Population'].sum()

print(population_per_continent) """

""" #Task 8
pd.set_option('display.float_format', '{:.0f}'.format) #Displays numbers with no decimals

worldPop = pd.read_csv("world_population.csv")

worldPop["Population Density"] = (worldPop["2022 Population"] // worldPop["Area (km²)"])

print(worldPop[["Country","2022 Population","Area (km²)","Population Density"]]) """

""" #Task 10
pd.set_option('display.float_format', '{:.0f}'.format) #Displays numbers with no decimals

worldPop = pd.read_csv("world_population.csv")

worldPop["Population Growth (per year)"] =  ((worldPop["2022 Population"] - worldPop["2020 Population"]) // 2)

print(worldPop[["Country","Population Growth (per year)"]]) """

""" #Task 11
pd.set_option('display.float_format', '{:.0f}'.format) #Displays numbers with no decimals

worldPop = pd.read_csv("world_population.csv")

worldPop["Population Growth (per year)"] =  ((worldPop["2022 Population"] - worldPop["2020 Population"]) // 2)

growthRates = worldPop[["Country","Population Growth (per year)"]]

print(growthRates.nlargest(10,"Population Growth (per year)")) """

""" #Task 12
pd.set_option('display.float_format', '{:.0f}'.format) #Displays numbers with no decimals

worldPop = pd.read_csv("world_population.csv")

worldPop["Population Growth (per year)"] =  ((worldPop["2022 Population"] - worldPop["2020 Population"]) // 2)

growthRates = worldPop[["Country","Population Growth (per year)"]]

decreasingPopulations = worldPop[worldPop["Population Growth (per year)"] < 0][["Country", "Population Growth (per year)"]].sort_values("Population Growth (per year)")

print(decreasingPopulations) """

#Task 12
pd.set_option('display.float_format', '{:.0f}'.format) #Displays numbers with no decimals

worldPop = pd.read_csv("world_population.csv")

top_10_population = worldPop[["Country","2022 Population"]].nlargest(10,"2022 Population")

top_10_population.plot(kind="bar",x="Country",y="2022 Population")

plt.show()