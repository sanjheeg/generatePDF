from fpdf import FPDF
import pandas as pd

# portrait orientation, millimeter uit
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")
count = 1

for index, row in df.iterrows():
    num = row["Pages"]
    for i in range(num):
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(90, 0, 50)
        # ln=1 is a break line. if ln=0, there is no break and the cells with collide
        # align=L is left
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
        pdf.line(10, 21, 200, 21)
        pdf.ln(260)
        pdf.set_text_color(0, 0, 100)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=10, txt=f'{row["Topic"]}   {count}', align="R")
        count += 1


pdf.output("output.pdf")
