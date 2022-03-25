import json
with open('cityNames.json', 'r') as f:
    citylist = json.load(f)

# # h3
# result = {}
# for city in citylist:
# 	with open('./cities/'+city+'.json','r',encoding='UTF-8') as f:
# 		h2List = []
# 		contentList = json.load(f)
# 		for content in contentList:
# 			if 'h3' in content:
# 				if content['h3'] not in h2List:
# 					h2List.append(content['h3'])
# 		result[city]=h2List
# with open('./h3.json','w',encoding='UTF-8') as f:
# 	json.dump(result, f)

# # h2
# result = {}
# for city in citylist:
# 	with open('./cities/'+city+'.json','r',encoding='UTF-8') as f:
# 		h2List = []
# 		contentList = json.load(f)
# 		for content in contentList:
# 			if content['h2'] not in h2List:
# 				h2List.append(content['h2'])
# 		result[city]=h2List
# with open('./h2.json','w',encoding='UTF-8') as f:
# 	json.dump(result, f)

# # h2-all
# result = []
# for city in citylist:
# 	with open('./cities/'+city+'.json','r',encoding='UTF-8') as f:
# 		contentList = json.load(f)
# 		for content in contentList:
# 			if content['h2'] not in result:
# 				result.append(content['h2'])
# with open('./h2-all.json','w',encoding='UTF-8') as f:
# 	json.dump(result, f)

# # h3-all
# result = []
# for city in citylist:
# 	with open('./cities/'+city+'.json','r',encoding='UTF-8') as f:
# 		contentList = json.load(f)
# 		for content in contentList:
# 			if 'h3' in content:
# 				if content['h3'] not in result:
# 					result.append(content['h3'])
# with open('./h3-all.json','w',encoding='UTF-8') as f:
# 	json.dump(result, f)

# level
# result = {}
# for city in citylist:
# 	with open('./cities/'+city+'.json','r',encoding='UTF-8') as f:
# 		contentList = json.load(f)
# 		head_dic = {}
# 		for content in contentList:
# 			if content['h2'] not in head_dic:
# 				head_dic[content['h2']] = []
# 			if 'h3' in content:
# 				head_dic[content['h2']].append(content['h3'])
# 		result[city] = head_dic
# with open('./level.json','w',encoding='UTF-8') as f:
# 	json.dump(result, f)
# from fuzzywuzzy import fuzz, process
# with open('./level.json', 'r', encoding='UTF-8') as f:
#     level_dic = json.load(f)
# city = '北京市'
# h2List = list(level_dic[city])
# question = "简称"
# h2Fuzzyresult = process.extractOne(question, h2List)
# print(h2Fuzzyresult)
from urllib.parse import quote, unquote
print(unquote("%D6%D0%B9%FA%B5%C4%CA%D7%B6%BC%CA%C7",encoding="GBK"))