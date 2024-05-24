import internetarchive

def download_collection(collection_id, dest_dir):
    search = internetarchive.search_items(f'collection:{collection_id}')
    for result in search:
        item_id = result['identifier']
        item = internetarchive.get_item(item_id)
        item.download(dest_dir)

if __name__ == "__main__":
    collection_id = "xxxxxxxxxxx"
    dest_dir = "downloaded_files"
    download_collection(collection_id, dest_dir)
