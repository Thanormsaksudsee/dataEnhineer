import sqlalchemy
connection

import pandas as pd
pd.read_sql("SELECT * FROM customers", db_engine)