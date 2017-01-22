#!/bin/bash
read x
printf "%.3f" "$(bc -l <<< "$x")"