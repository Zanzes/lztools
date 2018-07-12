import argparse
import random

import flickrapi

from lztools.DataTypes.LazyVariable import LazyVariable
from lztools.IO import read_words_from_disk

words = None
import inspect

import gc

def find_names(obj):
    frame = inspect.currentframe()
    for frame in iter(lambda: frame.f_back, None):
        frame.f_locals
    obj_names = []
    for referrer in gc.get_referrers(obj):
        if isinstance(referrer, dict):
            for k, v in referrer.items():
                if v is obj:
                    obj_names.append(k)
    return obj_names

words = LazyVariable()



def auth():
    return flickrapi.FlickrAPI("2a41e37e58cd08c0dbd5af131441dca0", "72c6a92f49f48f9e", format="parsed-json")

res = auth().photos.getRecent()

def add_total(img):
    img["total"] = int(img["width"])+int(img["height"])
    return img

def get_all_words():
    global words
    if words is None:
        words = read_words_from_disk()
    return words


def get_random_word():
    return random.choice(get_all_words())

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