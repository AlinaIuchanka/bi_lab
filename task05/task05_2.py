import argparse
import csv
import json
import urllib.request
import xmltodict
import yaml


def convert_csv(file_name, info):
    with open(file_name + '.csv', 'w') as file:
        writer = csv.writer(file)
        for key, value in info.items():
            writer.writerow([key, value])


def convert_xml(file_name, info):
    with open(file_name + '.xml', 'w') as file:
        xml_string = xmltodict.unparse(info, pretty=True)
        file.write(xml_string)


def convert_json(file_name, info):
    with open(file_name + '.json', 'w') as file:
        json.dump(info, file)


def convert_yaml(file_name, info):
    with open(file_name + '.yml', 'w') as file:
        yaml.dump(info, file, default_flow_style=False)


parser = argparse.ArgumentParser()

parser.add_argument('--download',
                    help='URL of the file',
                    default='https://transit.land/api/v1')
# json
# https://transit.land/api/v1

# xml
# https://www.w3schools.com/xml/plant_catalog.xml

parser.add_argument('--format',
                    help='Downloaded file format',
                    default='json')

args = parser.parse_args()
download_url = args.download
file_format = args.format

content = urllib.request.urlopen(download_url)
data = ""

if file_format == 'yml':
    data = yaml.load(content.read())
elif file_format == 'json':
    data = json.loads(content.read())
elif file_format == 'xml':
    data = xmltodict.parse(content.read())

convert_yaml('output', data)
convert_json('output', data)
convert_xml('output', data)
convert_csv('output', data)
