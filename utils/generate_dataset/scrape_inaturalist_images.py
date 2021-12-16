import urllib.request
import requests
import json
import os
import time

def scrape_inaturalist_images(taxon_id, dataset_path, per_page=200):
    count = 1
    page_num = 1
    done = False
    if taxon_id == 5097:
        dataset_path = os.path.join(dataset_path, "sharp_shinned", "inaturalist")
    elif taxon_id == 5212:
        dataset_path = os.path.join(dataset_path, "red_tailed", "inaturalist")
    try:
        print("Attempting to create directory structure...")
        os.makedirs(dataset_path)
    except:
        print("Folders already created!")
    while not done:
        response = requests.get(f"https://api.inaturalist.org/v1/observations?identified=true&photos=true&verifiable=true&quality_grade=research&taxon_id={taxon_id}&per_page={per_page}&page={page_num}")
        if not response.ok:
            done = True
        observations = json.loads(response.content)
        for j in range(len(observations["results"])):
            photos = observations["results"][j]["photos"]
            for k in range(len(photos)):
                photo = photos[k]["url"]
                #photo = photo.replace("square", "medium")
                try:
                    print(f"Scraping bird {count}...")
                    urllib.request.urlretrieve(photo, f"{dataset_path}/inaturalist_{count}{os.path.splitext(photo)[1]}")
                except:
                    print("Exception occurred! Sleeping...")
                    time.sleep(5)
                count += 1
        page_num += 1

if __name__ == "__main__":
    scrape_inaturalist_images(5097, "C:\\Users\\jasemichael\\Desktop\\dataset")
    scrape_inaturalist_images(5212, "C:\\Users\\jasemichael\\Desktop\\dataset")