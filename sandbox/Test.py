from PyPDF2 import PdfReader, PdfWriter

# Open the existing PDF
reader = PdfReader("golden_1_dao_agreement_templated.pdf")
writer = PdfWriter()

# Copy pages to a new PDF
for page in reader.pages:
    writer.add_page(page)

# Modify metadata
metadata = reader.metadata
writer.add_metadata({
    "/Title": "Deposit Account Opening Agreement",
    # "/Author": metadata.get("/Author", "Unknown"),
    # "/Subject": metadata.get("/Subject", ""),
})

# Save the new PDF
with open("golden_1_dao_agreement.pdf", "wb") as output_pdf:
    writer.write(output_pdf)

print("PDF Title updated successfully!")
