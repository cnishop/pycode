import PyPDF2

with open('encyptChack.pdf','rb') as pdfFileOjb:
    pdfReader = PyPDF2.PdfFileReader(pdfFileOjb)

    # numpages =pdfReader.numPages

    if pdfReader.isEncrypted:
        if pdfReader.decrypt('python'):
            pageObj = pdfReader.getPage(0)
            print(pageObj.extractText())
            pageObj.rotateClockwise(90)
        else:
            print('wrong password')
    else:
        pageObj = pdfReader.getPage(0)
        print(pageObj.extractText())