import easyocr
import fitz
import os
from llama_index.llms.ollama import Ollama
class PdfReader:
    def __init__(self,pdf_path,output_fold , llm= None, timeout=None ,language = None):
        self.pdf_path = pdf_path
        self.output_fold = output_fold
        if llm is None:
            self.llm = 'llama3'
        else:
            self.llm = llm
        if timeout is None:
            self.timeout = 60
        else:
            self.timeout = timeout
        self.paragraph = ' '
        if language is None:
            self.language = 'en'
        else:
            self.language = language
    def perform_OCR(self,output_path):
        reader = easyocr.Reader([self.language])
        docs = reader.readtext(output_path)
        for result in docs:
            self.paragraph  = self.paragraph + ' ' + result[1]

    def pdf_to_markdowntxt(self, dpi=300):
        pdf_document = fitz.open(self.pdf_path)
        zoom_x = dpi / 72
        zoom_y = dpi / 72
        matrix = fitz.Matrix(zoom_x, zoom_y)

        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap(matrix=matrix)
            output_path = os.path.join(self.output_fold, f"page_{page_num}.png")
            pix.save(output_path)
            self.perform_OCR(output_path)
            os.remove(output_path)
        pdf_document.close()
        markdown = self.llm_parse(self.paragraph)
        with open(f"{self.output_fold}/output.txt", 'w') as file:
            file.write(markdown)

    def llm_parse(self,text):
        model = Ollama(model= self.llm , request_timeout= self.timeout)
        template = "this text is extracted from a Document using OCR make this readable and like orignal document and fix it here is the OCR text" + text
        return f'{model.complete(template)}'

