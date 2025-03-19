# NetCDF to CSV Converter

This script converts **NetCDF (.nc) files** into **CSV (.csv) files**, handling large datasets efficiently by using chunking techniques.

## 📌 Requirements
Ensure you have the following installed:
- Python **3.8+**
- Required Python libraries:
  - `xarray`
  - `pandas`
  - `netCDF4`
  - `dask` (for chunked processing)

### Install Dependencies
Run the following command to install the necessary packages:
```sh
pip install xarray pandas netCDF4 dask
```

---

## 🚀 How to Run the Script
### 1️⃣ Place Your NetCDF File
Move your **.nc file** to the `data/` folder (or any directory you prefer).

### 2️⃣ Update the File Path in the Script
Edit `convert_nc_to_csv.py` and update the file path:
```python
nc_file = "D:/00/panpan/data_stream-oper_stepType-accum.nc"  # Update this path
```

### 3️⃣ Run the Script
Execute the script using:
```sh
python convert_nc_to_csv.py
```

### 4️⃣ Output CSV File
Once the script runs successfully, the CSV file will be saved in the same directory as your NetCDF file.

---

## 🛠 Alternative Approaches
### ✅ Convert Only a Specific Variable
Modify the script to extract only one variable (e.g., `tp`):
```python
df = ds["tp"].to_dataframe().reset_index()
```

### ✅ Handle Large Files with Chunking
If your file is **too large**, use Dask for chunked processing:
```python
ds = xr.open_dataset(nc_file, engine="netcdf4", chunks={'valid_time': 1000})
```

---

## 🔄 Troubleshooting
### ❌ `ModuleNotFoundError: No module named 'xarray'`
Run:
```sh
pip install xarray
```

### ❌ `ValueError: did not find a match in any of xarray's currently installed IO backends`
Ensure you have **netCDF4** installed:
```sh
pip install netCDF4
```

### ❌ `MemoryError`
Try processing in chunks:
```python
import dask.dataframe as dd
ddf = dd.from_pandas(df, npartitions=10)
ddf.to_csv("output.csv", index=False, single_file=True)
```

---

## 📌 Notes
- Works best with **Python 3.8+**
- Designed for large NetCDF datasets
- Supports **memory-efficient chunk processing**
- Added branch for multitasking

---
