# import sys
#
# #python text_compare.py ./output/TC1-1/TC1-1.cmty ./old_output/TC1-1/TC1-1.cmty
# #python text_compare.py ./output/2TC1-1/TC1-1.cmty ./output/1TC1-1/TC1-1.cmty
# def compare_files(file1_path, file2_path):
#     try:
#         with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
#             file1_content = file1.read()
#             file2_content = file2.read()
#
#         if file1_content == file2_content:
#             print("The files are identical.")
#         else:
#             print("The files are different.")
#
#     except FileNotFoundError as e:
#         print(f"Error: {e}")
#
#
# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python compare_files.py <file1_path> <file2_path>")
#     else:
#         file1_path = sys.argv[1]
#         file2_path = sys.argv[2]
#         compare_files(file1_path, file2_path)
import sys

def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
            file1_lines = file1.readlines()
            file2_lines = file2.readlines()

        identical = True
        max_lines = max(len(file1_lines), len(file2_lines))

        for i in range(max_lines):
            if i < len(file1_lines) and i < len(file2_lines):
                if file1_lines[i] != file2_lines[i]:
                    print(f"Difference at line {i + 1}:")
                    print(f"File 1: {file1_lines[i].rstrip()}")
                    print(f"File 2: {file2_lines[i].rstrip()}")
                    identical = False
            elif i < len(file1_lines):
                print(f"Extra line in file 1 at line {i + 1}: {file1_lines[i].rstrip()}")
                identical = False
            elif i < len(file2_lines):
                print(f"Extra line in file 2 at line {i + 1}: {file2_lines[i].rstrip()}")
                identical = False

        if identical:
            print("The files are identical.")
        else:
            print("The files are different.")

    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_files.py <file1_path> <file2_path>")
    else:
        file1_path = sys.argv[1]
        file2_path = sys.argv[2]
        compare_files(file1_path, file2_path)
