import csv


def load_data(files):
    rows = []

    for file_path in files:
        try:
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                rows.extend(list(reader))
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")

    return rows
