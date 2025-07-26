import xarray as xr

# Explicitly set the engine to 'cfgrib' for GRIB files
ds = xr.open_dataset("C:/Users/USER/Documents/00/nc-csv-converter/data/1994-1998.grib", engine="cfgrib")

# Print dataset structure
print(ds)
