from enum import unique

country_codes = {'PS':'970', 'Canada':'1', 'Turkey':'90'}

print(country_codes['Turkey'])

country_codes.update({'Jordan':'962', 'Qatar': '974'})
print(country_codes)
#unique 
text = "My name is Fatoom, I live in Gaza . Gaza is a nice city in Palestine. Palestine is a nice country in Middle East"
tokens = text.split(' ')
unique_tokens = set(tokens)
dict = {}
for token in unique_tokens:
    dict[token] = tokens.count(token)
    print('"', token, '"', ':',dict[token])