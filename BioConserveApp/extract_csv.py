import pandas as pd

def extract_csv(file_path):
    """
    Extract data from a CSV file.
    :param file_path: Path to the CSV file.
    :return: A pandas DataFrame containing the data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None