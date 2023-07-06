from fpdf import FPDF
import pandas as pd

# portrait orientation, millimeter uit
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    pdf.add_page()

    # any cell after this line will be the following style
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(90, 0, 50)
    # ln=1 is a break line. if ln=0, there is no break and the cells with collide
    # align=L is left
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)

pdf.output("output.pdf")
