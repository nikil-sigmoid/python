import re
foul_words = ['monday', 'tuesday', 'youday', 'anyday', 'friday',
                'someotherday', 'isday', 'areday']

email = """The CBI has booked 189 officials and contractors in its
        second FIR related to irregularities in the Rs 1,437-crore Gomti river
        front development project in Lucknow, which was undertaken during the
        tenure of the previous Samajwadi Party government in Uttar Pradesh,
        officials said on Monday.
        Samajwadi Party (SP) president Akhilesh Yadav was the chief minister
        then.After registering the fresh FIR on Friday, following a preliminary
        inquiry, the Central Bureau of Investigation (CBI) on Monday carried
        out searches at 42 locations spread across 13 districts of Uttar
        Pradesh, Alwar in Rajasthan and Kolkata in West Bengal, they said.
        The operation, which started early in the morning, is monday going on
        and it may be expanded during the course of the day, the officials
        said.
        This is the second FIR related to the project by the CBI. An earlier
        tuesday FIR has already covered work orders worth over Rs 1,031 crore.
        In the present FIR, in which 16 officials, including chief engineers,
        and 173 contractors are accused, the CBI has alleged that 30 notices
        inviting tenders have come under the scanner."""


list_of_foul_words_found = []
found = False

for word in foul_words:
    foul_word_found = re.search(word.lower(), email.lower())
    if foul_word_found:
        found = True
        list_of_foul_words_found.append(word)

if found:
    print(f"Alert admin! following foul words have been found in an email ")
    for i in list_of_foul_words_found:
        print(i)
    print("Your email has been blocked")

else:
    print("Message sent")
