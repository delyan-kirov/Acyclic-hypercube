#!/usr/bin/env bash

echo "deleting images"
find -iname '*.png' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.cover' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.solution' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.txt' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l

rm n.param
rm -r conjure-output
rm boolean_copy.essence
rm result.g
rm workspace.g
