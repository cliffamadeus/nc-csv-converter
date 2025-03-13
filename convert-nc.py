import xarray as xr
import pandas as pd
import time

# Load NetCDF file
nc_file = "C:/Users/maxid/Downloads/00/nc-csv-converter/data/2015-2024.nc"  # Replace with actual path
ds = xr.open_dataset(nc_file, engine="netcdf4")

# Ensure valid_time is in datetime format
if 'valid_time' in ds.coords:
    ds['valid_time'] = pd.to_datetime(ds['valid_time'])

# Start conversion timer
start_time = time.time()

# Convert the entire dataset to a DataFrame
df = ds.to_dataframe().reset_index()

# Save to CSV
csv_file = "C:/Users/maxid/Downloads/00/nc-csv-converter/output/2015_2024_output.csv"
df.to_csv(csv_file, index=False)

# End conversion timer
end_time = time.time()
print(f"Conversion completed in {((end_time - start_time)/60):.2f} minutes")
print(f"CSV saved at: {csv_file}")
print("Mana ug convert, humot2 na ang toga")
