import argparse
from builtins import map
from functools import partial
from types import GeneratorType

import flickrapi

from lztools.Data.Text import get_random_word

def auth():
    return flickrapi.FlickrAPI("2a41e37e58cd08c0dbd5af131441dca0", "72c6a92f49f48f9e", format="parsed-json")

def add_total(img):
    img["total"] = int(img["width"])+int(img["height"])
    return img

def handle_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", default=False, action='store_true', required=False)
    args = parser.parse_args()
    return args

def load_url(photo):
    sizes = auth().photos_getSizes(photo_id=photo["id"], secret=photo["secret"])
    return sorted([add_total(i) for i in sizes["sizes"]["size"]], key=lambda x: x["total"]).pop()

def search(term, count=1, verbose=False):
    photos = auth().photos_search(text=term, safe_search=3, per_page=count)["photos"]["photo"]
    return get_outputs(map(load_url, photos), verbose)

def get_random_image(verbose=False):
    while True:
        res = search(get_random_word(), count=1, verbose=verbose)
        for x in res:
            if x != "" and x is not None:
                return x

def get_outputs(images, verbose):
    for x in images:
        if isinstance(x, GeneratorType):
            for y in x:
                yield get_output(y, verbose)
        else:
            yield get_output(x, verbose)

def get_output(image, verbose=False):
    if verbose:
        s = u"Title: {}\nUrl: {}\nSource: {}".format(image["title"], image["url"], image["source"])
    else:
        s = image["source"]
    return s