import xarray as xr
import pandas as pd
import time

# Load NetCDF file
nc_file = "C:/Users/USER/Documents/00/nc-csv-converter/data/2004-2008.nc"  # Replace with actual path
ds = xr.open_dataset(nc_file, engine="netcdf4")

# Process data in smaller chunks
time_chunks = ds.valid_time.values[::1000]  # Adjust chunk size as needed

total_start_time = time.time()

for i, t in enumerate(time_chunks):
    chunk_start_time = time.time()
    chunk = ds.sel(valid_time=slice(t, time_chunks[min(i+1, len(time_chunks)-1)]))
    df = chunk.to_dataframe().reset_index()
    
    csv_file = f"C:/Users/USER/Documents/00/nc-csv-converter/output/2004-2008/2004_2008_output_chunk_{i}.csv"  # Replace with actual path
    df.to_csv(csv_file, index=False)
    
    chunk_end_time = time.time()
    print(f"Saved chunk {i} -> {csv_file} (Time elapsed: {chunk_end_time - chunk_start_time:.2f} seconds)")

total_end_time = time.time()
print(f"Total conversion time: {total_end_time - total_start_time:.2f} seconds")