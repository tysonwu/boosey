import os
import urllib.request
from tqdm import tqdm

def add_zeros(x):
    return '0' * (4 - len(x)) + str(x)

def make_page_list(start_page, end_page):
    return [add_zeros(str(page_number)) for page_number in range(int(start_page), int(end_page)+1)]


base = '/Users/TysonWu/dev/boosey/'
os.chdir(base)

# input parameters---------------------------
url = 'https://scoreserver.boosey.com/api/image/get/1ousnblpqwr_1324_v2/'
key = '89f3d383-373f-4a3d-ad53-830cf80ccf9c'
output_folder = 'sym3'
start_page = '0001'
end_page = '0130'
# --------------------------------------------


pages = make_page_list(start_page, end_page)
os.mkdir(base + output_folder)
os.chdir(base + output_folder)

for page in tqdm(pages):
    urllib.request.urlretrieve(url+'page'+page+'_1.jpg?uni='+key, page+'.jpg')
