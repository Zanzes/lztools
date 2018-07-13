import argparse
import flickrapi

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

def search(term, count):
    c = 0
    photos = auth().photos_search(text=term, safe_search=3, per_page=50)["photos"]["photo"]
    for photo in photos:
        if c >= count:
            break
        yield load_url(photo)

def load_url(photo):
    r = auth().photos_getSizes(photo_id=photo["id"], secret=photo["secret"])
    image = sorted([add_total(i) for i in r["sizes"]["size"]], key=lambda x: x["total"]).pop()
    return image

def print_output(image, verbose=False):
    if verbose:
        print(u"Title: {}".format(image["title"]))
        print(u"Url: {}".format(image["url"]))
        print(u"Source: {}".format(image["source"]))
    else:
        print(image["source"])

# if __name__ == "__main__":
#     args = handle_args()
#     img = auth().photos_search(text=get_random_word(), safe_search=3, per_page=1)["photos"]["photo"].pop()
#     r = auth().photos_getSizes(photo_id=img["id"], secret=img["secret"])
#     image = sorted([add_total(i) for i in r["sizes"]["size"]], key=lambda x: x["total"]).pop()
#     print_output(args.verbose)