#!/usr/bin/env python3
import base64

def obfuscate(file, layers):
    for i in range(layers):
        try:
            with open(file if i == 0 else 'obfuscated_code.py', 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print('No such file found')
            return

        b64_string = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        with open('obfuscated_code.py', 'w') as f:
            f.write(f"exec(__import__('base64').b64decode('{b64_string}').decode('utf-8'))")
    print('Saved obfuscated code as obfuscated_code.py')


def main():
    file = input('Enter path of the file to obfuscate\n')
    try:
        print('!WARNING! More than 10 layers is not recommended as it can reduce performance and increase output file size SIGNIFICANTLY')
        layers = int(input('Enter how much encoding layers to make\n'))
        if layers > 35:
            answer = input('That is a lot of layers. Are you sure? [y/N]').capitalize()
            if answer == 'N' or answer == 'NO' or not answer:
                return
            elif answer == 'Y' or answer == 'YES':
                print('Got it...')
    except Exception:
        print('Invalid input')
        return

    obfuscate(file, layers)


if __name__ == '__main__':
    main()
