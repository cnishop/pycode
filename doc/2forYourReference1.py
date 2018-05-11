import docx
from docx.shared import Cm

document = docx.Document('test.docx')

table = document.tables[0]

for row,obj_row in enumerate(table.rows):
    for col,cell in enumerate(obj_row.cells):
        cell.text = '{},{}'.format(row,col)

table.columns[4].width = Cm(4)
row = table.rows[4]
row.cells[0].text='aaa'
row.cells[1].text='bbbb'
document.save('test.docx')