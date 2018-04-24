import os

import pandas as pd

from .dataset_builder import DataSetBuilder


class CenturyDataSetBuilder(DataSetBuilder):

    def __init__(self):
        super().__init__()

    def build_data_set(self):
        df = pd.DataFrame()
        for division in self.DIVISIONS:
            for season_year in range(2000, self.MAX_YEAR - 1):
                path = os.path.join(os.path.dirname(__file__),
                                    "../data/" + division + "_" + str(season_year) + "_" + str(
                                        season_year + 1) + ".csv")
                df_tmp = pd.read_csv(path, keep_default_na=False, na_values="")
                df = pd.concat([df, df_tmp], ignore_index=True)
        df = df[["Div", "Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "HTHG", "HTAG", "HTR", "Attendance",
                 "Referee", "HS", "AS", "HST", "AST", "HHW", "AHW", "HC", "AC", "HF", "AF", "HO", "AO", "HY", "AY",
                 "HR", "AR", "HBP", "ABP", "GBH", "GBD", "GBA",
                 "IWH", "IWD", "IWA", "LBH", "LBD", "LBA", "SBH", "SBD", "SBA", "WHH", "WHD", "WHA"]]
        return df
