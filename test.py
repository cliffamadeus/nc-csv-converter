import xarray as xr

# Explicitly set the engine to 'netcdf4'
ds = xr.open_dataset("D:/00/panpan/data_stream-oper_stepType-accum.nc", engine="netcdf4")

# Print dataset structure
print(ds)
