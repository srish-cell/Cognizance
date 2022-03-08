import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
Ser=""
for i in range (len(ser)):
    ser[i]=ser[i].capitalize()
    Ser=Ser+ser[i]+" "
print(Ser)