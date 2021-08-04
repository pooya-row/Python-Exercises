import pandas as pd
import json
import datetime


def forecast_data(file_path: str) -> pd.DataFrame:
    """
    Convert contents of `file_path` json file into a pandas data frame.

    :param file_path: string or Path object
    :return: pd.DataFrame
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    sample_time = []
    sample_type = []
    topology_element_id = []
    topology_element_type = []
    value = []

    for i, dct in enumerate(data):
        sample_time.append(datetime.datetime.fromisoformat(dct['sample_time']))
        sample_type.append(dct['sample_type'])
        topology_element_id.append(dct['topology_element_id'])
        topology_element_type.append(dct['topology_element_type'])
        value.append(dct['value'])

    df = pd.DataFrame(data=sample_time, columns=['Sample Time'])

    df['Sample Type'] = sample_type
    df['Topology Element ID'] = topology_element_id
    df['Topology Element Type'] = topology_element_type
    df['Value'] = value
    df['Date'] = [i.date() for i in sample_time]
    df['Time'] = [i.time() for i in sample_time]
    df['hr'] = [i.hour for i in sample_time]

    return df
