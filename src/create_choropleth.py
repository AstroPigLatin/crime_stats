# Create heatmap
import folium
from folium import plugins
from folium.plugins import HeatMap, MarkerCluster


def create_choropleth(lat, lon, geo, coord_val, max_ind):
    '''function takes in latitude and longitude coordinates of target map, coordinates values of data points, and max index of color intensity  '''
    heatmap = folium.Map([lat, lon], zoom_start=11)
    cluster = MarkerCluster().add_to(heatmap)

    heat = HeatMap(coord_val.values,
                   min_opacity=0.2,
                   max_val=float(max_ind),
                   radius=float(30), blur=20,
                   max_zoom=11)

    heat.add_to(heatmap)

    return heatmap
