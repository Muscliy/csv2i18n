import os
import sys
import csv_2_json
import csv_2_strings
import csv_2_xml
from shutil import copyfile

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'leehu'

def convert_csv():
  file_name = sys.argv[1]
  paltform = sys.argv[2].lower()
  if paltform == 'json':
    csv_2_json.transfer()
  elif paltform == 'strings':
    csv_2_strings.transfer()
  elif paltform == 'xml':
    csv_2_xml.transfer()
  else:
    raise RuntimeError('no platform cant match translator')

if __name__ == "__main__":
  convert_csv()
