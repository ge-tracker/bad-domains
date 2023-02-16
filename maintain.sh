#!/bin/bash

# Unify locale settings temporarily to make sort produce the same order
LC_ALL=C
export LC_ALL

help() {
  cat <<EOF
usage: $0 [OPTIONS]
    --help                              Show this message
    add <DOMAIN, [DOMAIN, ...]>         Add domains to the blacklist
    remove <DOMAIN, [DOMAIN, ...]>      Remove domains from the blacklist
    maintain                            Maintain the list of domains
EOF
}

add_domains() {
  echo "Adding $# domains..."
  echo "$@" | tr ' ' '\n' >>blocklist.txt
}

remove_domains() {
  echo "Removing $# domains..."
  for domain in "$@"; do
    sed -i "/^${domain}$/d" blocklist.txt
  done
}

# Converts uppercase to lowercase, sorts, and removes duplicates and CRs
# The allowlist is then applied to the blocklist
maintain() {
  cat allowlist.txt | tr '[:upper:]' '[:lower:]' | sort -f | uniq -i >tmp.txt
  sed -i 's/\r$//g' tmp.txt
  mv tmp.txt allowlist.txt

  cat blocklist.txt | tr '[:upper:]' '[:lower:]' | sort -f | uniq -i >tmp.txt
  sed -i 's/\r$//g' tmp.txt
  comm -23 tmp.txt allowlist.txt >blocklist.txt
  rm -f tmp.txt

  echo "Blacklist sorted and de-duplicated!"
}

# Run maintain if no args
if [[ $# -eq 0 ]]; then
  maintain
  exit 0
fi

# Check args
for opt in "$1"; do
  case $opt in
  --help)
    help
    exit 0
    ;;
  maintain)
    maintain
    exit 0
    ;;
  add)
    add_domains "${@:2}"
    maintain
    exit 0
    ;;
  remove)
    remove_domains "${@:2}"
    maintain
    exit 0
    ;;
  esac
done
