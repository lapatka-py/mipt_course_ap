import re

def write_array(array, file):
    # записывает строки в список
    with open(file, 'a') as f:
        array = map(lambda x: x + '\n', array)
        f.writelines(array)
    pass


file_name = str(input())
text = []
s = re.sub(r'\s+', ' ', input(), flags=re.M)
for s in re.split(r'(?<=[.!?…]) ', s):
    text.append(s)
write_array(text, file_name)
