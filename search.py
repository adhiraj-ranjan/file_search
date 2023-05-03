import os
from fuzzywuzzy import fuzz

root_dir = input("Enter the root directory for your search: ")

if not os.path.exists(root_dir):
    print("[ ERROR ] the path is not found")
    exit(0)

file_types = input("Enter the file endings to look for (Separate by spaces) (Empty = ALL): ")
search_query= input("Enter a search query (Empty = None): ")
if search_query:
    p_f = int(input("Percentage of search query matching : "))
    

file_types = tuple(f for f in file_types.split())

print()
for _, dirs, files in os.walk(root_dir):
    for name in files:
        if not file_types or name.endswith(file_types):
            if not search_query or fuzz.token_sort_ratio(search_query.lower(), name.lower()) > p_f:
                print(root_dir + os.sep + name)