import csv
import os
import numpy as np


class ZapImoveisDataset:
    def __init__(self, file_path):
        script_dir = os.path.dirname(__file__)
        rel_path = "../Datasets/apartamentos_mini.csv"
        filename = os.path.join(script_dir, rel_path)
        filename = os.path.abspath(os.path.realpath(filename))

    def load(self):
        with open(filename, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            return np.array( \
            	[[row['min_area'], row['latitude_formatada'], \
            	row['longitude_formatada'], row['quant_quartos'], \
            	row['quant_vagas'],row['quant_suites'], row['price']] for row in reader])