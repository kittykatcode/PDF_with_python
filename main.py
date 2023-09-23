from fpdf import FPDF, XPos, YPos
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False)
#reading csv file
df = pd.read_csv('topics.csv')

#iterating data from csv file to get topics title and no. og pages
for index,row in df.iterrows():

    #print(row['Topic'])
    pdf.add_page()
    # setting up font style
    pdf.set_font(family='Times',style='B', size=20)
    #setting text color in RGB
    pdf.set_text_color(200,100,200)

    #adding cell alingments
    pdf.cell(w=0,h=10,txt= row['Topic'],  align='L',new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    #adding aline under x1,y1,x2,y2
    pdf.line(10,20,200,20)
    #adding a footer
    pdf.ln(265)
    pdf.set_font(family='Times',style='I', size=10)

    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=10,txt= str(index+1) + row['Topic']+ ' '+str(row['Order']),  align='R',new_x=XPos.RMARGIN, new_y=YPos.NEXT)



    #getting no. of pages and subtracting 1 for the page already added above
    for i in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(277)

        pdf.cell(w=0,h=10,txt= row['Topic']+ ' '+str(row['Order']),  align='R',new_x=XPos.RMARGIN, new_y=YPos.NEXT)

    
pdf.output('output.pdf')