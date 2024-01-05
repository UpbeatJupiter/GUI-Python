from openpyxl import load_workbook

# Load the workbook from an Excel file
wb = load_workbook("student_list.xlsx")

# Get the reference of the active (first) worksheet
ws1 = wb.active

# Get a range of values
output = ""
data = ws1["A2:C5"]
for row in data:
    for cell in row:
        output += str(cell.value) + "\t"
    output += "\n"

print(output)
