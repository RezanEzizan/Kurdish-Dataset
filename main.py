from scripts.pdf_to_text import PDFTextExtractor

# Converts the PDF file to text and transfers it to data/raw/raw_kurmanji.txt for manual review.
pdftextextractor = PDFTextExtractor("data/data_files/ciroka_rovi_u_ser.pdf")

# After manual review, the final data is transferred to kurmanji.txt and kurmanji.json.
pdftextextractor.append_raw_to_processed_data()
