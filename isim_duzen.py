import os
import re

def fix_png_sorting(folder_path):
    print("Dosya isimleri düzeltiliyor, lütfen bekleyin...")
    count = 0
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".png"):
                # Sayı aralığını tespit eder (Örn: _1-25.png veya _26-50.png)
                match = re.search(r'_(\d+)-(\d+)\.png$', file)
                if match:
                    start_num = int(match.group(1))
                    end_num = int(match.group(2))
                    
                    
                    new_file = re.sub(
                        r'_(\d+)-(\d+)\.png$', 
                        f'_{start_num:03d}-{end_num:03d}.png', 
                        file
                    )
                    
                    old_path = os.path.join(root, file)
                    new_path = os.path.join(root, new_file)
                    
                    if old_path != new_path:
                        os.rename(old_path, new_path)
                        count += 1

    print(f"ok.")

fix_png_sorting(r"C:\Users\burak\Documents\GitHub\yks-grafik-arsivi-2018-2025\Bölüme Göre Sıralanmış (1274 Sayfa, 21602 Grafik)")