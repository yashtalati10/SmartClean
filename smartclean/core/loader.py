import pandas as pd


class DataLoader:
    """
    Loads CSV and Excel files into a Pandas DataFrame.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_type = None

    def load_data(self):

        file_path = self.file_path.lower()

        if file_path.endswith(".csv"):

            self.file_type = "CSV"
            print("📂 Loading CSV file...")

            return pd.read_csv(self.file_path)

        elif file_path.endswith((".xlsx", ".xls")):

            self.file_type = "Excel"
            print("📂 Loading Excel file...")

            return pd.read_excel(self.file_path)

        else:

            raise ValueError(
                "Unsupported file type. Please upload a CSV or Excel file."
            )