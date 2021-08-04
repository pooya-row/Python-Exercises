"""
This script requires the data files be stored at the parent of the current working directory, under a separate
directory called "00_data". This setting can be changes in lines 10 and 11 below.
"""

from pathlib import Path
import bid_update
import forecast

bid_update_file = str(Path.cwd().parent / "00_data" / "Bid-Update.json")
forecast_file = str(Path.cwd().parent / "00_data" / "Forecast.json")

bid_update_df = bid_update.bid_update_data(bid_update_file)
forecast_df = forecast.forecast_data(forecast_file)

global mean_per_hr
means_collector = []
for d, t in zip(bid_update_df['Date'], bid_update_df['Time']):
    mean_per_hr = forecast_df[(forecast_df['Date'] == d) & (forecast_df['hr'] == t.hour)] \
        .groupby('Topology Element ID').mean()

    means_collector.append(list(mean_per_hr['Value']))

bid_update_df[list(mean_per_hr.index)] = means_collector

bid_update_df.columns = ['Start Time', 'Max Dispatch Sum', 'Load Reduction', 'Reference Load',
                         'Date', 'Time', 'Bid-update - GBESS', 'Bid-update - RBESS',
                         'Bid-update - waste water treatment',
                         'Bid-update - Sewage pump', 'PV', 'Hydro', 'Forecast - Waste Water Treatment',
                         'Forecast - Sewage Pump', 'Feeder-net']

bid_update_df[['Start Time', 'Feeder-net', 'PV', 'Hydro', 'Forecast - Waste Water Treatment',
               'Forecast - Sewage Pump', 'Reference Load', 'Load Reduction', 'Max Dispatch Sum',
               'Bid-update - GBESS', 'Bid-update - RBESS', 'Bid-update - waste water treatment',
               'Bid-update - Sewage pump']] \
    .to_csv('Summary.csv', index=False, index_label=True)
