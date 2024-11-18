from pdf2docx import Converter
old_pdf = "C:\Python_AK\Akash_CV.pdf"
new_doc = "New_Docx"
obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()