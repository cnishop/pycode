import PyPDF2
with open('PythonABC.pdf','rb') as pdfFile:
    pdfReader=PyPDF2.PdfFileReader(pdfFile)
    minutesFirstPage=pdfReader.getPage(0)

    with open('sy.pdf','rb') as markFile:
        pdfWaterMarkReader = PyPDF2.PdfFileReader(markFile)
        minutesFirstPage.mergePage(pdfWaterMarkReader.getPage(0))

        pdfWiter = PyPDF2.PdfFileWriter()
        pdfWiter.addPage(minutesFirstPage)

        for pageNum in range(1,pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWiter.addPage(pageObj)

        with open('waterMark.pdf','wb') as resultPdfFile:
            pdfWiter.write(resultPdfFile)
