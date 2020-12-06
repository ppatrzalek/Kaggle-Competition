from src.data.manage_data import DataLoader, DataSaver, _project_directory
import os
import pandas as pd
import numpy as np


files_location = os.listdir(os.path.join(_project_directory(), 'data/raw'))
files_location.remove('ALL_hourly.csv')

if __name__ == "__main__":

    df_all = pd.DataFrame()

    for path_raw in files_location:
        data_model_load = DataLoader(processed=False, name=path_raw[:-4])
        df = data_model_load.load_data()
        df['Name'] = np.repeat(df.columns[1], df.shape[0])
        df.columns = ('Datetime', 'Value', 'Name')
        df_all = pd.concat([df_all, df], axis=0)

    data_model_save = DataSaver(data=df_all, processed=True, name='ALL_hourly')
    data_model_save.save_data()
