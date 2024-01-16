import csv

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    column_sums = []
    column_counts = []
    for row in csv_reader:
        while len(column_sums) < len(row):
            column_sums.append(0)
            column_counts.append(0)
        for i, value in enumerate(row):
            try:
                num = float(value)
                column_sums[i] += num
                column_counts[i] += 1
            except ValueError:
                pass

averages = [sums / counts if counts > 0 else 0 for sums, counts in zip(column_sums, column_counts)]
print("Средние арифметические по колонкам:")
for i, average in enumerate(averages):
    print(f"Колонка {i + 1}: {average}")