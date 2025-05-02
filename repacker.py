import re

def repack_scenario(input_path, output_path, dialogue_path):
    with open(input_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    with open(dialogue_path, "r", encoding="utf-8") as extracted_file:
        extracted_lines = [line.strip() for line in extracted_file.readlines()]
    
    matches = re.findall(r'cn\s*=\s*\{\s*\{\s*(?:\[\[(.*?)\]\]|"([^"]*)")', content)
    matches = [m[0] if m[0] else m[1] for m in matches]

    if not matches:
        print("No valid 'cn' properties found in the input file.")
        return
    
    if len(extracted_lines) < len(matches):
        print("Warning: Not enough lines in extracted_dialogue.txt to replace all 'cn' entries.")
    
    new_content = content
    for i, old_text in enumerate(matches):
        if i >= len(extracted_lines):
            break  
        
        new_text = extracted_lines[i]
        
        if new_text.startswith("\"") and new_text.endswith("\""):
            new_text = f'[[{new_text}]]'
        
        if new_text.startswith("『") and new_text.endswith("』"):
            new_text = f'[[『{new_text[1:-1]}』]]'  
        

        new_content = re.sub(re.escape(old_text), new_text, new_content, 1)
    

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(new_content)
    
    print(f"Repacking completed! Saved to {output_path}")

input_file = "01_stella_16_1.ast"
output_file = "01_stella_16_1.ast.out"
dialogue_file = "01_stella_16_1.txt"

# Panggil fungsi repack_scenario
repack_scenario(input_file, output_file, dialogue_file)
