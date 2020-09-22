#Adding layer control in map
import folium
import pandas

# reading data such as lat and lon values from csv file
data = pandas.read_csv("11appwebmaps1.2.csv")
# converting the data(in columns) into lists
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
location = list(data["LOCATION"])
coronacases = list(data["CORONA_CASES"])

def color_producer(cc):
    if cc==0:
        return 'green'
    elif 0<cc<10:
        return 'orange'
    elif 10<cc:
        return 'red'
    else:
        return 'blue'

map = folium.Map(location=[27.675566, 85.305336], zoom_start=16)
#first feature group shows map with corona cases
fg1 = folium.FeatureGroup(name="Corona Map")
for lt,ln,nm,lc,ccases in zip(lat,lon,name,location,coronacases):
    fg1.add_child(folium.Marker(location=[lt,ln], popup=(nm + "\n" + lc + "\nCorona Cases: " + str(ccases)), icon=folium.Icon(color_producer(ccases))))

#second feature group shows colored polygon map based on population
fg2 = folium.FeatureGroup(name="Population Map")
fg2.add_child(folium.GeoJson(data=open('11appwebmaps2world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red'}))

map.add_child(fg1)
map.add_child(fg2)

#code for layer control(choice for selecting either of the two maps or both). always put this code after adding child for feature FeatureGroup
map.add_child(folium.LayerControl())

map.save("12appwebmaps1.html")
