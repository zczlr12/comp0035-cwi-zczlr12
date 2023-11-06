"""Prepare and explore the past sales data downloaded from
https://data.mendeley.com/datasets/njdkntcpc9/1

Authors of the original dataset:
    Paolo Mancuso, Veronica Piccialli, Antonio M. Sudoso (University of Rome
    Tor Vergata)

Usage:
    ./data_prep.py

Author:
    Renkai Liu - 05.11.2023
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def print_df_information(df):
    """
    Print basic data information of a pandas DataFrame

    Args:
        df: Pandas DataFrame from the original dataset
    """

    print("\nNumber of rows:")
    print(df.shape[0])
    print("\nNumber of columns:")
    print(df.shape[1])

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nColumn labels, datatypes and value counts:")
    print(df.info(verbose=True))


def find_nulls(df):
    """
    Find and print the information of missing values

    Args:
        df: Pandas DataFrame from the original dataset
    """
    print("\nTotal number of missing values:")
    print(df.isnull().sum().sum())

    print("\nColumns and rows with missing values:")
    cols_with_nulls = df.loc[:, df.isnull().any()]
    rows_with_nulls = cols_with_nulls[cols_with_nulls.isnull().any(axis=1)]
    print(rows_with_nulls)


def find_duplicates(df):
    """
    Find and print the information of duplicated rows

    Args:
        df: Pandas DataFrame from the original dataset
    """
    print("\nTotal number of duplicated rows:")
    print(df.duplicated().sum())

    print("\nDuplicated rows:")
    print(df[df.duplicated(keep=False)])


def find_unique_values_of_promotion_flags(df):
    """
    Find and print the unique values of the promotion flags

    Args:
        df: Pandas DataFrame from the original dataset
    """
    print("\nUnique values of promotion flags:")
    # Print unique values of all columns with names starting with 'PROMO'
    print(df.filter(regex='^PROMO').stack().unique())


def modify_columns(df):
    """
    Change the data type of DATE column, reorder columns to put columns of the
    same item together, and remove blank spaces in column labels

    Args:
        df: Pandas DataFrame from the original dataset

    Returns:
        df: A pandas DataFrame with the prepared data
    """

    # Change data type of DATE column from object to datetime
    df['DATE'] = pd.to_datetime(df['DATE'])

    # Reorder columns and remove blank spaces in column labels
    cols = df.columns.tolist()
    reordered_cols = cols.copy()  # initialise reordered column labels
    for i in range(1, (len(cols)-1)//2+1):
        # Put columns of the quantity sold to new locations
        reordered_cols[i*2-1] = cols[i].strip()
        # Put columns of promotion flags to new locations
        reordered_cols[i*2] = cols[i+(len(cols)-1)//2].strip()

    return df[reordered_cols]


def general_statistics(df):
    """
    Print the general statistics of the dataset, and plot boxplots of the
    quantity sold for four items

    Args:
        df: Pandas DataFrame from the prepared dataset
    """
    print("\nGeneral statistics of the dataset:")
    print(df.describe())

    print("\nGeneral statistics with the quantity sold only:")
    print(df.filter(regex='^QTY').describe())

    # Plot boxplots of the quantity sold for four items
    sampled_df = df[['QTY_B1_1', 'QTY_B1_2', 'QTY_B1_3', 'QTY_B1_4']]
    sampled_df.plot.box(subplots=True, grid=True)
    # Save the boxplots
    fig_file = Path(__file__).parent.joinpath('boxplots.png')
    plt.savefig(fig_file)


def line_chart(df):
    """
    Plot a line chart of the quantity sold for four items and the last two
    months in the dataset

    Args:
        df: Pandas DataFrame from the prepared dataset
    """
    # Plot a line chart of the quantity sold for four items
    df.iloc[1742:].plot(x='DATE',
                        y=['QTY_B1_1', 'QTY_B1_2', 'QTY_B1_3', 'QTY_B1_4'],
                        grid=True, ylim=(0, 10), ylabel='Quantity sold')
    # Save the line chart
    fig_file = Path(__file__).parent.joinpath('line_chart.png')
    plt.savefig(fig_file)


if __name__ == '__main__':
    # Load raw data into a pandas DataFrame
    raw_data_file = Path(__file__).parent.joinpath('dataset.csv')
    raw_df = pd.read_csv(raw_data_file)
    # Set the option to display all rows
    pd.set_option('display.max_rows', raw_df.shape[0])

    # Prepare the data
    print_df_information(raw_df)
    find_nulls(raw_df)
    find_duplicates(raw_df)
    find_unique_values_of_promotion_flags(raw_df)
    prepared_df = modify_columns(raw_df)

    # Save prepared data set
    prepared_data_file = Path(__file__).parent.joinpath('dataset_prepared.csv')
    prepared_df.to_csv(prepared_data_file, index=False)

    # Explore the data
    general_statistics(prepared_df)
    line_chart(prepared_df)
