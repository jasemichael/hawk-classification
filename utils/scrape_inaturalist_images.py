import urllib.request
import requests
import json
import os

def scrape_inaturalist_images(taxon_id, folder_name, per_page=200):
    count = 1
    page_num = 1
    while(True):
        response = requests.get(f"https://api.inaturalist.org/v1/observations?identified=true&photos=true&verifiable=true&quality_grade=research&taxon_id={taxon_id}&per_page={per_page}&page={page_num}")
        if not response.ok:
            break
        observations = json.loads(response.content)
        for j in range(len(observations["results"])):
            photos = observations["results"][j]["photos"]
            for k in range(len(photos)):
                photo = photos[k]["url"]
                photo = photo.replace("square", "medium")
                urllib.request.urlretrieve(photo, f"{folder_name}/inaturalist_{count}{os.path.splitext(photo)[1]}")
                count += 1
        page_num += 1

if __name__ == "__main__":
    scrape_inaturalist_images(5097, "/Users/jasemichael/Desktop/project_2/dataset/sharp_shinned")
    scrape_inaturalist_images(5212, "/Users/jasemichael/Desktop/project_2/dataset/red_tailed")