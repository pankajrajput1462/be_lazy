import pandas as pd
from datetime import date

fileUrl = 'resource\main.csv'
chunkFileName = 'Chunk_'
count = 1

for chunk in pd.read_csv(fileUrl, chunksize=500):
    print(chunk.shape)
    print(chunk)
    data_frame = pd.DataFrame(chunk, columns=['Header_1', 'Header_2', 'Header_3', 'Header_4'])
    data_frame.to_csv(chunkFileName + str(count) + '.csv', index=None)
    count += 1


    
# with specific seperator
for chunk in pd.read_csv(fileUrl, chunksize=100, sep='|'):
    print(chunk.shape)
    data_frame = pd.DataFrame(chunk,
                              columns=['Header_1', 'Header_2', 'Header_3', 'Header_4', 'Header_5', 'Header_6',
                                       'Header_7'])
    data_frame.to_csv(chunkFileName + str(count) + '.csv', index=None, sep='|')
    count += 1

    
   
date_today = str(date.today()).replace('-', '') + '_'

for chunk in pd.read_csv(fileUrl, chunksize=10000, sep='|'):
    print(chunk.shape)
    data_frame = pd.DataFrame(chunk,
                              columns=['Header', 'Header', 'Header', 'Header', 'Header', 'Header',
                                       'Header'])
    data_frame.to_csv(chunkFileName + date_today + str(count) + '.csv', index=None, sep='|')
    count += 1
