# aviris
# ea-2021-final-project-fire-histories-for-hydrologic-modeling

# Project Description

This is a repository for a watersheds and biodiversity project through CU Boulder's Earth Lab. The project aims to produce a classification system for landscapes surrounding a watershed from remote sensing data. The data collected were chemical signatures surrounding the Russian River Watershed in northern California. Using additional topographical maps, we create a reliable method for drawing conclusions about a landscape based on those chemicals. Although this project uses short range flight imaging, the future of chemical analysis lies in satellite technology, which will proliferate the amount of chemical data available. If we can contribute to the advancement of how to aggragate large amounts of chemical data efficiently, this project will be useful for future chemical analysis. The workflow in this repository is initially geared towards piecing together a mosaic of flight images, and ends with k-means clustering, as well as a correspondence analysis. The workflow may be useful to someone who is working with a geometric boundary within linear flight patterns. 

# Workflow

The tools and packages needed to run this workflow include:
* rioxarray
* rasterio
* xarray
* numpy
* matplotlib
* osgeo
* earthpy
* geopandas

At the present moment, we have two separate workflows for plotting, which is reflected by the multitude of tools and packages used. We will eventually stop working with osgeo and numpy. 

Using rioxarray, ten raster files (one chemical at a time) are clipped to the Russian River Watershed boundary and opened as an xarray datatype. Next, the list of xarrays is merged into a larger xarray. The order that the xarrays are read into a plot may determine how well all pixels are represented. We determined the order of xarrays based on dates of flight paths. Currently, we plot each chemical for observational purposes, but this step will be obsolete in the grand scheme. Once all chemicals are represented by xarrays, they are stacked. A geodatabase is also stacked with the chemical data before running k-means. Once k-means clusters the data into several categories, a correspondence analysis is done between functional process zone classification system and our newly created chemical signature classification system. 

# Data Used

1. AVIRIS (Airborne Visible / Infrared Imaging Spectrometer): Ten flight paths over the Russian River Watershed form a whole image of the study area. We have ten rasters for each of the seven chemicals. Many other chemicals can be found in the data; however, they were concluded to be too unreliable for analysis.
2. rr-hu8.tif: this is a boundary of the Russian River Watershed region
3. Geodatabase
4. Topographical map
5. Functional process zones

# Description of Files in this Repository

* Fire-Histories-for-Hydrologic-Modeling.html blog post
* aviris-carbon-rio.ipynb 
    * Using rioxarray library, the notebook takes in Carbon geotif files, clips to boundary, and plots a map of carbon chemical signatures. This notebook processes the raster files as xarrays.
* gdal-nitrogen.ipynb
    * Using GDAL library, the notebook is only used for data processing/clipping and writing new raster files which are smaller and easier to download. The notebook also plots a map of the nitrogen chemical signatures within the boundary. The geotif files in this notebook are processed as numpy arrays. 

*Note 1: No helper scripts are currently required for this repository.
*Note 2: The repository as of 5/19/2021 contains notebooks for chemical layer processing only. Additional steps in the workflow will be completed through Summer 2021, and additional notebooks will be added as they are written to combine and analyze the data. The readme file will be updated accordingly to reflect changes to the repositoryw ith time.
