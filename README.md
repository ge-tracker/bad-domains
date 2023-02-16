# Bad Domains

[blacklist.txt](https://raw.githubusercontent.com/ge-tracker/bad-domains/main/blacklist.txt) contains a list of domains that should be blacklisted from advert display.

## Usage

```bash
$ ./maintain.sh --help
usage: ./maintain.sh [OPTIONS]
    --help                              Show this message
    add <DOMAIN, [DOMAIN, ...]>         Add domains to the blacklist
    remove <DOMAIN, [DOMAIN, ...]>      Remove domains from the blacklist
    maintain                            Maintain the list of domains
```

Domains can be added or removed from the blacklist with the `add` and `remove` commands:

```bash
$ ./maintain.sh add example.com example.org
$ ./maintain.sh remove example.com example.org
```

The `blacklist.txt` file can also be modified directly and a workflow will automatically maintain the list for duplicates.
