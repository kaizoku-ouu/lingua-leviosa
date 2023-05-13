# LINGUA LEVIOSA  
#### Video Demo:  <URL HERE>  
### Description:  
  
___Lingua leviosa___ is a  Translate and Read Aloud CLI tool is a Python program that allows users to translate text or text files from one language to another using the _Google Translate API_. The tool supports automatic language detection, and users can specify the source and target languages as well.   
  
The program also features a read-aloud functionality that uses _Google Text-to-Speech_ (GTTS) to read the translated output aloud in the target language. If the target language is not supported by GTTS, the program will prompt the user to select another language for translation and read-aloud.   
  
Users can interact with the tool via the command line by providing input arguments or by responding to prompts. The program also outputs a pretty table of language codes for easy reference.   
  
Overall, this tool is useful for anyone who needs to translate and/or listen to text in different languages, and it provides a simple, convenient interface for doing so.  
  
### Files:  
The _project.py_ file contains all the source code of the tool.  
  
The _test_project.py_ file is a unit-test script for the _project.py_ which uses __pytest__ module.

The _requirements.txt_ file contains all the pip installable modules used in this project.
### Usage:
To use the script, simply run the project.py file from the command line. If no arguments are provided, the script will prompt the user for the necessary inputs. Alternatively, arguments can be provided using the following options:

| Argument      | Description                                                      |
| ------------- | ---------------------------------------------------------------- |
| `-i` / `--input` | Input text or path to input text file                           |
| `-f` / `--format` | Input format (either "text" or "file")                            |
| `-s` / `--source` | Source language (default: auto)                                   |
| `-t` / `--target` | Target language (default: "en")                                   |
| `-o` / `--output` | Output text or path to output text file                           |
| `--read`       | Read the output text aloud     
#### Examples:
__Using command line arguments:__
Translate a text file from German to English and save the output to another file:

`python project.py -i input.txt -f file -s de -t en -o output.txt` 

Translate a text file from Spanish to English and read the output aloud:

`python project.py -i input.txt -f file -s es -t en --read` 

