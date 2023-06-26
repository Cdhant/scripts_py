import json
import os
import xlsxwriter

def json_to_excel(json_file, worksheet):
    with open(json_file) as file:
        data = json.load(file)
        row = 0
        for idx, key in enumerate(data.keys()):
            row += 1
            worksheet.write(row, 0, idx+1)
            worksheet.write(row, 1, key)
            worksheet.write(row, 2, data[key])

def convert_dir_to_excel(dir_path, output_file):
    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet()

    row = 0
    worksheet.write(row, 0, 'File')
    worksheet.write(row, 1, 'Data')
    row += 1

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.json'):
                json_file = os.path.join(root, file)
                json_to_excel(json_file, worksheet)
                row += 1

    workbook.close()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Converts JSON files in a directory to an Excel spreadsheet')
    parser.add_argument('dir_path', help='Path to directory containing JSON files')
    parser.add_argument('output_file', help='Path to output Excel file')
    args = parser.parse_args()

    convert_dir_to_excel(args.dir_path, args.output_file)

