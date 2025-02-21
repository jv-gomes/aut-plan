from PIL import Image
import pytesseract
import pandas as pd
import numpy as np
import PyPDF2 as pdf
from datetime import datetime
import locale

#Configuração de ambiente
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


#Funções
def newExcel():
    planilha = {'Data': ['10/01/2025'],
                'Descrição':['teste'],
                'Valor': ['10,00']}
    data = pd.DataFrame(planilha)
    data.to_excel('planilha.xlsx')


def readExcel():
    data = pd.read_excel('planilha.xlsx')
    print(data)



def readImage(image):
    string = pytesseract.image_to_string(image, lang='por')
    return string


def readPDF():
    with open('PDF/pdf1.pdf' ,'rb') as arquivo:
        leitor_pdf = pdf.PdfReader(arquivo)
        texto = ""
        for pagina in leitor_pdf.pages:
            texto += pagina.extract_text()
        print('texto do PDF')
        return texto


def clearText(text ,base, tipo): 
    if tipo == 'imagem':
        valores = text.split('\n\n')
        date = datetime.strptime(valores[3], "%d de %B de %Y")
        local = valores[0]
        base.loc[len(base)] = [valores[6], 'UBER', 'daq ali', 8000]
        print (valores)

    if tipo == 'pdf':
        valores = text.split('\n')
        date = datetime.strptime(valores[1], "%d/%m/%Y %H:%M")

        print(valores)

base = pd.DataFrame(columns=['Data','Local','Descrição','Valor'])
imagem = Image.open('Images/imagem2.png')
# newExcel()
# readExcel()

clearText(readPDF(),base, 'pdf')
# clearText(readImage(imagem),base)
# clearText(readImage(imagem),base)
# print(base)