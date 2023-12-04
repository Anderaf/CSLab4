import xmltodict
import yaml
import time

input = open('schedule.xml', 'r', encoding='utf-8')
output = open('scheduleFromLib.yaml', 'w', encoding='utf-8')

start_time = time.perf_counter()
xmlstring = input.read()
for i in range(100):
    xmldict = xmltodict.parse(xmlstring)
    yaml.dump(xmldict, output, encoding='UTF-8', allow_unicode=True)
print(time.perf_counter() - start_time)
