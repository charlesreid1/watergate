from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.pdfpage import PDFPage
import StringIO

def convert_pdf(filename):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec)

    fp = file(filename, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()

    str = retstr.getvalue()
    retstr.close()
    return str

if __name__=="__main__":
    print convert_pdf('../1primarytexts/pdf/482-017_482-018.pdf')
