from typing import Protocol
import pandas as pd
from pandas import DataFrame


class ETL(Protocol):
    def download(self) -> DataFrame:
        ...

    def transform(self) -> DataFrame:
        ...


class MyETLProcess:
    def download(self) -> DataFrame:
        # Implement download logic
        return pd.DataFrame({"data": [1, 2, 3]})

    def transform(self) -> DataFrame:
        # Implement transformation logic
        df = self.download()
        return df * 2


def process_data(etl_process: ETL):
    df = etl_process.download()
    transformed_df = etl_process.transform()
    print(transformed_df)


# Usage
etl = MyETLProcess()
process_data(etl)

foo = object()
process_data(foo)