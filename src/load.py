#import psycopg2
from utils import db_utils
from psycopg2.extras import execute_values

import logging
import pandas as pd # only import for autocomplete and hints

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def load(df: pd.DataFrame, table_name: str):
    
    try:
        with db_utils.get_connection() as conn:
            with conn.cursor() as cur:

                cols = ", ".join(df.columns)
                values = [tuple(row) for row in df.itertuples(index=False)]

                sql = f"INSERT INTO {table_name} ({cols}) VALUES %s"

                execute_values(cur, sql, values)

                conn.commit()

                LOGGER.info(f"load: loaded {len(df)} rows into '{table_name}'")

    except Exception as e:
        LOGGER.error("load: load failed. Error: {e}")
        raise e   # propagate error to main.py
        



