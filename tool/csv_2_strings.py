import pandas as pd
import json
import sys
import shutil
import re

shorthand = {
  'English': 'en',
  'Chinese': 'cn'
}

def transfer():
  print("start transfer 2 strings")
  csv_file = '{path}/{name}.csv'.format(path='./', name=sys.argv[1])
  df = pd.read_csv(csv_file, encoding='utf-8')
  for l, s in shorthand.items():
    path='./'
    string_file = '{path}/{name}.strings'.format(path=path, name=s)
    strings_data = open(string_file, 'w')
    _df = df[['Key', l]]
    _df.dropna(inplace=True)
    for index, row in _df.iterrows():
      name=row['Key'].strip()
      value=re.sub("{{[^{}]*}}", '%s', row[l])
      strings_data.write( "\""+ name + "\"" + " = " + "\"" + value + "\"" + ";\n")
    strings_data.close()

if __name__ == "__main__":
  transfer()
