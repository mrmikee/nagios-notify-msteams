#!/bin/bash
# export some test values that Nagios would have sent us via environment variables.

# COMMON to both HOST and SERVICE
export NAGIOS__CONTACTWEBHOOKURL="https://your-connector-url-here/"
# state_color value is from MS-Teams Adaptive Card styling.
#export NAGIOS_state_color="good"

export NAGIOS_NOTIFICATIONTYPE="CUSTOM"
export NAGIOS_NOTIFICATIONAUTHOR="Contact Name Here"
export NAGIOS_NOTIFICATIONCOMMENT="SysAdmin running a notification test (SORRY, PLEASE IGNORE)"

export NAGIOS_HOSTNAME="TEST-HOST-IGNORE"
export NAGIOS_HOSTNOTES="notes from test-host (IGNORE)"
export NAGIOS__HOSTRESTORE_PRIORITY="(999-nagios-test-priority)"
# END COMMON


# SERVICE ONLY
export NAGIOS_SERVICEDESC="test-service (ignore)"
export NAGIOS_SERVICESTATE="UNKNOWN"
export NAGIOS_SERVICEOUTPUT="test output from testing-service (ignore)"


# HOST ONLY
export NAGIOS_HOSTSTATE="UNREACHABLE"
export NAGIOS_HOSTOUTPUT="nagios host output test IGNORE."

#./notify-msteams.py SERVICE --debug
./notify-msteams.py HOST --debug