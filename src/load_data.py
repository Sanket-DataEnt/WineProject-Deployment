# read the data from data source (through get_data)
# push the data into data/raw for further process

import os
from get_data import read_params, get_data
import argparse


def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    # removing empty spaces from the column names.
    new_cols = [col.replace(" ","_") for col in df.columns]
    # print(new_cols)
    raw_data_path = config['load_data']['raw_dataset_csv']
    # print(raw_data_path)
    df.to_csv(raw_data_path, index=False, header=new_cols)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)