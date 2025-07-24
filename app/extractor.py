import fitz  # PyMuPDF

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    font_size_counter = {}

    # Step 1: Analyze font sizes across all pages
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    size = round(span["size"], 1)
                    font_size_counter[size] = font_size_counter.get(size, 0) + 1

    # Step 2: Pick top 3 font sizes (assumed H1 > H2 > H3)
    top_sizes = sorted(font_size_counter.items(), key=lambda x: (-x[1], -x[0]))
    size_levels = [size for size, _ in top_sizes[:3]]

    h1_size = size_levels[0] if len(size_levels) > 0 else 16
    h2_size = size_levels[1] if len(size_levels) > 1 else h1_size - 1
    h3_size = size_levels[2] if len(size_levels) > 2 else h2_size - 1

    def is_bold(span):
        return (span.get("flags", 0) & 2) != 0

    def clean(text):
        return text.strip().replace('\n', ' ')

    # Step 3: Extract title (first bold H1-sized text on page 1)
    title = ""
    for block in doc[0].get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                if round(span["size"], 1) == h1_size and is_bold(span):
                    title = clean(span["text"])
                    break
            if title:
                break
        if title:
            break

    # Step 4: Extract headings only
    outline = []
    for page_num, page in enumerate(doc, start=1):
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = clean(span["text"])
                    size = round(span["size"], 1)

                    if len(text) < 4 or not text[0].isupper():
                        continue
                    if text.lower() in ["linkedin", "github", "email", "phone", "contact"]:
                        continue
                    if not any(c.isalpha() for c in text):
                        continue

                    level = None
                    if size == h1_size and is_bold(span):
                        level = "H1"
                    elif size == h2_size:
                        level = "H2"
                    elif size == h3_size:
                        level = "H3"

                    if level:
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_num
                        })

    return {
        "title": title or "Untitled Document",
        "outline": outline
    }
