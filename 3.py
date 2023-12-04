import re
import time

input = open('schedule.xml', 'r', encoding='utf-8')
output = open('scheduleRegex.yaml', 'w', encoding='utf-8')

start_time = time.perf_counter()
for i in range(100):
    xmlstring = input.read()
    xmlstring = re.sub(r'(\w+)=\"([^\"]*)\"', r'\n "@\1": \2', xmlstring)
    xmlstring = re.sub(r'(<)(\w+)([ \w\n:@\"-]*?)(>\n)', r"\2:\3\n", xmlstring)
    xmlstring = re.sub(r'(<)([\w\n:@\"-]+)([ \w\n:@\"-]*?)(>)', r"\2: \3", xmlstring)
    xmlstring = re.sub(r'[ \n]*</.*>', "", xmlstring)
    xmlstring = re.sub(r'(^)( )([^ ])', r"    \3", xmlstring, flags=re.MULTILINE)
    xmlstring = re.sub(r'^ ', "", xmlstring, flags=re.MULTILINE)
    xmlstring = re.sub(r'   ', " ", xmlstring)
    xmlstring = re.sub(r'(\d{2}:\d{2})', r'"\1"', xmlstring)
    output.write(xmlstring)
print(time.perf_counter() - start_time)
