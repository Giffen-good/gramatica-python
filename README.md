# Gramatica

Designed to improve your Spanish vocabulary and comprehension. Creates quizzes, tracks responses, and recycles terms or phrases that you struggle with to encourage fluency
## Installation

Clone the repository

```bash
git clone git@github.com:Giffen-good/gramatica-python.git
```

From a virtual environment ([venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)), use the package manager [pip](https://pip.pypa.io/en/stable/) to install gramatica

```bash
pip3 install -r requirements.txt 
```

Additionally, you need a key/secret for access to the [Oxford Dictionary API](https://developer.oxforddictionaries.com/). 

Postgres DB extends [Fred Jehle's Conjugated Spanish Verb Database](https://github.com/ghidinelli/fred-jehle-spanish-verbs).

To connect to Dictionary and DB, include an .env file with the following filled out:
```bash
OXFORD_ID=
OXFORD_SECRET=

DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

## Usage

Program can be run as a cli, with two available commands
- translate; Provides translations and related info about the word and it's uses.
- get_data; Provides further details about the word.

with 3 flags to pass in the word (-w), the base language (-b), the target language (-t), where base and target language accept language codes defined by [Oxford Dictionary](https://developer.oxforddictionaries.com/documentation/languages) Results are written to a text file with the format 
> {word}-{base language}-{command}.json

For example,
```bash
 python main.py translate -w ejemplo -b es -t en-gb
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)