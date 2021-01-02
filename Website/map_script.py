#Adding layer control in map
import folium
import pandas

# reading data such as lat and lon values from csv file
data = pandas.read_csv("map_data.csv", encoding='latin-1')
# converting the data(in columns) into lists
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
category = list(data["CATEGORY"])
location = list(data["LOCATION"])
contact = list(data["CONTACT"])

def color_producer(catg):
    if catg=="Gym":
        return 'green'
    elif catg=="Momo":
        return 'red'
    else:
        return 'blue'

map = folium.Map(location=[27.673378, 85.317900], zoom_start=16)
#first feature group shows all
fg1 = folium.FeatureGroup(name="All")
for lt,ln,nm,cat,lc,con in zip(lat,lon,name,category,location,contact):
    fg1.add_child(folium.Marker(location=[lt,ln], popup=(nm + "\nCategory: " + cat + "\nContact: " + str(con) + "\nLocation: " + lc), icon=folium.Icon(color_producer(cat))))

#second feature group shows gym
fg2 = folium.FeatureGroup(name="Gym")
for lt,ln,nm,cat,lc,con in zip(lat,lon,name,category,location,contact):
    if(cat=="Gym"):
        fg2.add_child(folium.Marker(location=[lt,ln], popup=(nm + "\nCategory: " + cat + "\nContact: " + str(con) + "\nLocation: " + lc), icon=folium.Icon(color_producer(cat))))

#third feature group shows gym
fg3 = folium.FeatureGroup(name="Momo")
for lt,ln,nm,cat,lc,con in zip(lat,lon,name,category,location,contact):
    if(cat=="Momo"):
        fg3.add_child(folium.Marker(location=[lt,ln], popup=(nm + "\nCategory: " + cat + "\nContact: " + str(con) + "\nLocation: " + lc), icon=folium.Icon(color_producer(cat))))


map.add_child(fg1)
map.add_child(fg2)
map.add_child(fg3)

#code for layer control(choice for selecting either of the two maps or both). always put this code after adding child for feature FeatureGroup
map.add_child(folium.LayerControl())

map.save("map.html")
