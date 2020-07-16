import pandas as pd
from datetime import date

fileUrl_1 = 'file1.csv'
fileUrl_2 = 'file2.csv'

chunkFileName = 'MergedFile'
count = 1

date_today = str(date.today()).replace('-', '') + '_'
csv1 = pd.read_csv(fileUrl_1, sep='|')
csv2 = pd.read_csv(fileUrl_1, sep='|')
data_frame1 = pd.DataFrame(csv1, columns=['Header1', 'Header2', 'Header3', 'Header4', 'Header5', 'Header6',
                                          'Header7'])
data_frame2 = pd.DataFrame(csv2, columns=['Header1', 'Header2', 'Header3', 'Header4', 'Header5', 'Header6',
                                          'Header7'])
concat = pd.concat([data_frame1, data_frame2])
concat.to_csv(chunkFileName + date_today + str(count) + '.csv', index=None, sep='|')
