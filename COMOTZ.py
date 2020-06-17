import base64, zlib, marshal, sys
merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'
blue = '\x1b[1;96m'
putih = '\x1b[1;97m'
tutup = '\x1b[0m'
abu = '\x1b[0;37m'
W = '\x1b[1;37m'
RR = '\x1b[1;37m\x1b[31m'
O = '\x1b[33m'
B = '\x1b[34m'
(W, O, W, RR, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W)
print '\x1b[0;96m           _____                 _       _____'
print '\x1b[0;96m          |   __| ___  ___  ___ |_| ___ |_   _| ___  ___'
print '\x1b[0;96m          |   __||   ||  _||  _|| || . |  | |  | . ||  _|'
print '\x1b[1;97m          |_____||_|_||___||_|  |_||  _|  |_|  |___||_|'
print '\x1b[1;97m                                   |_|python2 bytecode'
print ' \x1b[36m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n \x1b[31m[\x1b[37m+\x1b[31m] \x1b[32mAuthor   = \x1b[37mMr,Gaming\n \x1b[31m[\x1b[37m+\x1b[31m] \x1b[32mYoutube  = \x1b[37mJomblo Kawe\n \x1b[31m[\x1b[37m+\x1b[31m] \x1b[32mFacebook = \x1b[37mhttps://www.facebook.com/Neng.Njancok\n \x1b[31m[\x1b[37m+\x1b[31m] \x1b[32mUpdate   = \x1b[1;33mversi 1.2 Anti Recoder\n \x1b[36m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
print ' \x1b[37m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n \x1b[37m\xe2\x95\x91\x1b[31m           \xe2\x8f\xa3 \x1b[36mpython bytecode EncripTor | Coded By Mr.Gaming \x1b[31m\xe2\x8f\xa3\n \x1b[37m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n \x1b[31m[\x1b[37m1 \x1b[31m] \x1b[37mEncript To Marshall\n \x1b[31m[\x1b[37m2 \x1b[31m] \x1b[37mEncript To base16\n \x1b[31m[\x1b[37m3 \x1b[31m] \x1b[37mEncript To base32\n \x1b[31m[\x1b[37m4 \x1b[31m] \x1b[37mEncript To base64\n \x1b[31m[\x1b[37m5 \x1b[31m] \x1b[37mEncript To zlib,base64\n \x1b[31m[\x1b[37m6 \x1b[31m] \x1b[37mEncript To zlib,base16,marshall\n \x1b[31m[\x1b[37m7 \x1b[31m] \x1b[37mEncript To zlib,base32,marshall\n \x1b[31m[\x1b[37m8 \x1b[31m] \x1b[37mEncript To zlib,Base64,marshall'

def main():
    choice = raw_input(RR + '[++ ' + W + 'Choose: ')
    if choice == '4' or choice == '04':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b64encode(fileopen)
            b = "import base64\nexec(base64.b64decode('" + a + "'))"
            c = file.replace('.py', '_AGdcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'File output:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '2' or choice == '02':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b16encode(fileopen)
            b = "import base64\nexec(base64.b16decode('" + a + "'))"
            c = file.replace('.py', '_AGdcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'File Output:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '3' or choice == '03':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b32encode(fileopen)
            b = "import base64\nexec(base64.b32decode('" + a + "'))"
            c = file.replace('.py', '_AGdcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'File Output:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '1' or choice == '01':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = compile(fileopen, 'dg', 'exec')
            m = marshal.dumps(a)
            s = repr(m)
            b = 'import marshal\nexec(marshal.loads(' + s + '))'
            c = file.replace('.py', '_AGdcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'File Output:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '5' or choice == '05':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            c = zlib.compress(fileopen)
            d = base64.b64encode(c)
            e = 'import marshal,zlib,base64\nexec(zlib.decompress(base64.b64decode("' + d + '")))'
            f = file.replace('.py', '_AGdcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'File Output:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '8' or choice == '08':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b64encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + str(d) + '"))))'
            f = file.replace('.py', '_AGdcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'File Output:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '6' or choice == '06':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b16encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + str(d) + '"))))'
            f = file.replace('.py', '_AGdcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'File Output:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '7' or choice == '07':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b32encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + str(d) + '"))))'
            f = file.replace('.py', '_AGdcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'File Output:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    elif choice == '9' or choice == '09':
        sys.exit(RR + '[*] ' + W + 'By Gayn :v!1!!!!!!!!')
        main()
    else:
        print RR + '[-] ' + W + 'Wrong Input Comand!!'
        sys.exit(RR + '[*] ' + W + 'by Njer!!!1!1')


if __name__ == '__main__':
    main()