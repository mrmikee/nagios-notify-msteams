#!/usr/bin/env python3
#
# Michael Cone
#

import argparse
import json
import os
import requests
from datetime import datetime
from jinja2 import Environment, PackageLoader, select_autoescape

NAGIOS_URL = "http://nagios.my.lan/cgi-bin/nagios3"

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

env = Environment(
    loader=PackageLoader("notify-msteams"),
    autoescape=select_autoescape()
)

nag_template = {
    'HOST' : 'host.json.jinja',
    'SERVICE' : 'service.json.jinja',
    # 'HOST' : 'host_simple.json.jinja',
    # 'SERVICE' : 'service_simple.json.jinja',
}

def _get_nagios_macros():
    """Read all ENV vars then save and rename the Nagios Macros in a dictionary."""
    MACROS=dict()
    for k, v in sorted(os.environ.items()):
        if k.startswith('NAGIOS_'):
            k = k.replace('NAGIOS_', '')
            MACROS[k] = v
    # Inject Nagios location for template base url.
    MACROS.update({'nagios_url': NAGIOS_URL})
    return MACROS

def send_to_teams(url, message_json, debug):
    """ posts the json message to the ms teams webhook url """
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=message_json, headers=headers)
    if r.status_code == requests.codes.ok:
        if debug:
            print('success')
        return True
    else:
        if debug:
            print('failure: {}'.format(r.reason))
        return False

def main():
    """receive nagios environment data and send notifications via MS-Teams"""

    parser = argparse.ArgumentParser()
    parser.add_argument('msgtype', action='store', help='message subject')
    parser.add_argument('--debug', action='store_true', help='print json message, etc. for debugging')
    parsedArgs = parser.parse_args()

    message_type = parsedArgs.msgtype
    debug = parsedArgs.debug
    macros = _get_nagios_macros()
    url = macros.get('_CONTACTWEBHOOKURL')
    # verify url defined
    if url is None:
        # error no url
        print('ERROR: no ms-teams webhook url was found')
        exit(2)

    # get the Jinja template for "HOST" or "SERVICE"
    t = env.get_template(nag_template.get(message_type))
    message_json = t.render(**macros)
    if debug:
        print(message_json + '\n\n--> ' + current_time )
    send_to_teams(url, message_json, debug)


if __name__=='__main__':
    main()
