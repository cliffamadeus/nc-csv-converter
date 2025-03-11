import xarray as xr

# Explicitly set the engine to 'netcdf4'
ds = xr.open_dataset("C:/Users/USER/Documents/00/nc-csv-converter/data/1999-2003.nc", engine="netcdf4")

# Print dataset structure
print(ds)
