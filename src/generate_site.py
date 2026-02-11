def extract_title(markdown):
    split_md = markdown.split("\n")
    for line in split_md:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise Exception(f"No title found in provided markdown: {markdown}")