Translate text from French to German and display the output on the console:

	python project.py -i "Bonjour, comment ça va ?" -s fr -t de`
     _     _                           _               _                 
    | |   (_)_ __   __ _ _   _  __ _  | |    _____   _(_) ___  ___  __ _
    | |   | | '_ \ / _` | | | |/ _` | | |   / _ \ \ / / |/ _ \/ __|/ _` |
    | |___| | | | | (_| | |_| | (_| | | |__|  __/\ V /| | (_) \__ \ (_| |
    |_____|_|_| |_|\__, |\__,_|\__,_| |_____\___| \_/ |_|\___/|___/\__,_|
                   |___/

	Translated text: Hallo, wie geht's dir ?

  
__Using prompts:__                                  
_This is just an example. the output and prompts may vary according to the users input._

	\lingua leviosa>python project.py
	Enter input format:(text/file) Text
     _     _                           _               _                 
    | |   (_)_ __   __ _ _   _  __ _  | |    _____   _(_) ___  ___  __ _
    | |   | | '_ \ / _` | | | |/ _` | | |   / _ \ \ / / |/ _ \/ __|/ _` |
    | |___| | | | | (_| | |_| | (_| | | |__|  __/\ V /| | (_) \__ \ (_| |
    |_____|_|_| |_|\__, |\__,_|\__,_| |_____\___| \_/ |_|\___/|___/\__,_|
                   |___/

	+-----------------------+-------+
	|        Language       |  Code |
	+-----------------------+-------+
	|       afrikaans       |   af  |
	|        albanian       |   sq  |
	|        amharic        |   am  |
	|         arabic        |   ar  |
	|        armenian       |   hy  |
	|      azerbaijani      |   az  |
	|         basque        |   eu  |
	|       belarusian      |   be  |
	|        bengali        |   bn  |
	|        bosnian        |   bs  |
	|       bulgarian       |   bg  |
	|        catalan        |   ca  |
	|        cebuano        |  ceb  |
	|        chichewa       |   ny  |
	|  chinese (simplified) | zh-cn |
	| chinese (traditional) | zh-tw |
	|        corsican       |   co  |
	|        croatian       |   hr  |
	|         czech         |   cs  |
	|         danish        |   da  |
	|         dutch         |   nl  |
	|        english        |   en  |
	|       esperanto       |   eo  |
	|        estonian       |   et  |
	|        filipino       |   tl  |
	|        finnish        |   fi  |
	|         french        |   fr  |
	|        frisian        |   fy  |
	|        galician       |   gl  |
	|        georgian       |   ka  |
	|         german        |   de  |
	|         greek         |   el  |
	|        gujarati       |   gu  |
	|     haitian creole    |   ht  |
	|         hausa         |   ha  |
	|        hawaiian       |  haw  |
	|         hebrew        |   he  |
	|         hindi         |   hi  |
	|         hmong         |  hmn  |
	|       hungarian       |   hu  |
	|       icelandic       |   is  |
	|          igbo         |   ig  |
	|       indonesian      |   id  |
	|         irish         |   ga  |
	|        italian        |   it  |
	|        japanese       |   ja  |
	|        javanese       |   jw  |
	|        kannada        |   kn  |
	|         kazakh        |   kk  |
	|         khmer         |   km  |
	|         korean        |   ko  |
	|   kurdish (kurmanji)  |   ku  |
	|         kyrgyz        |   ky  |
	|          lao          |   lo  |
	|         latin         |   la  |
	|        latvian        |   lv  |
	|       lithuanian      |   lt  |
	|     luxembourgish     |   lb  |
	|       macedonian      |   mk  |
	|        malagasy       |   mg  |
	|         malay         |   ms  |
	|       malayalam       |   ml  |
	|        maltese        |   mt  |
	|         maori         |   mi  |
	|        marathi        |   mr  |
	|       mongolian       |   mn  |
	|   myanmar (burmese)   |   my  |
	|         nepali        |   ne  |
	|       norwegian       |   no  |
	|          odia         |   or  |
	|         pashto        |   ps  |
	|        persian        |   fa  |
	|         polish        |   pl  |
	|       portuguese      |   pt  |
	|        punjabi        |   pa  |
	|        romanian       |   ro  |
	|        russian        |   ru  |
	|         samoan        |   sm  |
	|      scots gaelic     |   gd  |
	|        serbian        |   sr  |
	|        sesotho        |   st  |
	|         shona         |   sn  |
	|         sindhi        |   sd  |
	|        sinhala        |   si  |
	|         slovak        |   sk  |
	|       slovenian       |   sl  |
	|         somali        |   so  |
	|        spanish        |   es  |
	|       sundanese       |   su  |
	|        swahili        |   sw  |
	|        swedish        |   sv  |
	|         tajik         |   tg  |
	|         tamil         |   ta  |
	|         telugu        |   te  |
	|          thai         |   th  |
	|        turkish        |   tr  |
	|       ukrainian       |   uk  |
	|          urdu         |   ur  |
	|         uyghur        |   ug  |
	|         uzbek         |   uz  |
	|       vietnamese      |   vi  |
	|         welsh         |   cy  |
	|         xhosa         |   xh  |
	|        yiddish        |   yi  |
	|         yoruba        |   yo  |
	|          zulu         |   zu  |
	+-----------------------+-------+
	Enter language-code for source-language/language to be translated from or 'auto' for automatic language detection: auto
	Enter language-code for  target-language/language to be translated to: en
	Do you want to read the output aloud? (y/n) n
	enter the text to be translated: 私はCS50を取りました
	Translated text: I took CS50
### Dependencies
 
 There is a _requirements.txt_ file that has all the libraries required. You can install all the libraries at once by using the command-

        pip install -r requirements.txt
 
 Or you can install them one by one as mentioned below.

_Note: make sure to install the exact versions of the modules as other versions tend to have bugs( that i faced,  you can go ahead and install the normal versions and try them if you would like to. )_
- `googletrans`: A free and unlimited Python library that implements the Google Translate API. You can install it using the following command:
	
        pip install googletrans==4.0.0rc1	
	
- `gtts`: A Python library and CLI tool to interface with Google Translate's text-to-speech API. You can install it using the following command:
	
        pip install gtts

- `prettytable`: A Python library used to create tables in a simple manner. You can install it using the following command:
	
        pip install prettytable

- `playsound`: A Python library used to play audio files. You can install it using the following command:

        pip install playsound==1.2.2

- `pytest`: A Python library used to perform simple unit-tests on the written python files. You can install it using the following command:

        pip install pytest

- `httpcore`: The HTTP Core package provides a minimal low-level HTTP client, which does one thing only. Sending HTTP requests. You can install it using the following command:

        pip install httpcore

-> ___text formating modules used:___
- `pyfiglet`: A Python library used to convert text to ASCII art. You can install it using the following command:

        pip install pyfiglet
- `printy`: A Python library used to colorize and apply some standard formats to the text. You can install it using the following command:

        pip install printy

#### _Other python packages used:_

-[`argparse`🔗](https://docs.python.org/3/library/argparse.html)

-[`sys`🔗](https://docs.python.org/3/library/sys.html)

-[`re`🔗](https://docs.python.org/3/library/re.html)

-[`webbrowser`🔗](https://docs.python.org/3/library/webbrowser.html)

### Functions

There are ten functions including the _main()_ function.

#### main():
This function is the entry point of the program. It displays the program's name in ASCII art(using [pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) library), then checks if there are any command-line arguments passed to it. If there are, it calls the [parseinput](#parseinput) function. If there aren't, it calls the [promptinput](#promptinput) function. If a KeyboardInterrupt is detected, it calls the [exity](#exity) function with an appropriate message.

#### parseinput():
This function uses the [argparse](https://docs.python.org/3/library/argparse.html) library to parse command-line arguments. It accepts arguments for input text or text file, input format, source language, target language, output text or text file, and whether to read the output aloud. It then calls either the [filemanager](#translate) or [translate](#translate) function based on the input format. If reading aloud is requested, it calls the [readaloud](#readaloud) function.

#### promptinput():
This function prompts the user for input if no command-line arguments were passed to the program. It asks the user for the input format, source language, target language, and whether to read the output aloud. It then calls either the [filemanager](#translate) or [translate](#translate) function based on the input format. If reading aloud is requested, it calls the [readaloud](#readaloud) function.

#### translate():
This function uses the [googletrans](https://pypi.org/project/googletrans/) library to translate the input text from the source language (srcl) to the target language (targ). If the source language is set to "auto", [googletrans](https://pypi.org/project/googletrans/) automatically detects the language. The function returns the translated text.
It takes in 3 arguments _text, srcl, targ_.
    
```python console
>>print(translate("xie xie!", srcl="auto", targ="en"))
>>Translated text: Thank you!
```
#### filemanager():
This function reads text from an input file (inp) and writes translated text to an output file (out), if specified and opens the file in the default text editor. It calls the [translate](#translate) function to translate the input text. If no output file is specified, it prints the translated text to the console. If reading aloud is requested, it calls the [readaloud](#readaloud) function.
It takes in 5 arguments 
```python
filemanager(inp, out, src, dest, read=False)
```
     
- `inp`: input file name
- `out`: output file name
- `src`: source language
- `dest`: destination or target language
- `read`: True or False to read out loud

#### readaloud():
This function generates audio from the input text using the [gtts](https://gtts.readthedocs.io/en/latest/index.html) library. It saves the audio as an mp3 file and plays it using the [playsound](https://pypi.org/project/playsound/) library. If the specified language is not supported by [gtts](https://gtts.readthedocs.io/en/latest/index.html), it prompts the user whether to translate the text to another language and reads it aloud. If reading aloud is not possible, it prints an error message.

#### langcodestable():
This function generates a [PrettyTable](https://pypi.org/project/prettytable/) object containing a list of languages and their codes from the input library (lib). It is used to display a table of languages and their codes in the [promptinput](#promptinput) function. It returns the generated table.

```python
import gtts

print(langcodestable(gtts.lang.tts_langs()))

'''
output:
+---------------------------+-------+
|          Language         |  Code |
+---------------------------+-------+
|         Afrikaans         |   af  |
|           Arabic          |   ar  |
|         Bulgarian         |   bg  |
|          Bengali          |   bn  |
|          Bosnian          |   bs  |
|          Catalan          |   ca  |
|           Czech           |   cs  |
|           Danish          |   da  |
|           German          |   de  |
|           Greek           |   el  |
|          English          |   en  |
|          Spanish          |   es  |
|          Estonian         |   et  |
|          Finnish          |   fi  |
|           French          |   fr  |
|          Gujarati         |   gu  |
|           Hindi           |   hi  |
|          Croatian         |   hr  |
|         Hungarian         |   hu  |
|         Indonesian        |   id  |
|         Icelandic         |   is  |
|          Italian          |   it  |
|           Hebrew          |   iw  |
|          Japanese         |   ja  |
|          Javanese         |   jw  |
|           Khmer           |   km  |
|          Kannada          |   kn  |
|           Korean          |   ko  |
|           Latin           |   la  |
|          Latvian          |   lv  |
|         Malayalam         |   ml  |
|          Marathi          |   mr  |
|           Malay           |   ms  |
|     Myanmar (Burmese)     |   my  |
|           Nepali          |   ne  |
|           Dutch           |   nl  |
|         Norwegian         |   no  |
|           Polish          |   pl  |
|         Portuguese        |   pt  |
|          Romanian         |   ro  |
|          Russian          |   ru  |
|          Sinhala          |   si  |
|           Slovak          |   sk  |
|          Albanian         |   sq  |
|          Serbian          |   sr  |
|         Sundanese         |   su  |
|          Swedish          |   sv  |
|          Swahili          |   sw  |
|           Tamil           |   ta  |
|           Telugu          |   te  |
|            Thai           |   th  |
|          Filipino         |   tl  |
|          Turkish          |   tr  |
|         Ukrainian         |   uk  |
|            Urdu           |   ur  |
|         Vietnamese        |   vi  |
|    Chinese (Simplified)   | zh-CN |
| Chinese (Mandarin/Taiwan) | zh-TW |
|     Chinese (Mandarin)    |   zh  |
+---------------------------+-------+
'''
```
#### getread():
This function prompts the user and returns _True_ or _False_ based on the user's input, i.e. whether to read out aloud or not, the input to the prompts can be any of the following: `y`, `yes`, `n`, `no`. it is case-insensitive.

#### exity():
This function's sole purpose is to print the exit message in color formatted text and call the `sys.exit()` method. 

_Note: As of now i don't know any method or library which can be used to format the text for sys.exit() method, so I made this function. Also [printy](https://github.com/edraobdu/printy) is pretty easy to use._

#### filecheck():
This function checks the input file type, i.e. whether the input-file is a _text document_ and whether the output-file is either a _text document_ or _empty_.