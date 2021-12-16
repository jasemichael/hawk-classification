from scrape_inaturalist_images import scrape_inaturalist_images
from scrape_ebird_images import scrape_ebird_images

def generate_dataset(dataset_path, sharp_shinned_csv_path, red_tailed_csv_path):
    #scrape_inaturalist_images(5097, dataset_path)
    #scrape_inaturalist_images(5212, dataset_path)
    scrape_ebird_images(dataset_path, sharp_shinned_csv_path)
    scrape_ebird_images(dataset_path, red_tailed_csv_path)

if __name__ == '__main__':
    generate_dataset("C:\\Users\\jasemichael\\Desktop\\dataset", 'C:\\Users\\jasemichael\\Repositories\\hawk-classification\\csv\\sharp_shinned.csv', 'C:\\Users\\jasemichael\\Repositories\\hawk-classification\\csv\\red_tailed.csv')