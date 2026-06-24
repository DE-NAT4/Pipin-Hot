from utils import s3_utils, db_utils

import extract
import transform
import load
import json
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def lambda_handler(event, context):
    file_path = 'NOT_SET'   # makes the exception handler compile

    try:
        bucket_name, file_path = s3_utils.get_file_info(event)

        df_raw = extract.get_data(bucket_name=bucket_name, s3_key=file_path)

        df_orders, df_products, df_order_items = transform.transform_data(df_raw)

        load.load(df_orders, "orders_test")
        load.load(df_products, "products_test")
        load.load(df_order_items, "order_items_test")

        LOGGER.info(f'lambda_handler: done, file={file_path}')

    except Exception as e:
        LOGGER.error(f'lambda_handler: failure: error={e}, file=')




    # # TODO implement
    # print('Hello from Lambda')
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello, Marcell!')
    # }
