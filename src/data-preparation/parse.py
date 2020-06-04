import json

f = open('../../gen/data-preparation/temp/Team09_Ligue1/Ligue1ΓÇôCancellation.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

outfile.write('id\tlanguage\ttext\n')

cnt = 0
for line in con:
    if (len(line)<=5): continue

    cnt+=1
    obj = json.loads(line.replace('\n',''))

    text = obj.get('text')
    text = text.replace('\t', '').replace('\n', '').replace(',', '')

    lang = obj.get('lang')

    outfile.write(obj.get('id_str')+'\t'+str(lang)+'\t'+text+'\n')
    #if (cnt>1000): break

print('done.')
