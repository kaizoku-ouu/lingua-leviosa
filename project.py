import googletrans
import gtts
import sys
import argparse
import pyfiglet
import re
from printy import printy, inputy, escape
from prettytable import PrettyTable
from playsound import playsound


def main():
    printy(pyfiglet.figlet_format("Lingua Leviosa"), "<b")
    try:
        if len(sys.argv) > 1:
            parseinput()
        else:
            promptinput()
    except KeyboardInterrupt:
        exity("KeyboardInterrupt", "Buh-Byee")


def parseinput():
    parser = argparse.ArgumentParser(
        description="Translate text or text file to another language"
    )
    parser.add_argument("-i", "--input", help="Input text or text file path")
    parser.add_argument(
        "-f", "--format", help="Input format: text or file", default="text"
    )
    parser.add_argument("-s", "--source", help="Source language", default="auto")
    parser.add_argument("-t", "--target", help="Target language", default="en")
    parser.add_argument("-o", "--output", help="Output text or text file path")
    parser.add_argument(
        "--read", help="Read the output text aloud", action="store_true"
    )
    args = parser.parse_args()
    srclang = args.source
    outlang = args.target
    if args.format == "file":
        if args.input:
            if not filecheck(str(args.input)):
                exity("FileTypeError", "invalid input file type")
            if not filecheck(str(args.output), False):
                exity("FileTypeError", "invalid output file type for writing")
            filemanager(args.input, args.output, args.source, args.target, args.read)
        else:
            exity("ArgumentError", "no input file given")
    elif args.format == "text":
        inputext = args.input
        translated = translate(inputext, srclang, outlang)
        printy("Translated text:", translated)
        if args.read:
            readaloud(translated, args.target)


def promptinput():
    informat = inputy("Enter input format:(text/file) ", "o").lower().strip()
    if informat not in ["text", "file"]:
        sys.exit("invalid input format")
    printy(langcodestable(googletrans.LANGCODES), "c")
    while True:
        srclang = inputy(
            "Enter language-code for source-language/language to be translated from or"
            " 'auto' for automatic language detection: ",
            "o",
        )
        if srclang in googletrans.LANGCODES.values() or srclang == "auto":
            break
        printy("Enter correct code", "r")
    while True:
        outlang = inputy(
            "Enter language-code for  target-language/language to be translated to: ",
            "o",
        )
        if outlang in googletrans.LANGCODES.values():
            break
        printy("Enter correct code", "r")
    read = getread()
    if informat == "text":
        inputext = inputy("enter the text to be translated: ", "o")
        translatedtext = translate(inputext, srclang, outlang)
        print("Translated text:", translatedtext)
        if read:
            readaloud(translatedtext, outlang)
    elif informat == "file":
        while True:
            infilename = inputy("Enter input File name or File path: ", "o")
            if not filecheck(infilename):
                printy("invalid input file type", "r")
                continue
            break
        while True:
            outfilename = inputy(
                "Enter output File name or File path(or leave blank for console output): ",
                "o",
            )
            if not filecheck(outfilename, False):
                printy("invalid output file type for writing", "r")
                continue
            break

        filemanager(infilename, outfilename, srclang, outlang, read)


def translate(text, srcl="auto", targ="en"):
    trans = googletrans.Translator()
    if srcl != "auto":
        translated = trans.translate(text, src=srcl, dest=targ)
    else:
        translated = trans.translate(text, dest=targ)
    return translated.text


def filemanager(inp, out, src, dest, read=False):
    try:
        with open(inp, "r", encoding="utf-8") as fileinp:
            text = fileinp.read()
            translatedtext = translate(text, src, dest)
        if out == "" or out is None:
            print(translatedtext)
        else:
            with open(out, "w", encoding="utf-8") as fileoutp:
                fileoutp.write(translatedtext)

    except FileNotFoundError:
        exity("FileNotFoundError", "invalid file")
    if read:
        readaloud(translatedtext, dest)


def readaloud(text, lang):
    try:
        reading = gtts.gTTS(text, lang=lang)
        reading.save("readaloud.mp3")
        playsound("readaloud.mp3")

    except ValueError:
        printy(
            f"[mB]{googletrans.LANGUAGES.get(lang)} ({lang})@ does not yet support reading.",
            predefined="r",
        )
        dotrans = inputy(
            "would you like to translate the text into another"
            " language and read it aloud?(y/n) ",
            "o",
        )
        if dotrans == "y" or dotrans == "yes":
            printy("reading supported languages:", "<cB")
            printy(langcodestable(gtts.lang.tts_langs()), "p>")
            dest = inputy(
                "Enter the language code for the language you would like to translate to: ",
                "o",
            )
            translated = translate(text, lang, dest)
            print(translated)
            readaloud(translated, dest)


def langcodestable(lib):
    table = PrettyTable()
    table.field_names = ["Language", "Code"]
    for language, code in lib.items():
        if lib == gtts.lang.tts_langs():
            table.add_row([code, language])
        else:
            table.add_row([language, code])
    return table


def getread():
    while True:
        read = inputy("Do you want to read the output aloud? (y/n) ", "o").lower()
        if read in ["y", "n", "yes", "no"]:
            return read == "y" or read == "yes"

        else:
            continue


def filecheck(fname: str, flag=True):
    return (
        re.fullmatch(r"^(.+(.txt))$", fname, flags=re.IGNORECASE)
        if flag
        else re.fullmatch(r"^((.+(.txt))|\\n|None|)$", fname, flags=re.IGNORECASE)
    )


def exity(error, msg):
    printy(f"[Br]{escape(error)}@: [yU]{escape(msg)}@")
    sys.exit()


if __name__ == "__main__":
    main()
