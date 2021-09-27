import os

import pandas
from sqlalchemy import create_engine

print("preparing data...")

engine = create_engine("sqlite:///data.sqlite")


for file in sorted(list(os.listdir("data"))):
    if file.endswith(".csv"):
        df = pandas.read_csv(
            os.path.join("data", file),
            index_col=0,
            dtype={"itm_cd": str, "itg_cd": str, "mfg_cd": str, "sup_cd": str},
        )
        df.to_sql(file.split(".")[0], con=engine)
