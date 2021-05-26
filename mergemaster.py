#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, glob

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import subprocess

from rioxarray.merge import merge_arrays
from rasterio.plot import plotting_extent
import rioxarray as rxr
import xarray as xr
import rasterio
from rasterio.plot import show

from osgeo import gdal
import earthpy as et
from shapely.geometry  import box
from tifffile import imsave
import earthpy.plot as ep


# In[5]:


def clip_merge_raster(boundary_path, 
                orig_raster_folder_path):
    
    import os, glob

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import geopandas as gpd
    import subprocess

    from rioxarray.merge import merge_arrays
    from rasterio.plot import plotting_extent
    import rioxarray as rxr
    import xarray as xr
    import rasterio
    from rasterio.plot import show

    from osgeo import gdal
    import earthpy as et
    from shapely.geometry  import box
    from tifffile import imsave
    import earthpy.plot as ep
    
    """Clip and merge a set of raster files.

    Parameters
    -----------
    boundary_path: string a path to the shp boundary
    orig_raster_folder_path: string a path to the folder containing all geotiff raster files to be merged

    Returns
    -----------
     raster : geotiff 
        A file inside of the original raster folder which replaces the raw data
    """
    
    
    # change directories to folder where raster files are located
    
    os.chdir(orig_raster_folder_path)
    
    # make new folder for future rasters
    
    os.makedirs('clipped-rasters')
    
    # list all geotifs to be opened
    
    orig_clips = glob.glob(os.path.join(str(orig_raster_folder_path), "*.tif"))
    
    # generate number if tifs
    
    num_files = len(orig_clips)
    
    # clip tifs to shp parameter

    for image, i in zip(orig_clips, range(0,num_files)):
        clipped = gdal.Warp(orig_raster_folder_path+'/clipped-rasters'+'/new-clip{}.tif'.format(i), 
        image, 
        cutlineDSName=boundary_path,
        cropToCutline=True,
        dstNodata = 0)
    
    # delete original files
    
    for raster in orig_clips:
        os.remove(raster)
    
    
    


# In[3]:


def raster2masked_xr(raster_path, valid_range=None):
    

    """converts raster to array and masks invalid values.

    Parameters
    -----------
    raster_path: string a path to the shp boundary
    valid_range: takes in a tuple 

    Returns
    -----------
     xr : xarray object 
        xarray with masked values outside valid range
    xr_counts : pandas data frame
        a count of all unique elements, helps locate possible artifacts
    """
    
    # open raster as rxr
    
    xr_object = rxr.open_rasterio(raster_path,
                                 masked=True, 
                                 parse_coordinates=False)
    

    # mask values
    
    if valid_range is not None:
        mask = ((xr_object < valid_range[0]) | (xr_object > valid_range[1]))
        xr_object = xr_object.where(~xr.where(mask, True, False))

    
    # generate data frame of unique values and counts
    
    xr_df = xr_object.to_dataframe(name='unique values')
    
    xr_counts = xr_df.value_counts()


    
    return xr_object, xr_counts
    


# In[ ]:




