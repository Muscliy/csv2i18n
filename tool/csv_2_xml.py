import pandas as pd
import json
import sys
import shutil
import re

shorthand = {
  'English': 'pipay_strings_en',
  'Chinese': 'pipay_strings_cn'
}

def init_xml_file(xml_data):
  xml_data.write('<?xml version="1.0" encoding="utf-8"?>' + "\n")
  xml_data.write('<resources>' + "\n")

def close_xml_file(xml_data):
  xml_data.write('</resources>' + "\n")
  xml_data.close()



def transfer():
  print("start transfer 2 xml")
  csv_file = '{path}/{name}.csv'.format(path='./',  name=sys.argv[1])
  df = pd.read_csv(csv_file, encoding='utf-8')
  for l, s in shorthand.items():
    path='./'
    xml_file = '{path}/{name}.xml'.format(path=path, name=s)
    xml_data = open(xml_file, 'w')
    init_xml_file(xml_data);
    result = {}
    _df = df[['Key', l]]
    _df.dropna(inplace=True)
    for index, row in _df.iterrows():
      name=row['Key'].strip()
      value=re.sub("{{[^{}]*}}", '%s', row[l])
      value=re.sub("\'", '\\\'', value)
      value=re.sub("&", '&amp;', value)
      xml_data.write('    <string name=\"'  + name + '\">' + value + '</string>' + "\n")
    close_xml_file(xml_data)

if __name__ == "__main__":
  transfer()
