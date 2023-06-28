import json

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def processor():

    source_file = open('./source/tile.json')

    source_data = json.load(source_file)

    file_to_generate = open("./source_documents/tiles.txt", "w")

    lines = [
        remove_html_tags(source_data['title']), 
        remove_html_tags(source_data['introduction']), 
        remove_html_tags(source_data['prerequisite']) 
    ]

    file_to_generate.writelines(lines)

    file_to_generate.close()

processor()

