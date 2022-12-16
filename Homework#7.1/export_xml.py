def create_export(data):

    with open('export.csv', 'a') as file:
        for elem in data:
            stringa = ""
            for contact_info in elem:
                stringa =+ (" "+ contact_info + ";")
            file.write(stringa[1:])
            file.write("\n")

