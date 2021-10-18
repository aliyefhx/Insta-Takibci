from instagram_private_api import Client, ClientCompatPatch, errors
from colorama import init, Fore, Style
from time import strftime, sleep
from sys import exit

def get_time():
    date = strftime("%H:%M:%S")
    return (f"{Style.BRIGHT + Fore.CYAN}[{date}]{Style.RESET_ALL}")

def main():
    logo = f"""
    {Style.BRIGHT + Fore.RED}  ▄▄ ▄███▄{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}▄▀▀▀▀ ▄▄▄ ▀▀▀▀▄   {Style.BRIGHT + Fore.MAGENTA}Instagram Kitləyə görə takipci tapan.{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}█    █   █    █   {Style.BRIGHT + Fore.RED}+-----------------------------------+{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}█    ▀▄▄▄▀    █             {Style.BRIGHT + Fore.YELLOW}Coded by Aliyefh // Telegram: @aliyefh_sos{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀{Style.RESET_ALL}

    """
    print(logo)
    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Hansı takip etmə metodundan istifadə etmək isdəyirsən:{Style.RESET_ALL}")
    tmp = (11 * " ")
    print(f"{Style.RESET_ALL}{tmp}{Style.BRIGHT + Fore.MAGENTA}1 > {Style.RESET_ALL + Fore.WHITE}Hashtag işlədərək takipçi tapmaq.{Style.RESET_ALL}")
    print(f"{Style.RESET_ALL}{tmp}{Style.BRIGHT + Fore.MAGENTA}2 > {Style.RESET_ALL + Fore.WHITE}istifadəçidən takipçi tapmaq.{Style.RESET_ALL}")
    print(f"{Style.RESET_ALL}")
    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[>] {Style.BRIGHT + Fore.WHITE}Seçiminiz:{Style.RESET_ALL} ", end="")
    method = input()

    if (method != "1" and method != "2"):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Seçiminiz 1 vəya 2 olmalıdır!{Style.RESET_ALL}")
        exit(0)
    
    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE} takiplər sırasında neçə saniyə gözlənilsin: {Style.RESET_ALL}", end="")
    sleep_sec = input()
        
    try:
        int(sleep_sec)
    except:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}gözləmə vaxtı bir rəqəm olmalıdır!{Style.RESET_ALL}")
        exit(0)

    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}insta adınız: {Style.RESET_ALL}", end="")
    username = input()
    if (" " in username or username.strip() == ""):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}insta adınız boş vəya boşluq içərir!{Style.RESET_ALL}")
        exit(0)
    
    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Şifrəniz: {Style.RESET_ALL}", end="")
    password = input()

    if (password.strip() == ""):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Şifrəniz boş olamaz!{Style.RESET_ALL}")
        exit(0)

    try:
        api = Client(username, password)
    except errors.ClientLoginError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}insta adınız vəya şifrəniz xətalı! ({e}){Style.RESET_ALL}")
        exit(0)
    except errors.ClientChallengeRequiredError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Giriş üçün doğrulama gərəkir! ({e}){Style.RESET_ALL}")
        exit(0)
    except errors.ClientCheckpointRequiredError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Giriş üçün doğrulama gərəkir! ({e}){Style.RESET_ALL}")
        exit(0)
    except errors.ClientSentryBlockError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Giriş uğursuz! Hesap spam olaraq işarələnmiş! ({e}){Style.RESET_ALL}")
        exit(0)
    except errors.ClientConnectionError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Bağlantı xətası! ({e}){Style.RESET_ALL}")
        exit(0)
    except errors.ClientError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Giriş uğursuz! ({e}){Style.RESET_ALL}")
        exit(0)
    
    print("")
    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}Giriş uğurlu!{Style.RESET_ALL}")
    
    if ("Aliyefh" not in logo):
        print("Code by Aliyefh:Oğurlayan məmə ata desin.")
        exit(0)

    if (method == "1"):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Axtarmaq istədiginiz hashtagləri girin ('#' siz ve hashtaglər arası vergül qoyun örnək: Aliyefh,InvenTorfilixs):{Style.RESET_ALL} ", end="")
        hashtags = input()
        hashtag_list = hashtags.strip().split(",")
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{len(hashtag_list)} ədəd hashtəg axtarılacaq!{Style.RESET_ALL}")
        
        for hashtag in hashtag_list:
            if (hashtag.strip() == ""):
                print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Boş hashtəg tapıldı! keçirəm...{Style.RESET_ALL}")
                continue

            try:
                data = api.top_search(hashtag)

                if (len(data["users"]) == 0):
                    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}{hashtag} hashtəgini heçkim işlətmiyib! keçirəm..!{Style.RESET_ALL}")
                    continue
                
                tmp = len(data["users"])
                print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{tmp} adəd istifadəçiyə takip atılacaq!{Style.RESET_ALL}")

                for users in data["users"]:
                    if ("user" not in users):
                        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}istifadəçi tapılmadı! keçirəm...{Style.RESET_ALL}")
                        continue

                    user_data = users["user"]
                    tmp = user_data["username"]

                    try:
                        if(api.friendships_show(user_data["pk"])["following"] == True):
                            print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{tmp} istifadəçiyə zatən takip atıldı! kəçilir..!{Style.RESET_ALL}")
                            continue

                        api.friendships_create(user_data["pk"])
                        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{tmp} istifadəçisinə takip atıldı!{Style.RESET_ALL}")
                    except errors.ClientError as e:
                        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}{tmp} istifadəçiyə takip atılmadı! ({e}){Style.RESET_ALL}")
                    except errors.ClientConnectionError as e:
                        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}{tmp} istifadəçiyə takip atılamadı! Bağlantı xətası!({e}){Style.RESET_ALL}")
                    
                    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.CYAN}[*] {Style.BRIGHT + Fore.WHITE}{sleep_sec} saniye gözlənilir!{Style.RESET_ALL}")
                    sleep(int(sleep_sec))
                    continue
            except errors.ClientError as e:
                print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Hashtəg bilgiləri alınmadı! ({e}){Style.RESET_ALL}")
            except errors.ClientConnectionError as e:
                print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Bağlantı xətası! ({e}){Style.RESET_ALL}")
    elif (method == "2"):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Hədəfin istifadəçinin adını girin:{Style.RESET_ALL} ", end="")
        target_username = input()
        if (" " in target_username or target_username.strip() == ""):
            print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Hədəfin istifadəçinin adı boş vəya boşluq içərir!{Style.RESET_ALL}")
            exit(0)

        try:
            data = api.username_info(target_username)
            data = api.user_followers(data["user"]["pk"], api.generate_uuid())
            
            tmp = data["users"]
            print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{len(tmp)} ədəd istifadəçiyə takip atılacaq!{Style.RESET_ALL}")

            for user in data["users"]:
                try:
                    tmp = user["username"]

                    if(api.friendships_show(str(user["pk"]))["following"] == True):
                        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{tmp} istifadəçiyə zatən takip atıldı! keçildi..!{Style.RESET_ALL}")
                        continue

                    api.friendships_create(str(user["pk"]))
                    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{tmp} istifadəçisinə takip atıldı!{Style.RESET_ALL}")
                except errors.ClientError as e:
                    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}{tmp} istifadəçisinə takip atılmadı! ({e}){Style.RESET_ALL}")
                except errors.ClientConnectionError as e:
                    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}{tmp} istifadəçisinə takip atılmadı! Bağlantı xətası!({e}){Style.RESET_ALL}")
                    
                print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.CYAN}[*] {Style.BRIGHT + Fore.WHITE}{sleep_sec} saniyə gözlənilir!{Style.RESET_ALL}")
                sleep(int(sleep_sec))
                continue
                    
        except errors.ClientError as e:
            print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Hashtəg bilgiləri alınmadı! ({e}){Style.RESET_ALL}")
        except errors.ClientConnectionError as e:
            print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Bağlantı xətası! ({e}){Style.RESET_ALL}")

    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.CYAN}[*] {Style.BRIGHT + Fore.WHITE}Takip işlənməsi bitti!{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        init()
        main()
    except KeyboardInterrupt:
        print()
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.CYAN}[*] {Style.BRIGHT + Fore.WHITE}Program bağlanılır Thanks Aliyefh!{Style.RESET_ALL}")
    pass
