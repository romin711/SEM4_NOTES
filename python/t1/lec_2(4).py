# filtering data

import pandas as pd

df = pd.read_csv('ipl-matches.csv')
# print(df)

rr = df[(df['Venue'] == 'Narendra Modi Stadium, Ahmedabad') & (df['TossWinner'] == 'Rajasthan Royals')]
# print(rr)

mi = df[(df['Venue'] == 'Wankhede Stadium') & (df['Player_of_Match'] == 'RG Sharma') & (df['WinningTeam'] == 'Mumbai Indians')]
# print(mi)

team_loss = df[(df['Margin'] > 50)]
# print(team_loss)




super_over = df[(df['SuperOver'] == 'Y')]
# print(super_over)

csk_kolakat = df[(df['WinningTeam'] == 'Chennai Super Kings') & (df['Venue'] == 'Eden Gardens')]
# print(csk_kolakat)
# print(csk_kolakat.shape[0])

msdhoni = df[(df['Player_of_Match'] == 'MS Dhoni') & ( (df['Team1'] == 'Mumbai Indians') | (df['Team2'] == 'Mumbai Indians'))]
print(msdhoni)

