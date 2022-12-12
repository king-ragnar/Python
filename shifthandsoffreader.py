import pandas as pd

x=pd.read_excel('Shift.xlsx',sheet_name="October")
y = pd.read_excel('swiperecords.xlsx')

core = x[x.columns[1:5]]
morning={}
noon = {}
night = {}

for indexx, row in core.iterrows():
    morning[row['Date'].day] = row['1st Shift SME']
    noon[row['Date'].day] = row['2nd Shift SME']
    night[row['Date'].day] = row['3rd Shift SME']

for indexx,row in y.iterrows():
    if row['Swipe In']>5 and row['Swipe In']<=6 and row['Name'] in morning[row['Date'].day]:
        pass
    elif row['Swipe In']>1 and row['Swipe In']<=2 and noon[row['Date'].day] == row['Name']:
        pass
    elif row['Swipe In']>9 and row['Swipe In']<=10 and night[row['Date'].day] == row['Name']:
        pass
    elif pd.isna(row['Swipe In']) and (row['Name'] not in morning[row['Date'].day]) and (row['Name'] not in night[row['Date'].day]) and (row['Name'] not in noon[row['Date'].day]):
        pass
    else:
        print("False record for the date "+str(row['Date'].day)+" by the employee"+row['Name'])
        #print(row['Swipe In'])





