import PyPDF2

with open('11.pdf','rb') as pdfFile:
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWiter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        pdfWiter.addPage(pdfReader.getPage(pageNum))

    pdfWiter.encrypt('python')

    with open('e11.pdf','wb') as resultPdf:
        pdfWiter.write(resultPdf)