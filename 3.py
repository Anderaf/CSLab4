import re

input = open('schedule.xml', 'r', encoding='utf-8')
output = open('scheduleRegex.yaml', 'w', encoding='utf-8')

xmlstring = input.read()

xmlstring = re.sub(r'(\w+)=\"([^\"]*)\"', r'\n "@\1": \2', xmlstring)
xmlstring = re.sub(r'(<)(\w+)([ \w\n:@\"-]*?)(>\n)', r"\2:\3\n", xmlstring)
xmlstring = re.sub(r'(<)([\w\n:@\"-]+)([ \w\n:@\"-]*?)(>)', r"\2: \3", xmlstring)
xmlstring = re.sub(r'[ \n]*</.*>', "", xmlstring)
xmlstring = re.sub(r'(^)( )([^ ])', r"    \3", xmlstring, flags=re.MULTILINE)
xmlstring = re.sub(r'^ ', "", xmlstring, flags=re.MULTILINE)
xmlstring = re.sub(r'   ', " ", xmlstring)
#xmlstring = xmlstring.replace('<schedule', '---\nschedule:').replace('lang="ru"', '\n    "-lang": ru').replace('group="P3114"', '\n    "-group": P3114').replace('day="thursday"', '\n    "-day": thursday').replace('>', '', 1)
#xmlstring = xmlstring.replace('<lessons>', 'lessons:').replace('</lessons>\n', '')
#xmlstring = xmlstring.replace('<lesson1>', 'lesson1:').replace('<lesson2>', 'lesson2:').replace('<lesson3>', 'lesson3:').replace('<lesson4>', 'lesson4:')
#xmlstring = xmlstring.replace('<lesson-type>', 'lesson-type: ').replace('<time>', 'time: ' ).replace('<name>', 'name: ').replace('<teacher>', 'teacher: ').replace('<location>', 'location: ')
#xmlstring = re.sub(r'</.*>', '', xmlstring)
xmlstring = re.sub(r'(\d{2}:\d{2})', r'"\1"', xmlstring)
output.write(xmlstring)
print(xmlstring)