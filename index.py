# from docxtpl import DocxTemplate

education = {
    'header1':"МІНІСТЭРСТВА ЎНУТРАНЫХ СПРАЎ РЭСПУБЛІКІ БЕЛАРУСЬ",
    'header2' :"ЎСТАНОВА АДУКАЦЫІ",
    'header3': '"АКАДЭМІЯ МІНІСТЭРСТВА ЎНУТРАНЫХ СПРАЎ РЭСПУБЛІКІ БЕЛАРУСЬ"',
    'img':'img/logo.png'
}
user = {
        'number':'34/2314',
        'firstname':'Борис',
        'secondname':'Александрович',
        'lastname':'Лавренов',
        'faculty':'Факультет Права',
        'form':'ЗАОЧНАЯ',
        'img':'img/sk.jpg',
        'date_stud':"29.09.2023",
        'date_vid':"11.06.2023",
        'date_end':"30.06.2028",
        }

# doc = DocxTemplate('template.docx')
# doc.render(data)
# doc.save('generate.docx')


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# def hello(c):
#     c.drawString(100,100,"Hello World")

NUMBER_X = 87*mm
FIELDS_LEFT_X = 58*mm
FIELDS_RIGTH_X = 147*mm
FIELDS_FOTO_X = 29*mm
CNT_X = 50.65*mm

def drawUserLEFT(pdf :canvas.Canvas,y,counter=0):
    # pdf.drawInlineImage('AMIAstamp_rotated.bmp',FIELDS_FOTO_X,y-34*mm-counter*CNT_X,20*mm,20*mm)
    pdf.drawImage(education['img'],FIELDS_FOTO_X,y-34*mm-counter*CNT_X,10*mm,11*mm,mask='auto')
    pdf.setFillColor('black')
    pdf.setFont('ArialBold',5)
    pdf.drawString(44*mm,y-25*mm-counter*CNT_X,education['header1'])
    pdf.setFillColor('red')
    pdf.drawString(61*mm,y-27*mm-counter*CNT_X,education['header2'])
    pdf.drawString(40*mm,y-29*mm-counter*CNT_X,education['header3'])
    pdf.setFillColor('black')
    pdf.setFont('ArialBoldItalic',10)
    pdf.drawString(NUMBER_X,y-34*mm-counter*CNT_X,user['number'])
    pdf.setFont('ArialBold',10)
    pdf.drawString(FIELDS_LEFT_X,y-42*mm-counter*CNT_X,user['lastname'].upper())
    pdf.drawString(FIELDS_LEFT_X,y-48.5*mm-counter*CNT_X,user['firstname'].upper())
    pdf.drawString(FIELDS_LEFT_X,y-55.5*mm-counter*CNT_X,user['secondname'].upper())
    pdf.drawString(FIELDS_LEFT_X,y-62*mm-counter*CNT_X,user['faculty'].upper())
    pdf.setFont('ArialBoldItalic',10)
    pdf.drawString(FIELDS_LEFT_X,y-68.5*mm-counter*CNT_X,user['form'].upper())
    pdf.drawImage(user['img'],FIELDS_FOTO_X,y-65*mm-counter*CNT_X,22*mm,29*mm)


def drawUserRIGHT(pdf:canvas.Canvas,y,counter =0):
    pdf.setFillColor('black')
    pdf.setFont('ArialBold',5)
    pdf.drawString(120*mm,y-26*mm-counter*CNT_X,education['header1'])
    pdf.setFillColor('red')
    pdf.drawString(137*mm,y-28*mm-counter*CNT_X,education['header2'])
    pdf.drawString(116*mm,y-30*mm-counter*CNT_X,education['header3'])
    pdf.setFillColor('black')
    pdf.setFont('ArialBold',8)
    pdf.drawString(FIELDS_RIGTH_X,y-34*mm-counter*CNT_X,user['date_stud'])
    pdf.drawString(FIELDS_RIGTH_X,y-39*mm-counter*CNT_X,user['date_vid'])
    pdf.drawString(FIELDS_RIGTH_X,y-44*mm-counter*CNT_X,user['date_end'])
    pdf.drawImage('img/pil.png',116*mm,y-63*mm-counter*CNT_X,30*mm,18.7*mm, mask='auto')
    pdf.drawImage('img/SignDekan_ed_preview_rev_1.png',147*mm,y-61*mm-counter*CNT_X,28*mm,17.5*mm, mask='auto')
    pdf.drawImage('img/background-removed.png',132*mm,y-68*mm-counter*CNT_X, 25*mm,25*mm,mask='auto')



c = canvas.Canvas("pdf/hello.pdf",pagesize=A4)
c.setFillColor
pdfmetrics.registerFont(TTFont('Arial','ArialRegular.ttf'))
pdfmetrics.registerFont(TTFont('ArialBoldItalic','ArialBoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold','ArialBold.ttf'))
x,y = A4


for i in range(0,13):
    if i % 5 == 0 and i!=0:
        c.showPage()
    drawUserLEFT(c,y,i%5)
    drawUserRIGHT(c,y,i%5)
 
c.save()