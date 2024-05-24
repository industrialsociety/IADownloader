import os
import internetarchive

def download_collection(collection_id, dest_dir, report_interval=10):
    search = internetarchive.search_items(f'collection:{collection_id}')
    total_items = len(search)
    print(f"Found {total_items} items in the collection '{collection_id}'.")

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    downloaded_count = 0
    for idx, result in enumerate(search):
        item_id = result['identifier']
        item = internetarchive.get_item(item_id)
        item.download(dest_dir)
        downloaded_count += 1

        if (downloaded_count % report_interval) == 0 or downloaded_count == total_items:
            print(f"Downloaded {downloaded_count} out of {total_items} items...")

    print(f"Download complete. Total items downloaded: {downloaded_count}")

if __name__ == "__main__":
    collection_id = input("Enter the collection ID: ")
    dest_dir = "downloaded_files"
    download_collection(collection_id, dest_dir)
