from pypdf import PdfReader, PdfWriter
def mergepdf(filelist, output_path, page_ranges=None, merge_into_existing=None):
    writing = PdfWriter()
    if merge_into_existing:
        existing_reader = PdfReader(merge_into_existing)
        for pages in existing_reader.pages:
            writing.add_page(pages)
    for index, file in enumerate(filelist):
        reading = PdfReader(file)
        total_pages = len(reading.pages)
        if page_ranges and index < len(page_ranges):
            start, end = page_ranges[index]
            start = max(0, start - 1)  # Adjusting to 0-indexing (user provides 1-indexed)
            end = min(total_pages, end)  # End remains the same (user provides inclusive end)
        else:
            start = 0
            end = total_pages
        for number in range(start, end):
            writing.add_page(reading.pages[number])
    with open(output_path, "wb") as finalpdf:
        writing.write(finalpdf)
    
    print(f"Merging successful for PDF files into {output_path}!")

def get_page_ranges(filelist):
    page_ranges = []
    for filepath in filelist:
        print(f"For file: {filepath}")
        start = int(input("Enter the start page (1-indexed): "))
        end = int(input("Enter the end page (inclusive, 1-indexed): "))
        page_ranges.append((start, end))
    return page_ranges
files = [
    input("Enter path for file 1: "),
    input("Enter path for file 2: ")
]
specify_page_ranges = input("Do you want to specify page ranges? (Y/N): ").strip().lower()
if specify_page_ranges == 'y':
    page_ranges = get_page_ranges(files)
else:
    page_ranges = None  
existing_pdf_to_merge = None  
output_path = input("Enter the output path for the merged PDF: ")

mergepdf(files, output_path, page_ranges=page_ranges, merge_into_existing=existing_pdf_to_merge)
