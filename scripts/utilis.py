# function that reads csv, prints number of rows and columns, counts missing value in each column without using pandas and saves the summary to a txt file called summary_report.txt

def analyze_csv(file_path):
    import csv

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        print("The CSV file is empty.")
        return

    num_rows = len(rows) - 1  # excluding header
    num_cols = len(rows[0])
    header = rows[0]
    
    missing_counts = {col: 0 for col in header}

    for row in rows[1:]:
        for i, value in enumerate(row):
            if value == '':
                missing_counts[header[i]] += 1

    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_cols}")
    print("Missing values per column:")
    for col, count in missing_counts.items():
        print(f"{col}: {count}")

    with open('summary_report.txt', 'w') as report_file:
        report_file.write(f"Number of rows: {num_rows}\n")
        report_file.write(f"Number of columns: {num_cols}\n")
        report_file.write("Missing values per column:\n")
        for col, count in missing_counts.items():
            report_file.write(f"{col}: {count}\n")
