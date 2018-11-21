#!/usr/bin/python3
import os

path = '/Users/Jesse/Dropbox/Familia/include/familia'

paths = []
for dir_name, dir_names, filenames in os.walk(os.path.expanduser(path)):
  for filename in filenames:
    paths.append(os.path.join(dir_name, filename))

chinese_lines = []
for path in paths:
  with open(path) as f:
    text = f.read()
  for line in text.splitlines():
    for ch in line:
      if ord(ch) >= 135:
        chinese_lines.append(line)
        break

with open('out.txt', 'w') as f:
  f.write('\n'.join(chinese_lines))

# // 采样器的接口
# 47 47 32 233 135 135 230 160 183 229 153 168 231 154 132 230 142 165 229 143 163

