file_path = "/data.tsv"

with open(file_path) as data_file:
    lines = data_file.readlines()

    print(f"The {file_path} file has {len(lines)} of text.")
    print(f"The first line has {len(lines[0])} elements...")
