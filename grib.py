import xarray as xr
import pandas as pd
import time

# Load GRIB file
grib_file = "C:/Users/maxid/Downloads/00/nc-csv-converter/data/2001-2011.grib"

# Open dataset with cfgrib
ds = xr.open_dataset(grib_file, engine="cfgrib", backend_kwargs={'indexpath': ''}, decode_timedelta=True)

# Identify the correct time coordinate
time_var = 'valid_time' if 'valid_time' in ds.coords else list(ds.coords.keys())[0]
ds[time_var] = pd.to_datetime(ds[time_var])  # Ensure datetime format

# Flatten the dataset before converting to DataFrame
df = ds.stack(z=("latitude", "longitude")).to_dataframe().reset_index()  # Flatten spatial dimensions

# Save to CSV
csv_file = "C:/Users/maxid/Downloads/00/nc-csv-converter/output/2001_2011_output.csv"
df.to_csv(csv_file, index=False)

print(f"Conversion completed. CSV saved at: {csv_file}")
print("Mana ug convert, humot2 na ang toga")
