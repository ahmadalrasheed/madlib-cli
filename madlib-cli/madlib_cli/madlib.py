import re

print('*************************')
print('*** WELCOME TO MADLIB ***')
print('*************************')
print('')

print('''In this game you will enter many words and we will create for you a paragraph with the words you choosed!.

''')
input_words=["Adjective","Adjective","A First Name","Past Tense Verb","A First Name","Adjective","Adjective","Plural Noun","Large Animal","Small Animal","A Girl's Name","Adjective","Plural Noun","Adjective","Plural Noun","Number 1-50","First Name's","Number","Plural Noun","Number","Plural Noun"]

output_words=[]


def read_template(path):
    """
    this fucntion is responsible of reading the Template Given so the user can enter the input
    """

    with open(f'{path}','r') as f:
        content=f.read()
        return(content)


def parse_template(text):
    spilt_file_list=re.findall(r"\{(.*?)\}",text)
    # print(spilt_file_list)
    spilt_text=re.sub(r"\{(.*?)\}","{}",text)
    # print(spilt_text)
    return spilt_text,tuple(i for i in spilt_file_list)

# print(parse_template('It was a {Adjective} and {Adjective} {Noun}.'))


   
def merge_file(bare_string,reg):
    # print(bare_string)
    return str(bare_string).format(*reg)




def create_txt(content):
    with open('../assets/text_game_copy.txt','w') as f:
        f.write(content)
    # return



if __name__=="__main__":
    for i in input_words:
        msg=input("please enter a :"+i+">>")
        output_words.append(msg)

    string=read_template("../assets/template.txt")
    bare_string,word_list=parse_template(string)

    # print(bare_string)
    # print(word_list)
    # print(word_list)
    # print(output_words)

    user_output=tuple(i for i in output_words)
    user_content=merge_file(bare_string,user_output)
    print(user_content)
    create_txt(user_content)

    # print(bare_string)
    # merge_file(bare_string,output_words)

    # expected_stripped = "It was a {} and {} {}."
    # expected_parts = ("Adjective", "Adjective", "Noun")
# mypath='../assets/dark_and_stormy_night_template.txt'
# print(read_template(mypath))

# a,b=['1aa','23f']
# print (a)
# print (b)
# Largeanimal=in
