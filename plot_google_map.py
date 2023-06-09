"""
Plot google map
Author: Will Julstrom, Meng Zhou, Weizhi Deng
Date: 05/26/2023
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt

# Plot google map image (Iowa City, 10km)
cord = [-91.7, -91.43, 41.6, 41.8] # bounding box, minlon, maxlon, minlat, maxlat
level = 14 # zoom in level (https://wiki.openstreetmap.org/wiki/Zoom_levels)
fig = plt.figure()
ax = plt.axes(projection=cimgt.GoogleTiles(style='satellite').crs)
ax.set_extent(cord, crs=ccrs.PlateCarree())
ax.add_image(cimgt.GoogleTiles(style='satellite'),level)
plt.savefig('iowa_city(10km).png', dpi=300) 


# Plot google map image (Iowa City, 1km)
cord = [-91.56, -91.55, 41.64, 41.65] # bounding box, minlon, maxlon, minlat, maxlat
level = 17 # zoom in level (https://wiki.openstreetmap.org/wiki/Zoom_levels)
fig = plt.figure()
ax = plt.axes(projection=cimgt.GoogleTiles(style='satellite').crs)
ax.set_extent(cord, crs=ccrs.PlateCarree())
ax.add_image(cimgt.GoogleTiles(style='satellite'),level)
plt.savefig('iowa_city(1km).png', dpi=300) 

# Plot google map image (Iowa City, 100m)
cord = [-91.553, -91.55, 41.643, 41.646] # bounding box, minlon, maxlon, minlat, maxlat
level = 18 # zoom in level (https://wiki.openstreetmap.org/wiki/Zoom_levels)
fig = plt.figure()
ax = plt.axes(projection=cimgt.GoogleTiles(style='satellite').crs)
ax.set_extent(cord, crs=ccrs.PlateCarree())
ax.add_image(cimgt.GoogleTiles(style='satellite'),level)
plt.savefig('iowa_city(100m).png', dpi=300) 