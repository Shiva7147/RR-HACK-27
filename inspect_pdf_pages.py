import pypdf

reader = pypdf.PdfReader(r"D:\HACKATHONS\SupeRR_Selector_Season_2\Rajasthan_Royals_IPL_2027_Auction_Strategy.pdf")
print("Total pages:", len(reader.pages))

for idx, page in enumerate(reader.pages):
    text = page.extract_text()
    first_line = text.split('\n')[0] if text else "EMPTY"
    last_line = text.split('\n')[-2] if len(text.split('\n')) > 1 else "EMPTY"
    print(f"Page {idx+1}: {first_line[:40]} ... | Footer: {last_line[-30:]} | Chars: {len(text)}")
