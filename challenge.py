# 1
# Function to add prefix 'un' to inputted word.
def add_prefix_un(x):
    y= x.lower().strip(' ')
    print('un' + y)

add_prefix_un("happy")
add_prefix_un("manageable")

# 2
# Function that adds first iput as prefix for second, third and fourth inputs.
def make_word_groups(x):
    z = []
    for i in x:
        if i == x[0]:
            y = i
        else:
            word = (x[0] + i)
            z.append(word)
    print(f"{y} :: {z[0]} :: {z[1]} :: {z[2]}")

make_word_groups(['en', 'close', 'joy', 'lighten'])
make_word_groups(['pre', 'serve', 'dispose', 'position'])
make_word_groups(['auto', 'didactic', 'graph', 'mate'])
make_word_groups(['inter', 'twine', 'connected', 'dependent'])

# 3 
# Function to remove suffix 'ness' from input.
def remove_suffix_ness(x):
    if x[-4:] == 'ness':
        y = x[0:-4]
        if y[-1] == 'i':
            y = y.replace("i", "y")
        print (y)
    else:
        return

remove_suffix_ness('heaviness')
remove_suffix_ness('sadness')

# 4
# Function to turn inputted adjective to a verb.
def adjective_to_verb(x, y):
    words = x.strip('.').split()
    print (words)
    for word in words:
        z = words[y] + 'en'
    print (z)

adjective_to_verb('I need to make that bright.', -1)
adjective_to_verb('It got dark as the sun set.', 2)
     
