# https://thecoollife.tistory.com/126
# python wav_to_pcm.py [변환할 파일명]
# .wav -> .pcm 변환

import sys
import os.path
ext = None


def convert_wave_to_pcm(filename):
    file = open(filename, 'rb')
    byteBuffer = bytearray(file.read())
    file.close()
    fn_ext = os.path.splitext(filename)

    if fn_ext[1] == '.wav':
        out_filename = fn_ext[0] + '.pcm'
    else:
        out_filename = fn_ext[0] + fn_ext[1] + '.pcm'

    print('Out file name: %s' % out_filename)
    out_file = open(out_filename, 'wb')
    out_file.write(byteBuffer[44:])
    out_file.close()


if len(sys.argv) == 1:
    YesNo = input('Do you want to convert *.wav to *.pcm? (Yes or No): ')

    if 'yes' in YesNo:
        filename = '.wav'
        print('Convert *.wav to *.pcm !!!')
    else:
        print('Please try it again with a filename or .wav !!!')
        exit(0)
else:
    filename = sys.argv[1]

while True:
    fn_ext = os.path.splitext(filename)
    if (not fn_ext[1]) & fn_ext[0].count('.'):
        if fn_ext[0] == '.':
            print('Input file name is invalid!!!')
            exit(0)
        else:
            print('Input file name has the only ext!!!')
            ext = fn_ext[0]
            break

    else:
        try:
            convert_wave_to_pcm(filename)
            break
        except:
            print('[Error] No such file: %s' % filename)
            filename = input('Please type file name: ')

if ext is not None:
    folder = os.getcwd()
    print('folder: %s' % folder)

    for filename in os.listdir(folder):
        print(filename)

        if filename.endswith(ext):
            convert_wave_to_pcm(filename)

input('Press Enter to exit')
exit(0)