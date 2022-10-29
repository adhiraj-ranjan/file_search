import os
from fuzzywuzzy import fuzz

root_dir = input("Enter the root directory for your search: ")

file_types = input("Enter the file endings to look for (Separate by spaces) (Empty = ALL): ")
fuzzy_search= input("Enter a search query (Empty = None): ")
if fuzzy_search:
    p_f = int(input("Percentage of search query matching : "))
    

file_types = file_types.split()

for root, dirs, files in os.walk(root_dir):
    for name in files:
        if name.endswith(tuple(ft for ft in file_types)) or not file_types:
            if not fuzzy_search or fuzz.token_sort_ratio(fuzzy_search.lower(), name.lower()) > p_f:
                print (root + os.sep + name)