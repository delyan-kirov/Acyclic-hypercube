#!/usr/bin/env bash
find -iname '*.solution' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
