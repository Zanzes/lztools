import argparse

import flickrapi

from lztools.Data.Text import get_random_word

def auth():
    return flickrapi.FlickrAPI("2a41e37e58cd08c0dbd5af131441dca0", "72c6a92f49f48f9e", format="parsed-json")

res = auth().photos.getRecent()

def add_total(img):
    img["total"] = int(img["width"])+int(img["height"])
    return img

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", default=False, action='store_true',required=False)
    args = parser.parse_args()
    img = auth().photos_search(text=get_random_word(), safe_search=3, per_page=1)["photos"]["photo"].pop()
    # print("https://www.flickr.com/photos/{}/{}".format(p["owner"], p["id"]))
    r = auth().photos_getSizes(photo_id=img["id"], secret=img["secret"])
    image = sorted([add_total(i) for i in r["sizes"]["size"]], key=lambda x: x["total"]).pop()
    if args.verbose:
        print(u"Title: {}".format(img["title"]))
        print(u"Url: {}".format(image["url"]))
        print(u"Source: {}".format(image["source"]))
    else:
        print(image["source"])