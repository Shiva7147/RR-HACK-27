import os
import subprocess
import pypdf

html_file = r"D:\HACKATHONS\SupeRR_Selector_Season_2\report.html"
pdf_file = r"D:\HACKATHONS\SupeRR_Selector_Season_2\Rajasthan_Royals_IPL_2027_Auction_Strategy.pdf"

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

print(f"Using Edge at: {edge_path}")

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-first-run",
    "--no-default-browser-check",
    "--run-all-compositor-stages-before-draw",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_file}",
    html_file
]

res = subprocess.run(cmd, timeout=30)
print("Subprocess return code:", res.returncode)

if os.path.exists(pdf_file):
    reader = pypdf.PdfReader(pdf_file)
    print(f"PDF successfully created at {pdf_file}")
    print(f"Total Pages: {len(reader.pages)}")
    print(f"File Size: {os.path.getsize(pdf_file) / 1024:.2f} KB")
