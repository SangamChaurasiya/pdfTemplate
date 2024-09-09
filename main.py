from fpdf import FPDF
import pandas

df = pandas.read_csv("topics.csv", sep=",")

pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0.0)

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")
    # pdf.line(x1=10, y1=21, x2=200, y2=21)
    for y in range(20, 298, 10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)

    # Set the footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="R")
    for i in range(int(row["Pages"])-1):
        pdf.add_page()
        for y in range(10, 298, 10):
            pdf.line(x1=10, y1=y, x2=200, y2=y)

        # Set the footer
        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="R")

pdf.output("output.pdf")
