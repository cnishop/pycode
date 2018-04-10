import PyPDF2
filenames=['11.pdf','22.pdf','33.pdf']

merger= PyPDF2.PdfFileMerger()
for filename in filenames:
    merger.append(PyPDF2.PdfFileReader(filename))
merger.write('PythonABC合并.pdf')