#!/bin/bash
set -e
#set -x
printf "${COLOR_YELLOW}\n`date`\n\n${COLOR_NONE}" >> logs.txt
trap 'echo "%3d: " "$LINENO" >> logs.txt' DEBUG

COLOR_RED='\033[0;31m'
COLOR_GREEN='\033[1;32m'
COLOR_ORANGE='\033[0;33m'
COLOR_YELLOW='\033[1;33m'
COLOR_PURPLE='\033[1;35m'
COLOR_CYAN='\033[1;36m'
COLOR_NONE='\033[0m'


setup () {
	if [ ! -f ./lists/main.pool ]; then
		touch ./lists/main.pool
	fi
	if [ ! -f ./logs.txt ]; then
		touch ./logs.txt
	fi
}

helpme () {
	printf "\n\t ${COLOR_ORANGE}./drop.sh [command] [arguments]"
	printf "\n\n\t ${COLOR_CYAN}drop add [args]"
	printf "\n\t\t ${COLOR_PURPLE}Adds a point to your todo list."
	printf "\n\t\t ${COLOR_}-t ) Start and finish time, formatted as {DDMMYYYY-HHMM}"
	printf "\n\n ${COLOR_NONE}"
}

add () {
	if [[ `grep -nw "${OPTARG}" ./lists/main.pool` != "" ]]; then
		printf "\n ${COLOR_ORANGE}Entrypoint already exists!${COLOR_NONE}"
	else
		echo "-[]${OPTARG}"	>> ./lists/main.pool
	fi
}

remove () {
	while read p; do
  	if [[ $p == "-[]${OPTARG}" ]]; then
			sed -i -e "s/-\[]${OPTARG}//g" ./lists/main.pool
		else
			echo "false"
		fi
	done <./lists/main.pool
}

while getopts a:r:s: option
do
	case "${option}"
	in
		s) setup;;
		a) add;;
		r) remove;;
	esac
done
