#!/bin/bash
# A script to get a uri with  200 response code
curl -s --retry 0 "$1"
