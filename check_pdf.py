import pypdf
import os

pdf_path = r"D:\HACKATHONS\SupeRR_Selector_Season_2\Rajasthan_Royals_IPL_2027_Auction_Strategy.pdf"
reader = pypdf.PdfReader(pdf_path)
print(f"Total Pages: {len(reader.pages)}")
print(f"Size: {os.path.getsize(pdf_path) / 1024:.2f} KB")
