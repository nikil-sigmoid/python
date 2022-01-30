# Youtube tutorial
# https://www.youtube.com/watch?v=g8u0wLvvPSs&t=748s
# Official documentation on regex
# https://docs.python.org/3/library/re.html


# findall: It finds all searches for matches and prints resultant in the form of a list.
# search: It works the same as a findall, but the resultant is a matched object if any is found.
# split: The split function splits the string from every matched into two new strings.
# sub: The sub-function works exactly like a replace function in notepad or MS Word.
#      It replaces the original word with a word of our choice.
# finditer: The finditer yields an iterator as a resultant with all the objects that
#           match the one we sent it) finditer supports more attributes than any other
#            function defined above. It also provides more details related to the matched object.
#            So, most of the examples we are going to see next will contain a finditer function in them.


import re
mystr = '''Clive Finkelstein is acknowledged as the "Father" of information 
technology engineering,[4][5] having developed its concepts from 1976 to 1980 
based on original work carried out by him to bridge from strategic business 
planning to information systems. He wrote the first publication on information 
technology engineering: a series of six in depth articles of the same name 
published by US Computerworld in May – June 1981. He also co-authored with 
James Martin the influential Savant Institute Report titled: "Information Engineering", 
published in Nov 1981. The Finkelstein thread evolved from 1976 as the business driven 
variant of ITE. The Martin thread evolved into the data processing-driven (DP) variant 
of ITE. From 1983 till 1986 ITE evolved further into a stronger business-driven variant 
of ITE, which was intended to address a rapidly changing business environment. The then 
technical director, Charles M. Richter, from 1983 to 1987, guided by Clive Finkelstein, 
played a significant role by revamping the ITE methodology as well as helping to design 
the ITE software product (user-data) which helped automate the ITE methodology, opening 
the way to next generation Information 22209-1911  aiaiiiaiaiaiaiaiiiiaiaiiii Architecture.'''


# findall, search, split, sub, finditer

# r indicates raw string, which doesn't recognise escape characters, etc.

# refer re.txt

# patt = re.compile(r'.')
# patt = re.compile(r'.iv')
# patt = re.compile(r'^Clive')
# patt = re.compile(r'ure.$')
# patt = re.compile(r'ai*')
# patt = re.compile(r'a*i*')
# patt = re.compile(r'ai+')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){2}')
# patt = re.compile(r'ai{1}|ITE')



# Special Sequences
# patt = re.compile(r'\AClive')

# patt = re.compile(r'ITE\b')

patt = re.compile(r'\d{5}-\d{4}')

matches = patt.finditer(mystr)

for match in matches:
    print(match)
    print(mystr[448:452])
