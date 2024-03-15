import json
import re


def receive_content_info_from_har(har_file_name: str) -> dict[str, set[str]]:
    with open(har_file_name) as f:
        data = f.read()
    har_json = json.loads(data)

    entries: list = har_json["log"]["entries"]
    url_regex = re.compile(r"/(\d+)\.(\w+)\??")
    extension_with_ids: dict[str, set[str]] = {}

    for entry in entries:
        response_status: int = entry["response"]["status"]
        if response_status != 200:
            continue
        request = entry["request"]
        url_regex_search = url_regex.search(request["url"])
        if url_regex_search is None:
            continue
        identification, extension = url_regex_search.groups()
        if extension not in extension_with_ids:
            extension_with_ids[extension] = set()
        extension_with_ids[extension].add(identification)
    return extension_with_ids
