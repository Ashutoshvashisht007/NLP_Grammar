import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
class SpellCheckerModule:
    def __init__(self):
        self.grammar_check = language_tool_python.LanguageTool('en-US')
    def correct_spell(self,text):
        matches = tool.check(text)
        
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
    