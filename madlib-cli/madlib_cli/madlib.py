print('*************************')
print('*** WELCOME TO MADLIB ***')
print('*************************')
print('')

print('''Read this paragraph and after you finish Enter series of words to fit each of the required components of the following template.Divide your series by comma ',',ex:silly,happy,...

''')

def read_template(path):
    with open(f'{path}','r') as f:
        content=f.read()
        return(content)

def parse_template(text):
    stripped=text.split('{}')
    return stripped
# print(parse_template('It was a {Adjective} and {Adjective} {Noun}.'))

string='It was a {Adjective} and {Adjective} {Noun}.'
arr=''
for item in string :
    if item!='{' and item!='}':
        arr=arr+item
print (arr)
    # expected_stripped = "It was a {} and {} {}."
    # expected_parts = ("Adjective", "Adjective", "Noun")
# mypath='../assets/dark_and_stormy_night_template.txt'
# print(read_template(mypath))

# a,b=['1aa','23f']
# print (a)
# print (b)
# Largeanimal=in
