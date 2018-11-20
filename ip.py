# encoding: utf-8
import os
import sys
import argparse
from workflow import Workflow, web


def local_ip():
    """
    ifconfig
    :return:
    """
    ipv4 = os.popen(' ifconfig | grep -A 1 "en" | grep broadcast | cut -d " " -f 2 | tr "\\n" " "').read()
    return ipv4


def external_ip(ip=None):
    """
    get external ip
    :return:
    """
    ip_api = 'http://ip-api.com/json'
    ip_api = ip_api + '/' + ip if ip else ip_api
    req = web.get(ip_api)
    req.raise_for_status()
    return req.json()


def main(wf):
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', dest='ip', nargs='?', default=None)
    args = parser.parse_args(wf.args)

    ip_intranet = local_ip()
    ip_public_info = external_ip(args.ip)

    location = '{}, {} ({}) '.format(ip_public_info['city'], ip_public_info['country'], ip_public_info['countryCode'])
    coordinates = '({}, {})'.format(ip_public_info['lat'], ip_public_info['lon'])

    if not args.ip:
        wf.add_item(title='Local IP: '+ip_intranet,
                    subtitle='press Enter to copy',
                    arg=ip_intranet)
    wf.add_item(title=ip_public_info['org'] + ': ' + ip_public_info['query'],
                subtitle=location + coordinates,
                arg=ip_public_info['query'],
                valid=True,
                icon=None)
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))