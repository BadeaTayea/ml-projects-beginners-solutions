import os

import pandas as pd

from .dataset_builder import DataSetBuilder


class MaxYearsDateSetBuilder(DataSetBuilder):

    def __init__(self):
        super().__init__()

    def build_data_set(self):
        df = pd.DataFrame()
        for division in self.DIVISIONS:
            for season_year in range(self.MIN_YEAR, self.MAX_YEAR - 1):
                path = os.path.join(os.path.dirname(__file__),
                                    "../data/" + division + "_" + str(season_year) + "_" + str(
                                        season_year + 1) + ".csv")
                df_tmp = pd.read_csv(path, keep_default_na=False, na_values="")
                df = pd.concat([df, df_tmp], ignore_index=True)
        df = df[["Div", "Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"]]
        return df
