#01.Libraries
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d


#02. Dataset
data = {
    'Timestamp': ['2023-07-01 00:00', '2023-07-02 00:00', '2023-07-04 00:00', '2023-07-06 00:00'],
    'Value': [10, 20, np.nan, 40]
}

#03.DataSet --> DataFrame
df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Sorting the DataFrame by timestamp
df.sort_values('Timestamp', inplace=True)

# Creating an interpolation function using linear interpolation
interpolation_func = interp1d(df['Timestamp'], df['Value'], kind='linear', fill_value='extrapolate')

# Generating a new timestamp range for interpolation
start_date = df['Timestamp'].min()
end_date = df['Timestamp'].max()
interpolated_timestamps = pd.date_range(start=start_date, end=end_date, freq='D')

# Applying interpolation function to fill missing values
interpolated_values = interpolation_func(interpolated_timestamps)

# Creating a new DataFrame with interpolated data
interpolated_df = pd.DataFrame({'Timestamp': interpolated_timestamps, 'Value': interpolated_values})

# Merging the original DataFrame and interpolated DataFrame
merged_df = pd.merge(df, interpolated_df, on='Timestamp', how='right')




import matplotlib.pyplot as plt

plt.plot(merged_df['Timestamp'], merged_df['Value_x'], 'o', label='Original Data')
plt.plot(merged_df['Timestamp'], merged_df['Value_y'], '-', label='Interpolated Data')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Interpolation of Missing Data in Time Series')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()