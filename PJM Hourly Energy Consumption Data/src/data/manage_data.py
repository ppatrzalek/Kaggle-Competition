import os
import pandas as pd


def _project_directory():
    return '/home/piotr/Documents/GitHub/Kaggle-Competition/PJM Hourly Energy Consumption Data'


class DataLoader:
    def __init__(self, processed, name):
        self.processed = processed
        self.name = name

    def _localization(self):
        if self.processed is True:
            return os.path.join(_project_directory(), 'data/processed')
        elif self.processed is False:
            return os.path.join(_project_directory(), 'data/raw')
        else:
            print('Processed have only two optional values: True or False :)')

    def _path_load(self):
        if self.processed is True:
            self.path = os.path.join(self._localization(), self.name + '.parquet')
        elif self.processed is False:
            self.path = os.path.join(self._localization(), self.name + '.csv')
        else:
            print('Processed have only two optional values: True or False :)')
        return self.path

    def _path_authentication(self):
        if os.path.isfile(self._path_load()) is True:
            return self._path_load()
        else:
            print(f'Wrong directory. {self._path_load()} is not exists :/')

    def load_data(self):
        try:
            self._path_authentication()
            if self.processed is True:
                return pd.read_parquet(os.path.join(self._path_load()), engine='fastparquet')
            elif self.processed is False:
                return pd.read_csv(os.path.join(self._path_load()))
            else:
                print('Processed have only two optional values: True or False :)')
        finally:
            pass


class DataSaver(DataLoader):
    def __init__(self, data, processed, name):
        super().__init__(processed, name)
        self.data = data

    def _path_save(self):
        if self.processed is True:
            self.path = os.path.join(_project_directory(), 'data/processed', self.name + '.parquet')
        elif self.processed is False:
            print('You can save data only to processed directory')
        else:
            print('Processed have only two optional values: True or False :)')
        return self.path

    def save_data(self):
        if self.processed is True:
            return self.data.to_parquet(self._path_save(), compression='snappy', engine='fastparquet')
        elif self.processed is False:
            print('You can save data only to processed directory')
        else:
            print('Processed have only two optional values: True or False :)')
