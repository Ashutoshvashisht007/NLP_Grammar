import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
class SpellCheckerModule:
    def __init__(self):
        self.grammar_check = language_tool_python.LanguageTool('en-US')
    def correct_spell(self,text):
        matches = tool.check(text)
        total_mistakes = len(matches)
        
        # Extract correct words and create a corrected sentence
        corrected_sentence = text
        offset = 0
        for match in reversed(matches):
            start = match.offset
            end = match.offset + match.errorLength
            suggested_replacement = match.replacements[0]
            corrected_sentence = corrected_sentence[:start-offset] + suggested_replacement + corrected_sentence[end-offset:]
            offset += len(match.replacements[0]) - match.errorLength
        
        return corrected_sentence

    def get_total_mistakes_and_suggestions(self, text):
        matches = tool.check(text)
        total_mistakes = len(matches)
        
        mistakes_with_suggestions = []
        for match in matches:
            mistake_info = {
                "Mistake": text[match.offset:match.offset + match.errorLength],
                "Suggested Replacements": match.replacements
            }
            mistakes_with_suggestions.append(mistake_info)
        
        return total_mistakes, mistakes_with_suggestions

if __name__  == "__main__":
    obj = SpellCheckerModule()
    message = "Hello world. I like mashine learning. appple. bananana"
    print(obj.correct_spell(message))
    # example_text = "This is an exampe sentence with somme grammatical errors."
    # example_text = "I have went to the store yesterday."
    # corrected_sentence, total_mistakes = check_grammar(example_text)

    # print(f'Total Mistakes: {total_mistakes}')
    # print(f'Corrected Sentence: {corrected_sentence}')

    # text = 'I am trying to install gingerit in my VS Code but it\'s giving an error'
    # matches = tool.check(text)

    # print(matches)

    # print(obj.correct_grammar(message))