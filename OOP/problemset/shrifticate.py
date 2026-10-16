from fpdf import FPDF


name = input('What is your name?: ')



pdf = FPDF()
pdf.add_page()

pdf.set_font("Helvetica", "B", 30)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(15, 20)
pdf.cell(180, 15, "CS50 Shirtificate", align="C")

pdf.image('shirtificate.png', x=15, y=65, w=180)

pdf.set_xy(15, 125)
pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.cell(180, 12, f"{name} took CS50", align="C")


pdf.output("shirtificate.pdf")