# encoding: utf-8
import os
import sys
from workflow import Workflow, web


def local_ip():
    """
    ifconfig
    :return:
    """
    ipv4 = os.popen(' ifconfig | grep -A 1 "en" | grep broadcast | cut -d " " -f 2 | tr "\\n" " "').read()
    print(ipv4)
    return ipv4


def external_ip(ip=None):
    """
    get external ip
    :return:
    """
    ip_api = 'http://ip-api.com/json'
    ip_api = ip_api + '/' + ip if ip else ip_api
    print(ip_api)


def ip_geolocation(ip_address):
    """
    http://ip-api.com/
    :param ip_address:
    :return:
    """
    pass


def main(wf):
    local_ip()
    external_ip()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))