import time

input = open('schedule.xml', 'r', encoding='utf-8')
output = open('schedule.yaml', 'w', encoding='utf-8')

start_time = time.perf_counter()
for i in range(100):
    xmlstring = input.read()

    xmlstring = xmlstring.replace('<schedule', '---\nschedule:').replace('lang="ru"', '\n    "@lang": ru').replace('group="P3114"', '\n    "@group": P3114').replace('day="thursday"', '\n    "@day": thursday').replace('>', '', 1)
    xmlstring = xmlstring.replace('<lessons>', 'lessons:').replace('</lessons>\n', '')
    xmlstring = xmlstring.replace('<lesson1>', 'lesson1:').replace('<lesson2>', 'lesson2:').replace('<lesson3>', 'lesson3:').replace('<lesson4>', 'lesson4:')
    xmlstring = xmlstring.replace('<lesson-type>', 'lesson-type: ').replace('<time>', 'time: ' ).replace('<name>', 'name: ').replace('<teacher>', 'teacher: ').replace('<location>', 'location: ')
    xmlstring = xmlstring.replace('</lesson-type>', '').replace('</time>', '').replace('</name>', '').replace('</teacher>', '').replace('</location>', '')
    xmlstring = xmlstring.replace('</lesson1>', '').replace('</lesson2>', '').replace('</lesson3>', '').replace('</lesson4>\n', '').replace('</schedule>', '')
    xmlstring = xmlstring.replace('08:20', "'08:20'").replace('10:00', "'10:00'").replace('13:30', "'13:30'").replace('15:20', "'15:20'")
    output.write(xmlstring)
print(time.perf_counter() - start_time)
