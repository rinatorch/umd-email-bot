#natural language processing attempts
nltk_results = ne_chunk(pos_tag(word_tokenize("")))
for nltk_result in nltk_results:
    if type(nltk_result) == Tree:
        name = ''
        for nltk_result_leaf in nltk_result.leaves():
            name += nltk_result_leaf[0] + ' '
        print ('Type: ', nltk_result.label(), 'Name: ', name)
        keywords_list.append(name)

print(keywords_list)

#more natural language processing attempts
def extract_entities(text):
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'node'):
                 print(chunk.node, ' '.join(c[0] for c in chunk.leaves()))
    keywords_list.append(c[0] for c in chunk.leaves())
extract_entities(msg)
print(keywords_list)

#attempting to print just the email signature
second_list = []
for url in url_list:
    single_msg_page = requests.get(url)
    soup = bs4.BeautifulSoup(single_msg_page.text, 'html.parser')
    signature = soup.find_all('umd-signature')
    text_list.append(signature)
    for x in text_list:
        capture_sig = x.find_all('p')
        print(capture_sig)
            #print(signature)
        second_list.append(capture_sig)
    #print(this)

    for signature in url:
        text_list.append(signature)

    for x in signature:
        capture_sig = x.find_all('p')
        print(capture_sig)
        #print(signature)
        text_list.append(capture_sig)

    sig_text = soup.find_all('div', class_="rich-text")
    if sig_text in signature:
        text_list.append(sig_text)
    else:
        pass

print(text_list)

#attempting to create an extra csv to build out a database
this = df.to_dict('records')
for item in this:
    print(item)
    #urls = []
    urls = item['URL']
    #if item not in urls:
        #urls.append(item['URL'])
    if URL not in urls:
        this.append(item)
    print(urls)
print(this)
#print(this.keys())

for dict in this:
    print(this.get('URL'))
#print(this['URL'])

for item in this:
    if URL not in this:
        this.append(item['Date'])
    if URL in this:
        pass
    df.to_csv('main.csv')

#extracting text of each email
text_list = []
for url in url_list:
    single_msg_page = requests.get(url)
    soup = bs4.BeautifulSoup(single_msg_page.text, 'html.parser')
    body_text = soup.find_all('section', id='section-body-text')
    for bodies in body_text:
        bodies = bodies.text
        bodies = re.sub("\n","",str(bodies))
        text_list.append(bodies)
        #print(bodies)
    #print(body_text)
    #for body_text
