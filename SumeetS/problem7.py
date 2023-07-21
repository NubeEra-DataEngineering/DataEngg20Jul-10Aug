import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt

data = {
    'Timestamp': ['2023-07-01 00:00', '2023-07-02 00:00', '2023-07-04 00:00', '2023-07-06 00:00'],
    'Value': [10, 20, np.nan, 40]
}

df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df.sort_values('Timestamp', inplace=True)

f = interp1d(df['Timestamp'], df['Value'], kind='linear', fill_value='extrapolate')

start_date = df['Timestamp'].min()
end_date = df['Timestamp'].max()
interpolated_daterange = pd.date_range(start=start_date, end=end_date, freq='D')

interpolated_values = f(interpolated_daterange)

interpolated_df = pd.DataFrame({'Timestamp': interpolated_daterange,
                   'Value': interpolated_values})

merged_df = df.merge(df, interpolated_df, on='Timestamp', how='right')
print(merged_df)

# plt.plot()
# plt.savefig('SumeetS/timestamp.png')