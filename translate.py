from translate import Translator
if __name__ == "_main_":
    pass
from translate import Translator
def translate_text(text,target_language='en'):
    translator =Translator(to_lang=target_language)
    translated_text =translator.translate(text)
    return translated_text
if __name__ == "_main_":
    input_text = input("Enter the text to translate:")
    target_language = input("Enter the target language (e.g., 'en' for English, 'fr' for French): ")
    translated_text =translate_text(input_text, target_language)
    print("Translated text:",translated_text)