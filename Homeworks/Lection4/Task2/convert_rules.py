def CSV(line):
    if line == "\n": line = ""
    else:
        line = line.replace("\t", ";")
    return line

def HTML(line):
    if line == "\n": line = ""
    else:
        line = "<tr color:><td>" + line.replace("\t", "</td><td>") + "</td></tr>\n"
    return line