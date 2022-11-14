import requests

from errors import NoConjugationSupport, UnidentifiedCommand


class OxfordDictionary:

    def __init__(self, base_url, api_id, api_secret):
        """Stores API related info for oxford dict.

        @param base_url: Base part of the URL for API requests
        @type base_url: str
        @param api_id: Oxford dictionary API key
        @type api_id: str
        @param api_secret: Oxford Dict. API secret
        @type api_secret: str
        """
        self.base_url = base_url
        self.__headers = {"app_id": api_id, "app_key": api_secret}

    def get_translation_url(self, w, lang_1, lang_2):
        return f"{self.base_url}/translations/{lang_1}/{lang_2}/{w}"

    def get_entry_url(self, w, lang_1):
        return f"{self.base_url}/entries/{lang_1}/{w}"

    def get(self, url):
        return requests.get(url, headers=self.__headers)


class WordFactory:

    @staticmethod
    def create_word(word, base_lang, target_lang, dictionary, db_curr):
        """Generates a Word obj based on its language

        See Factory Pattern for more details

        Args:
            word: string; defines the word.
            base_lang: Language Code; Specifies the language of the provided 'word'
            target_lang: Language Code; Target Language for Translation methods
            dictionary: OxfordDictionary Class;
            db_curr: Database Cursor

        Returns:
            an instance of a 'Word'
        """
        if base_lang == 'es':
            return SpanishWord(word, base_lang, target_lang, dictionary, db_curr)
        else:
            return GenericWord(word, base_lang, target_lang, dictionary, db_curr)

    @staticmethod
    def run_cmd(w, cmd):
        """Fetches response based on the specified command

        Args:
            w: An instance of a Word Obj
            cmd: CLI arg

        Returns:
            JSON response after running cmd on Word

        Raises:
            NoConjugationSupport: No language support for the Conjugation command.
            UnidentifiedCommand: Command not identified.
        """
        if cmd == 'translate':
            res = w.get_trans()
        elif cmd == 'get_data':
            res = w.get_word_data()
        elif cmd == 'get_conjugations':
            if w.base_lang != 'es':
                raise NoConjugationSupport(w.base_lang)
            res = w.get_all_conjugations()
        else:
            raise UnidentifiedCommand(cmd)
        return res


class GenericWord:
    _api_headers = None
    _word_data = None
    _trans_data = None

    def __init__(self, word, base_lang, target_lang, dictionary: OxfordDictionary, db_curr):
        """
        Args:
            word: string; defines the word.
            base_lang: Language Code; Specifies the language of the provided 'word'
            target_lang: Language Code; Target Language for Translation methods
            dictionary: OxfordDictionary Class;
            db_curr: Database Cursor
        """
        self._get_trans = None
        self.oxford_dict = dictionary
        self.word = word.lower()
        self.base_lang = base_lang
        self.target_lang = target_lang
        self.db_curr = db_curr

    def get_word_data(self):
        """
        Returns:
            JSON res from Oxford dictionary containing extended info about the provided word
        """
        if self._word_data:
            return self._word_data

        url = self.oxford_dict.get_entry_url(self.word, self.base_lang)
        res = self.oxford_dict.get(url)
        self._word_data = res.json()
        return res.json()

    def get_trans(self):

        """GET request to oxford dict for translation

        @return: res from Oxford Dict. containing translation data
        @rtype: JSON
        """
        if self._trans_data:
            return self._trans_data
        url = self.oxford_dict.get_translation_url(self.word, self.base_lang, self.target_lang)
        res = self.oxford_dict.get(url)

        self._get_trans = res.json()
        return res.json()

    def get_example_phrase(self):
        """GET request for additional example phrases containing word.

        @return: response from Oxford Dict. containing a list of example phrases containing a word
        @rtype: JSON
        """
        # @todo write this method

        pass

    def get_all_conjugations(self):
        pass


class SpanishWord(GenericWord):
    def __init__(self, word, base_lang, target_lang, dictionary, db_curr):
        super().__init__(word, base_lang, target_lang, dictionary, db_curr)

    def get_all_conjugations(self):
        # res = self.db_curr.execute('SELECT * FROM gerund')
        # print (res)
        return False
