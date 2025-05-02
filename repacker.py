import re

def repack_scenario(input_path, output_path, dialogue_path):
    with open(input_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Membaca extracted_dialogue.txt
    with open(dialogue_path, "r", encoding="utf-8") as extracted_file:
        extracted_lines = [line.strip() for line in extracted_file.readlines()]
    
    # Regular expression untuk menangkap teks dalam properti cn, termasuk format [[teks]]
    matches = re.findall(r'cn\s*=\s*\{\s*\{\s*(?:\[\[(.*?)\]\]|"([^"]*)")', content)
    matches = [m[0] if m[0] else m[1] for m in matches]  # Ambil teks yang ditemukan

    if not matches:
        print("No valid 'cn' properties found in the input file.")
        return
    
    # Pastikan jumlah baris cukup
    if len(extracted_lines) < len(matches):
        print("Warning: Not enough lines in extracted_dialogue.txt to replace all 'cn' entries.")
    
    # Mengganti setiap cn dengan teks dari extracted_dialogue.txt
    new_content = content
    for i, old_text in enumerate(matches):
        if i >= len(extracted_lines):
            break  # Hentikan jika tidak ada cukup baris
        
        new_text = extracted_lines[i]
        
        # Format ulang jika teks memiliki tanda petik atau sudah dalam bentuk [[teks]]
        if new_text.startswith("\"") and new_text.endswith("\""):
            new_text = f'[[{new_text}]]'
        
        # Cek apakah teks diawali dengan "『" dan diakhiri dengan "』"
        if new_text.startswith("『") and new_text.endswith("』"):
            new_text = f'[[『{new_text[1:-1]}』]]'  # Hilangkan 『 dan 』 sebelum membungkusnya
        
        # Ganti hanya teks dalam CN tanpa merusak format
        new_content = re.sub(re.escape(old_text), new_text, new_content, 1)
    
    # Simpan hasil ke file baru
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(new_content)
    
    print(f"Repacking completed! Saved to {output_path}")

# Tentukan path file
input_file = "01_stella_16_1.ast"
output_file = "01_stella_16_1.ast.out"
dialogue_file = "01_stella_16_1.txt"

# Panggil fungsi repack_scenario
repack_scenario(input_file, output_file, dialogue_file)
