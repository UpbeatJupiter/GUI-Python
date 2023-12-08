# Supports both hardcoded language strings and external language files.

import glob

class I18N:
    def __init__(self, language, load_from_file=True):
        if load_from_file:
            if language in self.get_available_languages():
                self.load_data_from_file(language)
            else:
                raise NotImplementedError("Unsupported language. Add missing language file.")
        else:
            if language == "en":
                self.load_data_in_english()
            elif language == "tr":
                self.load_data_in_turkish()
            else:
                raise NotImplementedError("Unsupported language.")

    def load_data_in_english(self):
        self.title = "Week 11"
        self.fname = "Name"
        self.lname = "Surname"
        self.grade = "Grade"
        self.update = "Update"

    def load_data_in_turkish(self):
        self.title = "Hafta 11"
        self.fname = "Ad"
        self.lname = "Soyad"
        self.grade = "Not"
        self.update = "Güncelle"

    def load_data_from_file(self, lang):
        lang_data = {}
        lang_file = f"data_{lang}.lng"
        with open(file=lang_file, encoding="utf-8") as f:
            for line in f:
                (key, val) = line.strip().split("=")
                lang_data[key] = val

        self.title = lang_data["title"]
        self.fname = lang_data["fname"]
        self.lname = lang_data["lname"]
        self.grade = lang_data["grade"]
        self.update = lang_data["update"]

    @staticmethod
    def get_available_languages():
        language_files = glob.glob("*.lng")
        language_codes = []

        for f in language_files:
            language_code = f.replace("data_", "").replace(".lng", "")
            language_codes.append(language_code)

        return language_codes
