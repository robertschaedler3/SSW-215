"""
    PigLatin Translator
    Robert Schaedler III
"""


def get_sents(inputString):
    return inputString.split('.')


def get_words(sentance):
    return sentance.split()


def translate(word):
    if word[0] in vowels:
        return word + "way "
    else:
        beg = ''
        for c in word:
            if c not in vowels:
                beg += c
            else:
                break

        end = word[len(beg):]

        return end + beg + "ay "


def translate_with_hyphen(word):
    parts = word.split(hyphen)
    translatedParts = ''

    # Translate each part separately as words
    for part in parts:
        translatedParts += translate(part)

    return translatedParts.replace(' ', '-')[:-1] + ' '


def expand_contraction(word):
    contractions = {
        "n't": [word[:-3], "not"],
        "'ll": [word[:-3], "will"],
        "'s": [word[:-2], "is"],
        "'ve": [word[:-2], "have"],
        "'d": [word[:-2], "would"],
        "'m": [word[:-2], "am"]
    }
    for contraction in contractions:
        if contraction in word:
            return contractions.get(contraction)  # Known contraction

    return [word]  # Not a known contraction


if __name__ == '__main__':

    print("Type 'exit()' to exit.")

    vowels = 'aeiou'
    apostrophe = "'"
    hyphen = '-'

    while(True):

        inputString = input(
            "Translate to PigLatin: ").lower()  # Get user input
        if(inputString == "exit()"):
            break

        output = ''

        # Break the input into sentances
        if '.' in inputString and '.' in inputString[:-1]:
            if inputString.endswith('.'):
                sents = get_sents(inputString[:-1])
            else:
                sents = get_sents(inputString)
        else:
            sents = [inputString[:-1]]

        # Break the sentances into words
        for sent in sents:
            words = get_words(sent)

            # Process each word
            for word in words:

                # Process contractions
                if apostrophe in word:
                    expandedWords = expand_contraction(word)
                    for expandedWord in expandedWords:
                        output += translate(expandedWord)

                # Process hypenated words
                elif hyphen in word:
                    output += translate_with_hyphen(word)

                # Process as normal word
                else:
                    output += translate(word)

            # Remove trailing space and add a period at the end of each sentance
            output = output[:-1] + '. '

        print(f'\n{output[:-1]}\n')
