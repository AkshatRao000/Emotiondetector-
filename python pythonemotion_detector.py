import os

# ====== 1. Folder aur File ka Naam ======
folder_name = "emotion_data"
file_name = "emotion_dataset.csv"
file_path = os.path.join(folder_name, file_name)

# ====== 2. Folder Banaao (Agar Nahi Hai Toh) ======
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' bana diya gaya.")
else:
    print(f"Folder '{folder_name}' already exist karta hai.")

# ====== 3. File Content (Sample Data) ======
content = """text,emotion
I am happy,happy
I am sad,sad
I am angry,angry
I am surprised,surprised
I am scared,fear
"""

# ====== 4. File Banaao Aur Data Likho ======
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"File '{file_path}' bana di gayi aur data likh diya gaya.")

# ====== 5. Output Dikhana (Optional) ======
print("\nFile ka content:")
with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())
