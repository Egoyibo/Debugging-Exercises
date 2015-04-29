def remove_html_markup(s):
    tag = False
    quote = False
    output = ""

    for char in s:
        if char == '<':
            tag = True
        elif char == '>':
            tag = False
        elif char == '"' or char =="'" and tag:
            quote = not quote
        elif not tag:
            output = output + char
    return output