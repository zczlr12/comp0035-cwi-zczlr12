# Data preparation and understanding code
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def rename_column(column_name):
    """
    Renames a column name to a more readable format

    Args:
        column_name: Name of the column to be renamed

    Returns:
        Renamed column name
    """
    new_column = column_name.replace("QTY_B", "Quantity sold for brand ")
    new_column = new_column.replace("PROMO_B", "Promotion flag for brand ")
    new_column = new_column.replace("_", " item ")
    return new_column.strip()


def prepare_data(df):
    """
    Prepares the data for analysis

    Args:
        df: Pandas DataFrame from the dataset

    """
    df['DATE'] = pd.to_datetime(df['DATE'])
    df_prepared = df.rename(columns=rename_column)
    prepared_data_file = Path(__file__).parent.joinpath('dataset_prepared.csv')
    df_prepared.to_csv(prepared_data_file, index=False)
    return df_prepared


def print_df_information(df):
    """
    Prints general information about the DataFrame

    Args:
        df: Pandas DataFrame from the dataset
    """

    print("\nNumber of rows:\n")
    print(df.shape[0])
    print("\nNumber of columns:\n")
    print(df.shape[1])

    print("\nFirst 5 rows:\n")
    print(df.head())

    print("\nColumn labels, datatypes and value counts:\n")
    print(df.info(verbose=True))

    print("\nGeneral statistics:\n")
    print(df.describe())

    print("\nNumber of missing values per column:\n")
    print(df.isnull().sum())

    print("\nRows with missing values:\n")
    print(df[df.isnull().any(axis=1)])

    print("\nNumber of duplicates:\n")
    print(df.duplicated().sum())


if __name__ == '__main__':
    raw_data_file = Path(__file__).parent.joinpath('dataset.csv')
    raw_df = pd.read_csv(raw_data_file)

    print_df_information(raw_df)
    prepared_df = prepare_data(raw_df)
    print_df_information(prepared_df)
