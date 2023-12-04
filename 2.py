import xmltodict
import yaml

input = open('schedule.xml', 'r', encoding='utf-8')
output = open('scheduleFromLib.yaml', 'w', encoding='utf-8')

xmlstring = input.read()
xmldict = xmltodict.parse(xmlstring)
yaml.dump(xmldict, output, encoding='UTF-8', allow_unicode=True)