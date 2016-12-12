import csv
import os

script_dir = os.path.dirname(__file__)
rel_path = "../Datasets/apartamentos_mini.csv"
filename = os.path.join(script_dir, rel_path)
filename = os.path.abspath(os.path.realpath(filename))


apartamentos = []
with open(filename, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        apartamentos+=[[row['min_area'], row['latitude_formatada'], row['longitude_formatada'], row['quant_quartos'], row['quant_vagas'],row['quant_suites'], row['price']]]
