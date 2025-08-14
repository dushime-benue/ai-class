# craeting gict
contact_book ={'ben':'099999877','cyber':'098777666','leon':'0997543657','dan':'08876453'}
contact_book['paul']='990877654'
contact_book['queen']='088976512'

# deleting iterm in dictionary
print(contact_book)

menu={'pizza':'12.99','salad':'6.99','fish':'10.99'}
del menu['salad']
print(menu)

# looping in dictionary
for iterm in contact_book.keys():
    print(iterm)
for things in contact_book.values():
    print(things)

    # loop throught key-value
    for iterm, things in contact_book.items():
        print(f'{iterm}:{things}')
