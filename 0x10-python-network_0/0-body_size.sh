#!/bin/bash
# A script to display the sixlze of a url response
curl -s --write-out "%{size_download}\n" "$1" | tail -1
