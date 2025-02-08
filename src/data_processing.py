import json
import csv

class Data:
    def __init__(self, data):
        self.data = data
        self.column_name = self.__get_columns()
        self.rows_amount = self.__size_data()

    @staticmethod
    def __read_json(path):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def __read_csv(path):
        csv_data = []
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                csv_data.append(row)
        return csv_data

    @classmethod
    def data_read(cls, path, data_type):
        if data_type == "csv":
            data = cls.__read_csv(path)
        elif data_type == "json":
            data = cls.__read_json(path)
        else:
            raise ValueError("Unsupported data type. Use 'csv' or 'json'.")
        return cls(data)

    def __get_columns(self):
        if not self.data:
            return []
        return list(self.data[0].keys())  # Pega as colunas do primeiro item

    def rename_columns(self, key_mapping):
        new_data = []
        for old_dict in self.data:
            dict_temp = {key_mapping.get(old_key, old_key): value for old_key, value in old_dict.items()}
            new_data.append(dict_temp)

        self.data = new_data
        self.column_name = self.__get_columns()

    def __size_data(self):
        return len(self.data)

    @staticmethod
    def join(dataA, dataB):
        combined_list = dataA.data + dataB.data
        return Data(combined_list)

    def __table_data_transform(self):
        data_table_combined = [self.column_name]

        for row in self.data:
            transformed_row = [row.get(column, 'Indisponível') for column in self.column_name]
            data_table_combined.append(transformed_row)

        return data_table_combined

    def save_data(self, path):
        data_table_combined = self.__table_data_transform()
        with open(path, 'w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_table_combined)
