import xarray as xr

# Explicitly set the engine to 'cfgrib' for GRIB files
ds = xr.open_dataset("C:/Users/maxid/Downloads/00/nc-csv-converter/data/2001-2011.grib", engine="cfgrib")

# Print dataset structure
print(ds)
