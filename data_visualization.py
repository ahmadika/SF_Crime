import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium


def readFile(train_path):
    train=pd.read_csv(train_path)
    train.dropna()
    return train

def histVisualize(train, name):
    sns.countplot(x=name, data=train)
    plt.show()

def violinPlot(train, x, y):
    pkmn_type_colors = ['#78C850',  # Grass
                        '#F08030',  # Fire
                        '#6890F0',  # Water
                        '#A8B820',  # Bug
                        '#A8A878',  # Normal
                        '#A040A0',  # Poison
                        '#F8D030',  # Electric
                        '#E0C068',  # Ground
                        '#EE99AC',  # Fairy
                        '#C03028',  # Fighting
                        '#F85888',  # Psychic
                        '#B8A038',  # Rock
                        '#705898',  # Ghost
                        '#98D8D8',  # Ice
                        '#7038F8',  # Dragon
                        ]
    sns.violinplot(x=x, y=y, data=train, palette=pkmn_type_colors)
    plt.show()

def mapVisualize(train, x, y):
    sfCoordinate = (37.76, -122.45)

    #maximum number of crimes to display
    maxCrimes = 100
    sfMap = folium.Map(location=sfCoordinate, zoom_start=12)
    for each in train[0:maxCrimes].iterrows():
        folium.Marker([each[1]['Y'], each[1]['X']], popup=each[1]['Category']).add_to(sfMap)
    sfMap.save("map.html")

def summary(train):
    categories = train.Category.value_counts()
    categories.plot.bar()
    for index, row in categories.iteritems():
        print ("{"+'"name"'+":" +'"'+str(index)+'"' +","+ " "+'"'+"size"+'"'+":"+ str(row) +"},")
    plt.show()

def main():
    train = readFile('data/train.csv')
    summary(train)

    #Which day is most dangerous
    histVisualize(train,"DayOfWeek")

    #which hour is most dangerous to be out
    train["Dates"] = pd.to_datetime(train["Dates"])
    train["hours"] = train["Dates"].dt.hour
    histVisualize(train, "hours")

    # plotting dangerous hours for each day
    violinPlot(train, "DayOfWeek", "hours")

    # showing crime locations on map
    mapVisualize(train,"X","Y")

if __name__=="__main__":
    main()
