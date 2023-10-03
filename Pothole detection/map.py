# import folium package
import folium

# Map method of folium return Map object

# Here we pass coordinates of Gfg
# and starting Zoom level = 12
location_pot = [18.627702, 73.806515]
my_map1 = folium.Map(location=location_pot,
                     zoom_start=16)

# save method of Map object will create a map
my_map1.save(" my_map1.html ")