import os
import json
from pprint import pprint


def data_transform(file_name: str):
    global counter
    print(file_name)
    with open(file_name, 'r') as fhandle:
        raw = fhandle.read().strip().split('\n')
    headers = tuple(header.strip() for header in raw[0].strip().split(','))
    data_output = list()
    for row in raw[1:]:
        counter += 1
        temp = {'ROW_ID': counter}
        row = tuple(field.strip() for field in row.strip().split(','))
        if len(row) == len(headers):
            for indx in range(len(headers)):
                if row[indx] != 'NULL':
                    if row[indx] != 'PrivacySuppressed':
                        try:
                            ent = float(row[indx])
                        except ValueError:
                            temp[headers[indx]] = row[indx]
                        else:
                            if ent % 1 == 0:
                                ent = int(ent)
                            temp[headers[indx]] = ent
            data_output.append(temp)
    return data_output


def get_data_info(dt: list):
    # Get headers and their uniques values
    headers = dict()
    for line in dt:
        for key in line:
            if key not in headers:
                headers[key] = {line[key]}
            elif key in headers:
                headers[key].add(line[key])
    # Get header data types
    headers_type = dict((hd, set(type(entry) for entry in headers[hd])) for hd in headers)
    # Get all possible types variants
    type_set = set(tuple(headers_type[types]) for types in headers_type)
    return {'headers': headers, 'headers_type': headers_type, 'type_set': type_set}


if __name__ == '__main__':
    counter = 0
    os.chdir('/home/windr/ResilioSync/GitHub/CS593-Final-Project/CollegeScorecard_Raw_Data/')
    all_data = list(row for file in sorted(os.listdir('./')) if file.endswith('_PP.csv')
                    for row in data_transform(file))
    # Get headers info
    data_info = get_data_info(all_data)
    # Print total rows & total columns
    print(len(all_data))
    print(len(data_info['headers']))
    # Transform data
    for i in range(len(all_data)):
        for head in all_data[i]:
            if type(float()) in data_info['headers_type'][head]:
                all_data[i][head] = float(all_data[i][head])
            elif type(str()) in data_info['headers_type'][head]:
                all_data[i][head] = str(all_data[i][head])
    # Print type_set
    pprint(get_data_info(all_data)['type_set'])
    # Write data to file
    with open('/home/windr/CS593_Data/all_data.json', 'w') as fh:
        json.dump(all_data, fh)
