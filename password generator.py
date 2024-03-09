import sys
import string, random
import argparse
import test


def create_password(length=8, upper=False, lower=False, digit=False, punc=False):
    psd=''
    if upper:
        psd+=string.ascii_uppercase
    if lower:
        psd+=string.ascii_lowercase
    if digit:
        psd+=string.digits
    if punc:
        psd+=string.punctuation
    if psd == '':
        psd=string.ascii_letters

    return ''.join(random.choices(psd, k=length))


if __name__ == '__main__':

    parser=argparse.ArgumentParser()
    parser.add_argument('length', type=int)
    parser.add_argument('-l','--lower', type=str)
    parser.add_argument('-u','--upper', type=str)
    parser.add_argument('-d','--digit', type=str)
    parser.add_argument('-p','--punc', type=str)

    args=parser.parse_args()
    print(create_password(args.length))
