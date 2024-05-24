import os
import internetarchive
import sys

def download_collection(collection_id, report_interval=10):
    search = internetarchive.search_items(f'collection:{collection_id}')
    total_items = len(search)
    print(f"Found {total_items} items in the collection '{collection_id}'.")

    dest_dir = os.path.join("downloaded_files", collection_id)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    downloaded_count = 0
    for idx, result in enumerate(search):
        item_id = result['identifier']
        item = internetarchive.get_item(item_id)
        item.download(dest_dir)
        downloaded_count += 1

        if (downloaded_count % report_interval) == 0 or downloaded_count == total_items:
            sys.stdout.write(f"\rDownloaded {downloaded_count} out of {total_items} items...")
            sys.stdout.flush()

    print(f"\nDownload complete. Total items downloaded: {downloaded_count}")

if __name__ == "__main__":
    collection_id = input("Enter the collection ID: ")
    download_collection(collection_id)
