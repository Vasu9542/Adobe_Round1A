import os
import json
from app.extractor import extract_outline

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, file)
            output_path = os.path.join(OUTPUT_DIR, file.replace(".pdf", ".json"))
            print(f"Processing {file}")
            result = extract_outline(input_path)
            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
