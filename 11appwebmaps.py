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

#without the use of feature group (fg)
# map.add_child(folium.Marker(location=[27.676261, 85.303447], popup="Simul's house!", icon=folium.Icon(color='blue')))

fg = folium.FeatureGroup(name="My Map")
#manually add markers on the map one by one (without using loop or fetching data from external source such as json file)
# fg.add_child(folium.Marker(location=[27.676261, 85.303447], popup="Simul's house!", icon=folium.Icon(color='blue')))
# fg.add_child(folium.Marker(location=[27.67783, 85.307118], popup="Ghode's house!", icon=folium.Icon(color='blue')))
for lt,ln,nm,lc,ccases in zip(lat,lon,name,location,coronacases):

    #icon markers
    # fg.add_child(folium.Marker(location=[lt,ln], popup=(nm + "\n" + lc + "\nCorona Cases: " + str(ccases)), icon=folium.Icon(color_producer(ccases))))

    #circular markers
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=7, popup=(nm + "\n" + lc + "\nCorona Cases: " + str(ccases)),
    fill_color=color_producer(ccases), color='grey', fill_opacity=1))

    #Adding polygon layers in the map using .geojson file
    # fg.add_child(folium.GeoJson(data=open('11appwebmaps2world.json','r',encoding='utf-8-sig').read()))

    #Changing color of polygon
    # Note: l = lambda x: x**2
    # l(25)
    # the above two lines will return 25
    # fg.add_child(folium.GeoJson(data=open('11appwebmaps2world.json','r',encoding='utf-8-sig').read(),
    # style_function=lambda x:{'fillColor':'yellow'}))

    # Setting color condition on the polygon
    # note that POP2005 stands fo population of year2005 which is one of the data field in the .geojson file
    # we are changing the color of the countries based on this population
    fg.add_child(folium.GeoJson(data=open('11appwebmaps2world.json','r',encoding='utf-8-sig').read(),
    style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red'}))

map.add_child(fg)
map.save("11appwebmaps1.1.html")
