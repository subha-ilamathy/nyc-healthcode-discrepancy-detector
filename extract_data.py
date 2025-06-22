from docling.document import PDFDocument
import re
import json

# Load entire Health Code PDF
doc = PDFDocument("health-code-article81.pdf")
text = doc.text()

# Clean up formatting if needed
text = text.replace('\xa0', ' ')  # Remove non-breaking spaces

# Pattern to capture ANY section like 81.09(c)
# Captures: section, subsection, content
pattern = r"(\d{2}\.\d{2})\s*\(([a-z])\)\s+(.*?)(?=\n\d{2}\.\d{2}\s*\([a-z]\)|\n\d{2}\.\d{2}|$)"

matches = re.findall(pattern, text, re.DOTALL)

# Build structured dictionary
section_map = {}
for section, subsection, desc in matches:
    code = f"{section}({subsection})"
    cleaned = re.sub(r"\s+", " ", desc.strip())
    section_map[code] = cleaned

# Save to JSON
with open("parsed_health_code.json", "w") as f:
    json.dump(section_map, f, indent=2)

print(f"Extracted {len(section_map)} section codes.")
