#!/bin/bash

# This script doesn't do much on its own. It is useful mainly with another
# script called reuuid.sh.
# These scripts were shared by someone on PL-Slack -- I didn't write them.
#
# Requires the uuidgen command to be installed on the system.
# This is generally pretty easy to install in Linux or Mac -- not sure about
# Windows.

uuid=`uuidgen`
echo \ \ \  \"uuid\": \"$uuid\",
