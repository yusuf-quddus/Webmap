import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 2000:
        return 'green'
    elif 2000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=3, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="vocanoes")

for lt, ln, el in zip(lat, lon, elev): 
    fgv.add_child(folium.Marker(location=[lt, ln], popup = str(el) + " meters", icon = folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 30000000 else 'orange'
if 30000000 <= x['properties']['POP2005'] < 90000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("Map1.html")
