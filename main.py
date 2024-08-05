from scrapeBase import extract_links
from siteData import SITE_DATA

def main():
    site_info = SITE_DATA['Nike']
    url = site_info['url']
    class_name = site_info['class_name']
    tag = site_info.get('tag', 'a')  #Default 'a'
    
    links = extract_links(url, class_name, tag)
    
    print(f"Links trovati su {site_name}:")
    for idx, link in enumerate(links, start=1):
        print(f"{idx}. {link}")

if __name__ == "__main__":
    main()
