from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def add_shirt_image(self, name):
        self.image("shirtificate.png", x=0, y=60, w=210)
        self.set_font("Arial", "B", 24)
        self.set_text_color(255, 255, 255)
        self.text(x=105, y=140, txt=name)

def main():
    name = input("Enter your name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.add_shirt_image(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
