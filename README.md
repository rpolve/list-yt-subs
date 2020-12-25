# List YT subs

Since the old subscription manager which allowed .xml export is now gone, a better way of extracting subscribed channels is to use Google API.

## Usage

It needs:
- a developer api key
- specified channel ID whose subscription list is set to public

Simply export the env vars `YT_CHANNEL_ID` and `YT_API_KEY` and run `subs.py`.

Returns:
- a list of channels IDs that the specified channel subscribes to

### Docker

```
docker build . -t list-subs
docker run --rm \
    -e YT_CHANNEL_ID=<...> \
    -e YT_API_KEY=<...> \
    list-subs
```

## Newsboat branch

It differs from main branch in that it lists the .xml feed urls and tags them in a format which newsboat will readily understand.
