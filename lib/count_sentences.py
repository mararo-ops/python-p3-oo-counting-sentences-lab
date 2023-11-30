class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace common punctuation with periods and split the string
        sentences = self.value.replace('?', '.').replace('!', '.').split('.')
        
        # Remove empty strings from the list
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        
        return len(sentences)



