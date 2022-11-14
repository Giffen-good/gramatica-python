import json
import os
from constants import ROOT_DIR


def write_response_to_file(w, args, res):
    fname = f"{w.word}-{args.base_lang}-{args.cmd}.json", "x"
    if os.path.isfile(f"{ROOT_DIR}/word_data/{fname}"):
        print('File Already exists. Skipping')
    else:
        f = open(fname, "x")
        f.write(json.dumps(res, indent=4))
        f.close()


def set_cli_args(parser, __version__):
    # Required positional argument
    parser.add_argument("cmd", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    parser.add_argument("-w", "--word", action="store", dest="word")
    # Base Language - set it with the language matching your word
    # Optional argument which requires a parameter (eg. -b es)
    # accepts a valid language code as an argument (ex es, en-gb)
    parser.add_argument("-b", "--base", action="store", dest="base_lang")

    parser.add_argument("-t", "--target", action="store", dest="target_lang")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    return parser.parse_args()
