import pandas as pd
import json
import datetime


def bid_update_data(file_path: str) -> pd.DataFrame:
    """
    Convert contents of `file_path` json file into a pandas dataframe and perform summation of max dispatch over all
    assets for each given start time.

    :param file_path: string or Path object
    :return: dataframe containing start time and hourly max dispatch summation over all assets
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    max_dispatch = [0] * len(data['data']['assets'][0]['maximum_dispatch_schedule'])
    for t, _ in enumerate(data['data']['assets'][0]['maximum_dispatch_schedule']):
        for ast_num, _ in enumerate(data['data']['assets']):
            max_dispatch[t] += data['data']['assets'][ast_num]['maximum_dispatch_schedule'][t][
                'maximum_dispatch']

    load_reduction = []
    reference_load = []
    start_time = []

    for _, dct in enumerate(data['data']['meter_point_schedule']):
        load_reduction.append(dct['load_reduction'])
        reference_load.append(dct['reference_load'])
        start_time.append(datetime.datetime.fromisoformat(dct['start_time']))

    df = pd.DataFrame(data=start_time, columns=['Start Time'])
    df['Max Dispatch'] = max_dispatch
    df['Load Reduction'] = load_reduction
    df['Reference Load'] = reference_load
    df['Date'] = [i.date() for i in start_time]
    df['Time'] = [i.time() for i in start_time]

    asset_id = []
    asset_max_dptch = []
    for i, dct in enumerate(data['data']['assets']):
        asset_id.append(dct['id'])
        asset_max_dptch.append([dct['maximum_dispatch_schedule'][md]['maximum_dispatch'] for md in
                                range(len(dct['maximum_dispatch_schedule']))])

    for i in range(len(asset_id)):
        df[asset_id[i] + 'bu'] = asset_max_dptch[i]

    return df
