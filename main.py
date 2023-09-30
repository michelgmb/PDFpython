from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')

# create FDPF object
# Layout ('P', 'L')
# unit ('mm' , 'cm', 'in')

#format ('A3', 'A4'(default), 'A5', 'Letter' , 'Legal', (100,150))

pd =pd.read_csv('topics.csv')
for index, row in pd.iterrows():
        #for row in range()
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=24)
        pdf.set_text_color(100,100,100)#(rgb) 254 max
        # height h in pdf.cell should be as h for pdf.set-font()
        pdf.cell(w=0, h=12, txt=row['Topic'], align="L", border=0)
        pdf.line(10,20, 200, 20)


pdf.output('output.pdf')








# # specify font
# #font('times', 'courier', 'helvetica', 'symbol', 'zpfding')
# #'B' B (bold), I (italic) and U (underline) ,''(regular), combination(i.e , ('BU'))
# pdf.add_page()
# header = 'Header of PDF Report'
# pdf.set_font('helvetica', 'B', 10, )
# pdf.header()
# pdf.set_x((210) / 2)
#
# pdf.footer()
#
# pdf.set_font('helvetica', '', 20, )
# pdf.set_font(style="B")
# #Add text
# # W = width
# # h = height
# pdf.cell(120, 10, )
# pdf.ln()
# pdf.cell(120, 10, txt='God is good  World!')
# pdf.ln()
# pdf.cell(120, 10, txt='All the time World')
#
#
#
# pdf.add_page()
# pdf.cell(40, 10, txt='Hello World')
#
# pdf.output('output.pdf')