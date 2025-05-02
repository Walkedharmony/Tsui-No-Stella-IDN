import re
import os

def extract_dialogue(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.ast'):
            file_path = os.path.join(directory, filename)
            output_filename = filename.replace('.ast', '.txt')
            output_path = os.path.join(directory, output_filename)
            
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Tangkap semua teks dari "cn = {{ "..." }}" dan "[[...]]"
            pattern = re.findall(r'cn\s*=\s*\{\s*\{\s*(?:"(.*?)"|\[\[(.*?)\]\])', content, re.DOTALL)
            
            with open(output_path, "w", encoding="utf-8") as output_file:
                for group in pattern:
                    text = group[0] if group[0] else group[1]
                    output_file.write(text + "\n")
            
            print(f"Extraction completed! Saved to {output_path}")

extract_dialogue(".")
