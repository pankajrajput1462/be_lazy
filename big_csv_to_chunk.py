import pandas as pd

fileUrl = 'resource\main.csv'
chunkFileName = 'Chunk_'
count = 1

for chunk in pd.read_csv(fileUrl, chunksize=500):
    print(chunk.shape)
    print(chunk)
    data_frame = pd.DataFrame(chunk, columns=['Header_1', 'Header_2', 'Header_3', 'Header_4'])
    data_frame.to_csv(chunkFileName + str(count) + '.csv', index=None)
    count += 1
