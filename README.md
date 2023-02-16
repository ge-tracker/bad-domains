# Bad Domains

[blocklist.txt](https://raw.githubusercontent.com/ge-tracker/bad-domains/main/blocklist.txt) contains a list of domains that should be denied from advert display.

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

The `blocklist.txt` file can also be modified directly and a workflow will automatically maintain the list for duplicates.

### Getting domains from Google Search

I'm using [Serpapi](https://serpapi.com/) to quickly search Google for results for search queries relating to domains that should be denied. The resulting domains will be written to `blocklist.txt`, however, this will require some maintenance of `allowlist.txt` to stop domains such as `youtube.com` being blocked.

![](https://i.imgur.com/ufka8M4.png)

```bash
$ SERPAPI_API_KEY=abc123 ./search.py --help
usage: search.py [-h] [--query [QUERY ...]] [--pages PAGES] [--per-page PER_PAGE]

options:
  -h, --help           show this help message and exit
  --query [QUERY ...]  Search query
  --pages PAGES        Number of pages to fetch
  --per-page PER_PAGE  Number of results per page
```

We can submit custom queries, delimited by a space.

```bash
$ SERPAPI_API_KEY=abc123 ./search.py --query 'osrs botting' 'osrs bot' --pages 2 --per-page 10
```

