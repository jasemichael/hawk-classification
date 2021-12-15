from scrape_inaturalist_images import scrape_inaturalist_images
from scrape_ebird_images import scrape_ebird_images

def scrape_images():
    scrape_inaturalist_images(5097, "/Users/jasemichael/Desktop/project_2/dataset/sharp_shinned")
    scrape_inaturalist_images(5212, "/Users/jasemichael/Desktop/project_2/dataset/red_tailed")
    scrape_ebird_images('/Users/jasemichael/Desktop/project_2/dataset/sharp_shinned', '/Users/jasemichael/Desktop/project_2/csv/sharp_shinned.csv')
    scrape_ebird_images('/Users/jasemichael/Desktop/project_2/dataset/red_tailed', '/Users/jasemichael/Desktop/project_2/csv/red_tailed.csv')

if __name__ == '__main__':
    scrape_images()