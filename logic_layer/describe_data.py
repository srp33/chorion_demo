with open("/data.tsv") as data_file:
    lines = data_file.readlines()

    print(f"The file has {len(lines)} of text.")
    print(f"The first line has {len(lines[0])} elements.")
