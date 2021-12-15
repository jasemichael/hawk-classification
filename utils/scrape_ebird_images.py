import urllib.request
import csv

def scrape_ebird_images(folder_name, csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # skip the headers
        count = 1
        for row in reader:
            number = row[0]
            urllib.request.urlretrieve(f"https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{number}", f"{folder_name}/ebird_{count}")
            count += 1

if __name__ == '__main__':
    scrape_ebird_images('/Users/jasemichael/Desktop/project_2/dataset/sharp_shinned', '/Users/jasemichael/Desktop/project_2/csv/sharp_shinned.csv')
    scrape_ebird_images('/Users/jasemichael/Desktop/project_2/dataset/red_tailed', '/Users/jasemichael/Desktop/project_2/csv/red_tailed.csv')