import requests
import json
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

# Connect the path with your '.env' file name
class UserConfig:
    def __init__(self, src_lang, target_lang):
        self.src_lang
        self.target_lang
class Connection:
    def __init__(self, api_root, id, secret):
        self.api_root = api_root
        self.id = id
        self.secret = secret
    def get_headers(self):
        pass
    def get_base_url(self):
        return self.api_root

class OxfordConnection(Connection):
    def __init__(self, api_root, id, secret):
        super().__init__(api_root, id, secret)
    def get_headers(self):
        return {"app_id": self.id, "app_key": self.secret}



class Word:
    def __init__( self, word, src_lang, target_lang, Conn ):
        self.api_headers = Conn.get_headers()
        self.base_url = Conn.get_base_url()
        self.word = word
        self.src_lang = src_lang
        self.target_lang = target_lang

    def get_word_data(self, rev = 0):
        lang_1, lang_2 = self.set_local_src_and_target_lang(rev)
        print(lang_1)
        url = f"{self.base_url}/entries/{lang_1}/{self.word.lower()}"
        res = requests.get(url, headers=self.api_headers)
        print(res)
        return res.json()

    def set_local_src_and_target_lang(self, rev = 0):
        if rev:
           return (self.target_lang, self.src_lang)
        else:
           return (self.src_lang, self.target_lang)

    def get_trans(self, rev = 0):
        lang_1, lang_2 = self.set_local_src_and_target_lang(rev)
        url = f"{self.base_url}/translations/{lang_1}/{lang_2}/{self.word}"
        res = requests.get(url, headers=self.api_headers)
        return res.json()



c = OxfordConnection("https://od-api.oxforddictionaries.com:443/api/v2", os.getenv("OXFORD_ID"), os.getenv("OXFORD_SECRET"))
word = Word(word = "example", src_lang = 'en-gb', target_lang = 'es', Conn = c)
d = word.get_word_data()
trans = word.get_trans()
#
print(json.dumps(trans, indent = 4))