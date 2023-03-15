def get_text_from_file(file_path):
    with open(file_path) as file:
        text = file.readlines()
        string = ''
        for line in text:
            string += line.rstrip()
        return string