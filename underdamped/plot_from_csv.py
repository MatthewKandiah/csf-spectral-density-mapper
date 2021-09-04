import matplotlib.pyplot as plt
import csv

### run this in the same directory as your csv containing your plot points

with open('./results/mapped_underdamped_spectral_density.csv', 'r') as read_obj:
  csv_reader = csv.reader(read_obj)
  list_of_rows = list(csv_reader)

print(list_of_rows)