def get_num_words(contents):
    return len(contents.split())

def get_num_character(contents):
    characters = {}

    for i in contents:
        char = i.lower()
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

    return characters

def sort_on(character):
    return character["count"]
def sort_characters(characters):
    characters_list = []
    for character in characters:
        characters_list.append({"name":character, "count":characters[character]})

    characters_list.sort(reverse=True, key=sort_on)
    return characters_list