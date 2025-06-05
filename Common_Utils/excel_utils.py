import openpyxl

class ExcelUtils:

    @staticmethod
    def read_excel_as_dicts(file_path, sheet_name=None):

        wb = openpyxl.load_workbook(file_path)
        sheet = wb[sheet_name] if sheet_name else wb.active

        # Read headers from the first row
        headers = [cell.value for cell in sheet[1]]

        # Read each row as a dictionary
        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_dict = dict(zip(headers, row))
            data.append(row_dict)

        wb.close()
        return data