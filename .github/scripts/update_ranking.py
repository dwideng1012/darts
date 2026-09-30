import json, os, sys

src, dst, now = sys.argv[1], sys.argv[2], sys.argv[3]

with open(src, encoding='utf-8') as f:
    raw = json.load(f)

assert isinstance(raw.get('data'), list), 'Missing data array in response'
new_data = raw['data']

try:
    with open(dst, encoding='utf-8') as f:
        existing = json.load(f)
    if existing.get('data') == new_data:
        print('Data unchanged, skipping write.')
        sys.exit(0)
except (FileNotFoundError, json.JSONDecodeError):
    pass

result = {'updated': now, 'data': new_data}
tmp = dst + '.tmp'
with open(tmp, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, separators=(',', ':'))
os.replace(tmp, dst)
print('Data changed, wrote new file.')
