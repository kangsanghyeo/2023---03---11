import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


url = 'https://comic.naver.com/webtoon/detail?titleId=648419&no=1' # 원하는 링크 입력 
site = requests.get(url, headers=headers) # 내용 가져오기
source1_data = site.text # 인터넷 소스코드를 source1_data변수에 저장

count1 = source1_data.count('" aria-current="') # 웹툰 제목 개수 가져오기

for i in range(count1): # 해당 개수만큼 반복
            
      pos1 = source1_data.find('<div class="flicking-camera episode_list">')+ len('<div class="flicking-camera episode_list">') # 링크앞부분 위치 지정
      source1_data = source1_data[pos1:] # 해당 위치로 이동

      pos2 = source1_data.find('<a href="')+ len('<a href="') # 링크앞부분 위치 지정
      source1_data = source1_data[pos2:] # 해당 위치로 이동  

      pos3 = source1_data.find('" aria-current="') # 링크뒷부분 위치 지정
      a_data = source1_data[: pos3].strip() # 앞부분 부터 뒷부분까지 내용 추출 해서 저장
      
      pos4 = source1_data.find('<p class="title">')+ len('<p class="title">') # 제목 앞부분 위치 지정
      source1_data = source1_data[pos4:] # 해당 위치로 이동

      pos5 = source1_data.find('</p>') # 제목 뒷부분 위치 지정
      b_data = source1_data[: pos5].strip() # 앞부분 부터 뒷부분 까지 내용 추출 해서 저장

      source1_data = source1_data[pos5+1:] # 다음 내용을 찾기위해 뒤부분 으로 이동사키기
      print(i+1, a_data, b_data) # 화면에 출력

      url = 'https://comic.naver.com/webtoon/detail?titleId=648419&no=1' # 링크 입력
      site = requests.get(url, headers=headers) # 내용 가져오기
      source2_data = site.text # 인터넷 소스 코드를 source2_data변수에 저장

      count2 = source2_data.count(' alt="comic content') # 개수 가져오기

      for u in range(count2): # 해당 개수만큼반복

            pos6 = source2_data.find('background:#FFFFFF">')+ len('background:#FFFFFF">') # 이미지 링크 앞부분 위치 지정
            source2_data = source2_data[pos6:] # 해당 위치로 이동

            pos7 = source2_data.find('<img src="')+ len('<img src="') # 이미지 링크 앞부분 위치 지정
            source2_data = source2_data[pos7:] # 해당 위치로 이동

            pos8 = source2_data.find('"') # 이미지 링크 뒷부분 위치 지정
            c_data = source2_data[: pos8] # 앞부분 부터 뒷부분 까지 내용 추출 해서 저장 
                  
            source2_data = source2_data[pos8+1:] # 다음 내용을 찾기위해 뒤부분을 이동시키기
            print(u+1, c_data) # 화면에 출력
            try:
                  file_name = './webtoon/{0}{1}{2}.{3}'.format('뷰티풀 군바리', b_data, i+1, c_data[-3:]) # 이미지 파일 이름 입력하기
                  ss = requests.get(c_data, headers=headers) # 
                  file = open(file_name, 'wb') # 
                  file.write(ss.content) # 
                  file.close() # 
            except Exception as e: # 
                  print('에러발생 : ', e) # 
                  
