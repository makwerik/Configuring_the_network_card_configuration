import os
import subprocess
import time
import yaml


class Ethernet:
    """
    Смена IP-адреса, шлюза,
    DNS-сервера, включение Proxy, а также возврат к стандартным настройкам
    """
    def __init__(self, cfg_filepath=None):
        if not cfg_filepath:
            print("Please specify the full path to file with params!")
        else:
            with open(cfg_filepath, "r", encoding="utf8") as file:
                params = yaml.load(file, Loader=yaml.FullLoader)

            self.ip = params['ip']
            self.dns = params['dns']
            self.dns2 = params['dns2']
            self.proxy = params['proxy']
            self.ip_def = params['ip_def']
            self.dns_def = params['dns_def']
            self.proxy_def = params['proxy_def']

    def work_setting(self):
        """
        Смена IP, DNS, Proxy
        """
        subprocess.call(self.ip, shell=True)
        subprocess.call(self.dns, shell=True)
        subprocess.call(self.dns2, shell=True)
        subprocess.call(self.proxy, shell=True)

    def home_setting(self):
        """
        Возврат к default-настройкам
        """
        subprocess.call(self.ip_def, shell=True)
        subprocess.call(self.dns_def, shell=True)
        subprocess.call(self.proxy_def, shell=True)


if __name__ == '__main__':
    Et = Ethernet("data/cfg.yaml")
    ask = input('Home or Work? ')

    if ask == 'Home':
        Et.home_setting()
    elif ask == 'Work':
        Et.work_setting()

