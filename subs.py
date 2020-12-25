#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import googleapiclient.discovery
import re
import os


def get_subs(page_token=None):
    channel_id = os.environ.get('YT_CHANNEL_ID')
    developer_key = os.environ.get('YT_API_KEY')

    api_service_name = "youtube"
    api_version = "v3"
    max_results = 50
    part = "snippet,contentDetails"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key
    )

    if page_token:
        request = youtube.subscriptions().list(
            channelId=channel_id,
            maxResults=max_results,
            pageToken=page_token,
            part=part,
        )
    else:
        request = youtube.subscriptions().list(
            channelId=channel_id, maxResults=max_results, part=part
        )

    response = request.execute()
    items = response["items"]

    if "nextPageToken" in response.keys():
        items += get_subs(response["nextPageToken"])

    return items


def main():
    pattern = re.compile('[^A-Za-z0-9 ]+')

    for i in get_subs():
        i = i["snippet"]
        title = pattern.sub('', i["title"]).rstrip()
        channel_id = i["resourceId"]["channelId"]
        feed = "https://www.youtube.com/feeds/videos.xml?channel_id=" + channel_id
        print(feed, '"~' + title + '" video')


if __name__ == "__main__":
    main()
