import json

file_path = 'C:\\Users\\tk1051984\\OneDrive - Bose Corporation\\Desktop\\20s_best_book.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
print(type(data))
print(data)

import pandas as pd
df = pd.DataFrame(data)
author_df = df[['ranking','bookname', 'authors']].copy()
print(author_df.head())
author_df.to_csv("ranking_book_authors_info.csv", index=False, encoding='utf-8-sig')