import sys

if len(sys.argv) >= 3:
    script = sys.argv[0]
    encoding = sys.argv[1]
    error = sys.argv[2]
else:
    print("Este script precisa de pelo menos três argumentos.")

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<====>", cooked_string)


languages = open('languages.txt', encoding='utf-8')

main(languages, encoding, error)