import xarray as xr
import pandas as pd

# Load NetCDF file
nc_file = "D:/00/panpan/data/data_stream-oper_stepType-accum.nc"
ds = xr.open_dataset(nc_file, engine="netcdf4")

# Process data in smaller chunks
time_chunks = ds.valid_time.values[::1000]  # Adjust chunk size as needed

for i, t in enumerate(time_chunks):
    chunk = ds.sel(valid_time=slice(t, time_chunks[min(i+1, len(time_chunks)-1)]))
    df = chunk.to_dataframe().reset_index()
    
    csv_file = f"D:/00/panpan/output/output_chunk_{i}.csv"
    df.to_csv(csv_file, index=False)
    print(f"Saved chunk {i} -> {csv_file}")
