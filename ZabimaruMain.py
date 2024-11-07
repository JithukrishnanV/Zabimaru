from customtkinter import *
from ZabiCode import *
from PIL import Image
from tkinter import messagebox, font, Text
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
import os,sys
from datetime import datetime  


if getattr(sys, 'frozen', False):  # Checks if running as a bundled executable
    base_path = sys._MEIPASS       # Temporary directory for bundled files
else:
    base_path = os.path.abspath(".")  # Regular directory when running as a script

# Initialize main window
win = CTk(fg_color="white")
win.title("Zabimaru")
win.geometry("500x300+400+80")
win.resizable(False, False)

# Load and place the logo
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, 'Logo.png')
my_img = CTkImage(dark_image=Image.open(logo_path), size=(400, 200))
lab = CTkLabel(win, image=my_img, text="")
lab.grid(row=0, column=0, padx=50, pady=10)

# Define the save_as_pdf function
def save_as_pdf(result_text):
    current_date = datetime.now().strftime("%Y-%m-%d")
    pdf_path = f"Reports/Scan_Result_{current_date}.pdf"

    # Create a PDF document using SimpleDocTemplate for easy text handling
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Retrieve text from result_text widget
    result_content = result_text.get("1.0", "end-1c").splitlines()

    # Loop through each line and add formatting
    for line in result_content:
        if line.startswith("Hash:") or line.startswith("Malware Information:") or line.startswith("Summary of Malware Analysis:") or line.startswith("Malicious Detections:"):
            paragraph = Paragraph(f"<b>{line}</b>", styles["Normal"])  # Bold headings
        else:
            paragraph = Paragraph(line, styles["Normal"])  # Regular text

        story.append(paragraph)
        story.append(Spacer(1, 10))  # Add space between lines for readability

    # Build the PDF
    doc.build(story)

    messagebox.showinfo("PDF Saved", f"Scan result saved as {pdf_path}")


# scan function
def scan(): 
    scan_text.set("SCANNING...")
    win.update_idletasks() 
    data = main() 
    if data == 1:
        return
    print(data)
    if not isinstance(data, dict) or not data:
        formatted_data = "No malicious hashes detected."
        messagebox.showinfo("Scan Completed", "No Virus found!")
        scan_text.set("SCAN")
    else:
        result_window = CTkToplevel(win)
        result_window.title("Scan Results")
        result_window.geometry("500x600")

        result_text = Text(result_window, wrap="word", padx=10, pady=10, width=58, height=30)
        result_text.pack(expand=True, fill="both")

        bold_font = font.Font(result_text, result_text.cget("font"))
        bold_font.configure(weight="bold")
        result_text.tag_configure("bold", font=bold_font)

        for hash_value, details in data.items():
            result_text.insert("end", "Hash: ", "bold")
            result_text.insert("end", f"{hash_value}\n")
            result_text.insert("end", "Malicious Detections: ", "bold")
            result_text.insert("end", f"{details['malicious_count']}\n")
            result_text.insert("end", "Malware Information:\n\n", "bold")
            
            if isinstance(details['malware_info'], list):
                for info in details['malware_info']:
                    result_text.insert("end", f"  - {info}\n\n")
            else:
                result_text.insert("end", f"{details['malware_info']}\n\n")
            
            result_text.insert("end", "-" * 50 + "\n\n")
            if hash_value =='d14b48bae7484afe7942b7f21830a9561e8c49cb4cf4fa9ebbc1dc5b4573a375':
                messagebox.showinfo("Dummy result", "This result is based on the virus hash in the code. check line 148 Zabicode.py")

        result_text.config(state="disabled")

        messagebox.showinfo("Scan Completed", "Virus found! Check the result")
        scan_text.set("SCAN")

        # Add "Save as PDF" button in the result window
        save_button = CTkButton(result_window, text="Save as PDF", command=lambda: save_as_pdf(result_text))
        save_button.pack(pady=10)

# Scan button
scan_text = StringVar()
scan_button = CTkButton(win, textvariable=scan_text, command=scan, font=("Bold", 20),
                        fg_color="black", text_color="white", hover_color="#800000",
                        border_width=1, border_color="red", height=40, width=190, cursor="hand2")
scan_text.set("SCAN")
scan_button.grid(row=2, column=0, pady=20)

# Run the application
win.mainloop()
