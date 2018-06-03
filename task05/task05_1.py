import argparse
from ftplib import FTP
import gzip
import os


parser = argparse.ArgumentParser()
parser.add_argument('--download',
                    help='URL of the file',
                    default='ftp.fu-berlin.de/pub/misc/'
                            'movies/database/frozendata/'
                            'ratings.list.gz')

args = parser.parse_args()

url = args.download
file_address = url.split('/')[0]
file_path = url[url.find('/'):url.rfind('/'):]
file_full_name = url.split('/')[-1]
file_name = file_full_name[:file_full_name.rfind('.')]

try:
    if not os.path.isfile(file_full_name):
        with FTP(file_address, timeout=100) as ftp:
            ftp.login()
            ftp.cwd(file_path)
            ftp.retrbinary("RETR {full_file_name}"
                           .format(full_file_name=file_full_name),
                           open(file_full_name, 'wb').write)

        with gzip.GzipFile(file_full_name, 'rb') as input_file:
            s = input_file.read()

        with open("{file_name}.txt".format(file_name=file_name), 'wb') \
                as output_file:
            output_file.write(s)
except TimeoutError:
    print("Server not response")
