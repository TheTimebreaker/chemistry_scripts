import pyperclip, re, requests

print('Requesting GHS statement list... ', end='')
ghs_text = requests.get('https://pubchem.ncbi.nlm.nih.gov/ghs/ghscode_10.txt').text
ghs_lines = [line for line in ghs_text.split('\n') if line]
ghs_dict = {}
for line in ghs_lines:
    elements = line.split('\t')
    code, statement = elements[0], elements[1]
    ghs_dict[code] = statement
print('DONE!')


inputhp = str(input('Please enter string with H or P statements as numbers (e.g. H225, H226, P210, etc). Can be seperated by ;,\\n:'))
statements_numbers = re.split('; |;|, |,|\n', inputhp)
statements_full = {}
for statement_number in statements_numbers:
    statements_full[statement_number] = ghs_dict[statement_number]

outstrs = []
for code, statement in statements_full.items():
    line = f'{code}: {statement}'
    outstrs.append(line)

outstr = '\n'.join(outstrs)
pyperclip.copy(outstr)
print(outstr)