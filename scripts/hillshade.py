# Python to process DEM hillshade
# GEO 409, Fall 2018
# TastyFreeze


# Specify your geodatabase, output directory, and DEM raster you want to hillshade
geodatabase = "Z:/BoydsGIS/data/rrg_build.gdb"
dem_raster = "dem_lo_res"
out_dir = "Z:/BoydsGIS/data/_sun/"

# Hillshade parameters
azimuth = 90
altitude = 55

# Check contents of database
try:
    arcpy.env.workspace = geodatabase
    arcpy.env.overwriteOutput = True
    rasterList = arcpy.ListRasters()
    print ("Raster: ", rasterList) # Print two different data types at once
except:
    print("Not a valid database")
    
# Resample DEM if needed to speed things up :)
arcpy.Resample_management ("DEM_2016_5ft_clip", dem_raster, 15, "CUBIC")

# Iterate through three values for the azimuth parameter
while azimuth < 271:
    out_raster = out_dir + "hillshade_" + str(azimuth) + ".tif"
    print("Making " + out_raster + " with azimuth value of " + str(azimuth) + "...")
    arcpy.HillShade_3d(dem_raster, out_raster, azimuth, altitude)
    azimuth += 90

print("All done!")