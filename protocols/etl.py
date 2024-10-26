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


class YourETLProcess:
    def download(self) -> DataFrame:
        # Implement download logic
        return pd.DataFrame({"data": [4, 5, 6]})

    def transform(self) -> DataFrame:
        # Implement transformation logic
        df = self.download()
        return df * 3


def process_data(etl_process: ETL):
    transformed_df = etl_process.transform()
    print(transformed_df)


# Usage
etl = MyETLProcess()
process_data(etl)

etl = YourETLProcess()
process_data(etl)

# foo = object()
# process_data(foo)
