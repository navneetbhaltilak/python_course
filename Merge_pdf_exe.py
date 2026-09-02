import PyPDF2 as pdf
class PDF_merger:
    def __init__(self):
        self.pdf_merger = pdf.PdfMerger()
        pdf1 = input("Enter the name of First pdf you want to merge: ")
        pdf2 = input("Enter the name of Second pdf you want to merge: ")
        merger = self.pdf_merger
        merger.append(pdf1)
        merger.append(pdf2)
        merger.write("Merged.pdf")
        merger.close()
class PDF_reader:
    def __init__(self):
        pdf_file = input("Enter the name of pdf you want to read: ")
        pdf_reader = pdf.PdfReader(pdf_file)
        print("The number of pages in the pdf is: ", len(pdf_reader.pages))
        page_number = int(input("Enter the page number you want to read: "))
        page = pdf_reader.pages[page_number]
        print(page.extract_text())
class menu:
    def __init__(self):
        print("1.Merge two PDF's")
        print("2.Read a PDF")
        choice = int(input("Enter your choice: "))
        if choice ==1:
            PDF_merger()
        elif choice ==2:
            PDF_reader()
        else:
            print(".......Invalid choice......")
edit=menu()