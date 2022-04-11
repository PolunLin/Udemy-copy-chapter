


from reprlib import recursive_repr
from bs4 import BeautifulSoup
# import required module
from pathlib import Path
import re
# assign directory
directory = 'course_html'
 
# iterate over files in
# that directory
files = Path(directory).glob('*.html')
for file in files:
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        tags = soup.find_all('div',class_='section--panel--1tqxC')## section tag
        course_name = soup.find('div',class_="lead--title--2Wz2g")
        # print(file)
        # result_file_name =re.sub(".html","",str(file))
        with open("course_result/"+file.stem +".txt" ,"w") as result:
            result.write(f"### Course name : {course_name.text}\n")
            for i,tag in enumerate(tags):
                    result.write("<details>\n\t")
                    result.write("<summary>\n")
                    result.write(f" {str(i)}. {tag.find_next(class_='section--section-title--8blTh').text} ") # chapter tag
                    result.write(f'{tag.find_next(class_="section--section-content--9kwnY").text}\n') # chapter information
                    result.write("</summary>\n\n")
                    courses = tag.find_all('span','section--item-title--2k1DQ') # course tag
                    courses_info = tag.find_all('span','section--item-content-summary--126oS') # course infomation
                    
                    for ix,(course,info) in enumerate(zip(courses,courses_info)):
                        
                        result.write(f'\t{str(i)}.{str(ix)}. {course.text} ')
                        result.write(f'{info.text}\n')
                        
                    result.write("\n</details>\n")
                
            # break
            
            # break
            

# for city in soup.find_all('span', {'class' : 'city-sh'}):
#     print(city)