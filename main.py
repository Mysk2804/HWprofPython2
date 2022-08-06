import re
from pprint import pprint
import csv


def contacts():
    with open("phonebook_raw.csv", encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        name_list = []
        new_list = []

        for row in contacts_list:
            joined_rows = ','.join(row[0:3])
            name_list.append(joined_rows)

        for joined_rows in name_list:
            new_row = re.split(r'[, ]', joined_rows)
            new_row = list(filter(None, new_row))
            new_list.append(new_row)
        new_list[-1].append('')

        for row in new_list:
            i = new_list.index(row)
            row.append(contacts_list[i][3])
            row.append(contacts_list[i][4])
            row.append(contacts_list[i][5])
            row.append(contacts_list[i][6])

        phone_pattern = re.compile(
            r'(\+7|8)\s*\(*(495)\)*\s*\-*(\d{3})[-\s*]?(\d{2})[-\s*]?(\d{2})(\s*)\(*(доб.)?\s*(\d{4})?\)*')
        contacts_list2 = []
        for line in new_list:
            line_str = ','.join(line)
            format_line = phone_pattern.sub(r'+7(\2)\3-\4-\5\6\7\8', line_str)
            line_as_list = format_line.split(',')
            contacts_list2.append(line_as_list)
        pprint(contacts_list2)

        contacts_list_updated = []
        for i in new_list:
            for j in new_list:
                if i[0] == j[0] and i[1] == j[1] and i is not j:
                    if i[2] == '':
                        i[2] = j[2]
                    if i[3] == '':
                        i[3] = j[3]
                    if i[4] == '':
                        i[4] = j[4]
                    if i[5] == '':
                        i[5] = j[5]
                    if i[6] == '':
                        i[6] = j[6]
            if i not in contacts_list_updated:
                contacts_list_updated.append(i)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list_updated)



if __name__ == '__main__':
    contacts()