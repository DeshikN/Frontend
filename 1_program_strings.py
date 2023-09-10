"""
From below string,
Extract
IP
DATE
PICS
URL

Expected OUTPUT
# -------------------
123.123.123.123
26/Apr/2000
wpaper.gif
http://www.jafsoft.com/asctortf/
# -------------------
"""

print("in_string")
print("-"*20)
# -----------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(in_string)

print("-"*40)
# -----------------


print("type of in_string")
print("-"*20)
# -----------------

print(type(in_string))

print("-"*40)
# -----------------

print("IP : 1 - way to think")
print("-"*20)
# -----------------

index_of_first_space = in_string.index(' ')
print('index_of_first_space : ', index_of_first_space)
ip = in_string[0:index_of_first_space]
print('ip : ', ip)

print("-"*40)
# -----------------

print("IP : 2 - way to think")
print("-"*20)
# -----------------

sp = in_string.split()
print("sp : ", sp)
ip = sp[0]
print("ip : ", ip)

print("-"*40)
# -----------------

print("DATE : 1 - way to think")
print("-"*20)
# -----------------

index_of_first_square_bracket = in_string.index('[')
index_of_first_colon = in_string.index(':')
dt = in_string[ index_of_first_square_bracket + 1    :  index_of_first_colon ]
print('DATE : ', dt)

print("-"*40)
# -----------------

print("DATE : 2 - way to think")
print("-"*20)
# -----------------

sp = in_string.split()
print("sp : ", sp)
raw_date = sp[3]
print('raw_date : ', raw_date)
print('type of raw_date : ', type(raw_date)) # '[26/Apr/2000:00:23:48'

splitted_raw_date = raw_date.split(":")
print("splitted_raw_date : ", splitted_raw_date) # ['[26/Apr/2000', '00', '23', '48']

splitted_raw_date_2 = splitted_raw_date[0]
print('splitted_raw_date_2 : ', splitted_raw_date_2) # '[26/Apr/2000'

# Remove [
dt_1_way = splitted_raw_date_2.removeprefix('[')
print('DATE - 1 Way : ', dt_1_way)

dt_2_way = splitted_raw_date_2.split('[')
print('Splitted date : ', dt_2_way) # ['', '26/Apr/2000']
dt_2_way = dt_2_way[1] # OR dt_2_way[-1]
print('dt_2_way : ', dt_2_way)

# 3rd way 
dt_3_way = splitted_raw_date_2[1:]
print('dt_3_way : ', dt_3_way)

# replace('[', '')
# lstrip('[')
print("-"*40)
# -----------------

#PIC
print("PIC : 1 - way to think")
print("-"*20)
# -----------------
pic_data1 = sp[6]
print('pic_data1 : ' , pic_data1)#"/pics/wpaper.gif"
pic_data2=pic_data1.split('/')
print('pic_data2 :', pic_data2)#"", "pics", "wpaper.gif"
pic = pic_data2[2]
print('pic :', pic)# 'wpaper.gif'
print("-"*40)
# -----------------
print("PIC : 2 - way to think")
print("-"*20)
# -----------------
pic_data1 = sp[6]
print('pic_data1 : ' , pic_data1)#"/pics/wpaper.gif"
pic = pic_data1.replace('/pics/', '')
print('pic :', pic)
print("-"*40)
# -----------------
print("PIC : 3 - way to think")
print("-"*20)
# -----------------
pic_data1 = sp[6]
print('pic_data1 : ' , pic_data1)#"/pics/wpaper.gif"
pic = pic_data1.lstrip('/pics/')
print('pic :', pic)
print("-"*40)
# -----------------

#URL
print("URL : 1- way to think")
print("-"*20)
# -----------------
url_data= sp[-5]
print('url_data :', url_data)#'"http://www.jafsoft.com/asctortf/"'
url = url_data.replace('"', '')
print('url :', url)
print("-"*40)
# -----------------
print("URL : 2- way to think")
print("-"*20)
# -----------------
url_data= sp[-5]
print('url_data :', url_data)#'"http://www.jafsoft.com/asctortf/"'
url = url_data[1:-1]
print('url :', url)
print("-"*40)
# -----------------
print("URL : 3- way to think")
print("-"*20)
# -----------------
url_data= sp[-5]
print('url_data :', url_data)#'"http://www.jafsoft.com/asctortf/"'
url_data2 = url_data.split('"')
print('url_data2 :', url_data2)
url = url_data2[1]
print('url :', url)
print("-"*40)
# -----------------

# COMMENT - 1
'''
>>> s = 'XYXYXYWELCOME'
>>> s.removeprefix('XY')
'XYXYWELCOME'
>>> s.lstrip('XY')
'WELCOME'
'''
