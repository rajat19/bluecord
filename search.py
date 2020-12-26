#!/usr/bin/env python
__author__ = 'Rajat Srivastava'

import pprint
import settings as my_settings
from googleapiclient.discovery import build


def search_main(query):
    service = build("customsearch", "v1",
                    developerKey=my_settings.GOOGLE_API_KEY)

    result = service.cse().list(
        q=query,
        cx=my_settings.GOOGLE_CSE_KEY,
    ).execute()
    # print("response", result)
    try:
        items = result["items"]
        top_five_links = []
        for i in items:
            if(len(top_five_links) < 5):
                top_five_links.append(i["link"])
        pprint.pprint(result["items"])
        # print(top_five_links)
        return top_five_links
    except:
        return