import pandas as pd
import json
import sys
import shutil
import re


shorthand = {
  'English': 'en',
  'Chinese': 'zh-CN'
}

def transfer():
  print("start transfer 2 json")
  csv_file = '{path}/{name}.csv'.format(path='./', name=sys.argv[1])

  df = pd.read_csv(csv_file, encoding='utf-8')
  for l, s in shorthand.items():
    result = {}
    _df = df[['Key', l]]
    _df.dropna(inplace=True)
    for index, row in _df.iterrows():
      matches = re.findall("{{[^{}]*}}", row[l])
      str = row[l]
      for j in range(len(matches)):
        replace = "{"+bytes(j)+"}"
        str = re.sub("{{[^{}]*}}", replace, str, 1)
      result[row['Key'].strip()] = str
    save_to_assets(s, result)

def save_to_assets(file_name, content):
  path='./'
  with open('{path}/{file}'.format(path = path, file = file_name + '.json'), 'w') as f:
    f.write(json.dumps(content, indent=2, sort_keys=True, ensure_ascii=False))

if __name__ == "__main__":
  transfer()
