import urllib.request
import csv
import os

def scrape_ebird_images(dataset_path, csv_path):
    bird_type = os.path.basename(csv_path)
    if "sharp_shinned" in bird_type:
        dataset_path = os.path.join(dataset_path, "sharp_shinned", "ebird")
    elif "red_tailed" in bird_type:
        dataset_path = os.path.join(dataset_path, "red_tailed", "ebird")
    try:
        print("Attempting to create directory structure...")
        os.makedirs(dataset_path)
    except:
        print("Folders already created!")
    with open(csv_path, newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # skip the headers
        count = 1
        for row in reader:
            number = str(row[0])
            try:
                print(f"Scraping bird {number}...")
                urllib.request.urlretrieve(f"https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{number}", os.path.join(dataset_path, f"ebird_{count}.jpg"))
                count += 1
            except:
                print(f"Error scraping bird {number}...")