class NoConjugationSupport(Exception):
    """Exception raised for trying to retrieve conjugations for an unsupported language

    Attributes:
        lang -- Oxford Dictionary language code. Ex. 'es', 'en-gb', etc.
        message -- Explanation of the error
    """

    def __init__(self, lang, message="Conjugation support only available for Spanish words"):
        self.lang = lang
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.lang} -> {self.message}'


class UnidentifiedCommand(Exception):
    """Exception raised if CLI command is unrecognized

    Attributes:
        cmd -- Command provided
        message -- Explanation of the error
    """

    def __init__(self, cmd, message="Command could not be identified"):
        self.cmd = cmd
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> {self.cmd}'


class InvalidQueryFetchOption(Exception):
    def __init__(self, cmd, message="Fetch command passed into the query object could not be identified"):
        self.cmd = cmd
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> {self.cmd}'
