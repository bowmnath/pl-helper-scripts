#!/bin/bash

# Run `reuuid.sh info.json` or `reuuid.sh infoAssessment.json` to change
# the info file's UUID in place.
#
# Requires newuuid.sh to run.
# These scripts were shared by someone on PL-Slack -- I didn't write them.

sed -i "s/.*uuid.*/$(newuuid.sh)/" $1
