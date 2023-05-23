from fpdf import FPDF


pdf = FPDF(orientation="portrait", format="A5")
pdf.set_auto_page_break(auto=False)
pdf.add_page()
pdf.image('shirtificate.png',x=0, y=50,h=pdf.eph, w=pdf.epw*1.15)
pdf.set_font('helvetica', size=20)
pdf.cell(txt="CS50 Shirtificate", x_new=100, y_new=100)
pdf.output("shirtificate.pdf")
