import os
from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    """
    extract_title is a method that extracts the title from a markdown file
    
    :param markdown: Markdown file
    """
    split_md = markdown.split("\n")
    for line in split_md:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise ValueError(f"No title found in provided markdown: {markdown}")

def generate_page(from_path, template_path, dest_path, basepath):
    """
    generate_page is a method that generates a website
    
    :param from_path: Where the page you want to generate is located
    :param template_path: Where the HTML template is located
    :param dest_path: Where you want the generated html file to be located
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as f:
        html_temp = f.read()
    # create the html
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)
    updated_html = html_temp.replace("{{ Title }}", title).replace("{{ Content }}", html)
    updated_href_src = updated_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    destination_path = os.path.dirname(dest_path)
    os.makedirs(destination_path, exist_ok = True)
    with open(dest_path, 'w') as f1:
        f1.write(updated_href_src)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    """
    generate_pages_recursive is a method that generates multiple pages recursively
    
    :param dir_path_content: the directory name
    :param template_path: path of the template
    :param dest_dir_path: path of the destination
    """
    
    # list out everything
    if not os.path.isfile(dir_path_content):
        contents = os.listdir(dir_path_content)
        for item in contents:
            item_path = os.path.join(dir_path_content, item)
            if not os.path.isfile(item_path):
                generate_pages_recursive(item_path, template_path, dest_dir_path, basepath)
            else:
                if item.endswith(".md"):
                    # build dest path
                    item_rel = item_path[8:]
                    html_dest_path = os.path.join(dest_dir_path, f"{item_rel[:-3]}.html")
                    generate_page(item_path, template_path, html_dest_path, basepath)
