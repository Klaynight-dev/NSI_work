from gmplot import GoogleMapPlotter
from random import random

# We subclass this just to change the map type
class CustomGoogleMapPlotter(GoogleMapPlotter):
    def __init__(self, center_lat, center_lng, zoom, apikey='',
                 map_type='satellite'):
        super().__init__(center_lat, center_lng, zoom, apikey)

        self.map_type = map_type
        assert(self.map_type in ['roadmap', 'satellite', 'hybrid', 'terrain'])

    def write_map(self,  f):
        f.write('\t\tvar centerlatlng = new google.maps.LatLng(%f, %f);\n' %
                (self.center[0], self.center[1]))
        f.write('\t\tvar myOptions = {\n')
        f.write('\t\t\tzoom: %d,\n' % (self.zoom))
        f.write('\t\t\tcenter: centerlatlng,\n')

        # This is the only line we change
        f.write('\t\t\tmapTypeId: \'{}\'\n'.format(self.map_type))


        f.write('\t\t};\n')
        f.write(
            '\t\tvar map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);\n')
        f.write('\n')

initial_zoom = 16
num_pts = 40

lats = [37.428]
lons = [-122.145]
for pt in range(num_pts):
    lats.append(lats[-1] + (random() - 0.5)/100)
    lons.append(lons[-1] + random()/100)
gmap = CustomGoogleMapPlotter(lats[0], lons[0], initial_zoom,
                              map_type='satellite')
gmap.plot(lats, lons, 'cornflowerblue', edge_width=10)

gmap.draw("mymap.html")