import pandas as pd
import uuid

def get_transaction_data():
    """
    Temporary extract function.
    Replace with actual extract module later.
    """
    return pd.read_csv(
        "./data/leeds_28-03-2025_09-00-00_1.csv",
        header=None,
        names=["payment_time", "city", "customer_name", "basket", "total_price", "payment_method", "card_number"]
        )


df = get_transaction_data()

def generate_uuid():
    
    return str(uuid.uuid4())


def add_uuid(df, id_column_name):
    """
    Function for adding a UUID column to an existing df 
    """

    df[id_column_name] = [generate_uuid() for i in range(len(df))]

    return df


def remove_duplicates(df):
    '''
    Function to remove duplicate rows from our data
    '''
    
    return df.drop_duplicates()


def drop_sensitive_data(df):

    return df.drop(columns=["customer_name", "card_number"])




def normalise_to_1nf(df: pd.DataFrame):

    # atomise the df

    # create a new column named 'items', turn values in 'basket' into a list and populate the 'items' column with these lists
    df_1nf = df.assign(items=df['basket'].str.split(','))

    # turn each element of a list in a cell into seperate rows
    df_1nf = df_1nf.explode('items')

    # clean whitespaces
    df_1nf['items'] = df_1nf['items'].str.strip()

    # split items into product_name and product_price
    df_1nf[['product_name', 'product_price']] = df_1nf["items"].str.rsplit(' - ', n=1, expand=True)

    # drop unnecessary columns
    df_1nf = df_1nf.drop(columns=['basket', 'items'])

    return df_1nf





# ------------------------------------

def transform_data(df):
    
    # remove duplicate rows
    df = remove_duplicates(df)

    # generate GUIDs for the orders
    df = add_uuid(df, "order_id")

    # drop customer name and card number columns
    df = drop_sensitive_data(df)

    # normalise to 1NF
    df_1nf = normalise_to_1nf(df)

    # normalise to 3NF

    
    return df_1nf

df = transform_data(df)
print(df.head(10))


