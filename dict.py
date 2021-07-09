# DICTIONARY, СЛОВАРЬ

# d = {'key':'value'}
# data = {'name':'ulan',
#         'surname':'temirbekov',
#         'phone':'+996700700700',
#         'age:':20,
#         'friends': [
#             'amna', 'dima', 'emir', 'abdullah', 'amirkhan',
#             'maksat', 'omurbek'
#         ]
# }

# print(dir(data))
# data.clear() - clear dictionary


# print(data.get('name'))
# print(data.get('phone'))
# print(data.get('friends'))
# print(data.get('adress', 'default'))
# print(data['friends'])
# print(data.items())

# print(list.data.items()[0])

# print(data.keys())
# print(data.values())

# data.pop('name')
# print(data)


# data.popitem()
#
# nums = {1: 2,
#         3: 4
#     }
# n = {5: nums}
# n = {5: 6}

# nums.update(n)
# print(nums, n)
#   or
# print({**nums, **n})



# for key, value in data.items():
#     print(f'this is a key {key} and this is a value {value}')


# asd = 'qowpoeeidk'
# b = [1, 2, 3, 4]
# c = 34567890
# d = {5: 6,7: 8 }


# data = {"web-app": {
#     "servlet": [
#         {
#             "servlet-name": "cofaxCDS",
#             "servlet-class": "org.cofax.cds.CDSServlet",
#             "init-param": {
#                 "configGlossary:installationAt": "Philadelphia, PA",
#                 "configGlossary:adminEmail": "ksm@pobox.com",
#                 "configGlossary:poweredBy": "Cofax",
#                 "configGlossary:poweredByIcon": "/images/cofax.gif",
#                 "configGlossary:staticPath": "/content/static",
#                 "templateProcessorClass": "org.cofax.WysiwygTemplate",
#                 "templateLoaderClass": "org.cofax.FilesTemplateLoader",
#                 "templatePath": "templates",
#                 "templateOverridePath": "",
#                 "defaultListTemplate": "listTemplate.htm",
#                 "defaultFileTemplate": "articleTemplate.htm",
#                 "useJSP": False,
#                 "jspListTemplate": "listTemplate.jsp",
#                 "jspFileTemplate": "articleTemplate.jsp",
#                 "cachePackageTagsTrack": 200,
#                 "cachePackageTagsStore": 200,
#                 "cachePackageTagsRefresh": 60,
#                 "cacheTemplatesTrack": 100,
#                 "cacheTemplatesStore": 50,
#                 "cacheTemplatesRefresh": 15,
#                 "cachePagesTrack": 200,
#                 "cachePagesStore": 100,
#                 "cachePagesRefresh": 10,
#                 "cachePagesDirtyRead": 10,
#                 "searchEngineListTemplate": "forSearchEnginesList.htm",
#                 "searchEngineFileTemplate": "forSearchEngines.htm",
#                 "searchEngineRobotsDb": "WEB-INF/robots.db",
#                 "useDataStore": True,
#                 "dataStoreClass": "org.cofax.SqlDataStore",
#                 "redirectionClass": "org.cofax.SqlRedirection",
#                 "dataStoreName": "cofax",
#                 "dataStoreDriver": "com.microsoft.jdbc.sqlserver.SQLServerDriver",
#                 "dataStoreUrl": "jdbc:microsoft:sqlserver://LOCALHOST:1433;DatabaseName=goon",
#                 "dataStoreUser": "sa",
#                 "dataStorePassword": "dataStoreTestQuery",
#                 "dataStoreTestQuery": "SET NOCOUNT ON;select test='test';",
#                 "dataStoreLogFile": "/usr/local/tomcat/logs/datastore.log",
#                 "dataStoreInitConns": 10,
#                 "dataStoreMaxConns": 100,
#                 "dataStoreConnUsageLimit": 100,
#                 "dataStoreLogLevel": "debug",
#                 "maxUrlLength": 500}},
#         {
#             "servlet-name": "cofaxEmail",
#             "servlet-class": "org.cofax.cds.EmailServlet",
#             "init-param": {
#                 "mailHost": "mail1",
#                 "mailHostOverride": "mail2"}},
#         {
#             "servlet-name": "cofaxAdmin",
#             "servlet-class": "org.cofax.cds.AdminServlet"},
#
#         {
#             "servlet-name": "fileServlet",
#             "servlet-class": "org.cofax.cds.FileServlet"},
#         {
#             "servlet-name": "cofaxTools",
#             "servlet-class": "org.cofax.cms.CofaxToolsServlet",
#             "init-param": {
#                 "templatePath": "toolstemplates/",
#                 "log": 1,
#                 "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",
#                 "logMaxSize": "",
#                 "dataLog": 1,
#                 "dataLogLocation": "/usr/local/tomcat/logs/dataLog.log",
#                 "dataLogMaxSize": "",
#                 "removePageCache": "/content/admin/remove?cache=pages&id=",
#                 "removeTemplateCache": "/content/admin/remove?cache=templates&id=",
#                 "fileTransferFolder": "/usr/local/tomcat/webapps/content/fileTransferFolder",
#                 "lookInContext": 1,
#                 "adminGroupID": 4,
#                 "betaServer": True}}],
#     "servlet-mapping": {
#         "cofaxCDS": "/",
#         "cofaxEmail": "/cofaxutil/aemail/*",
#         "cofaxAdmin": "/admin/*",
#         "fileServlet": "/static/*",
#         "cofaxTools": "/tools/*"},
#
#     "taglib": {
#         "taglib-uri": "cofax.tld",
#         "taglib-location": "/WEB-INF/tlds/cofax.tld"}}}
#
# print(data['web-app']['servlet'][4]['init-param'].get('dataLogLocation'))



# data = {
#     'name': 'ulan',
#     'surname': 'temirbekov',
#     'name': 'dima'
# }
#
# print(data)
#
# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {2: 'c'}
# dict_1.update(dict_2)
# print(dict_1)




# data = [
#     {
#         'name': 'ulan',
#         'email': 'ulan@mail.ru'
#     },
#     {
#         'name': 'dima',
#         'email': 'dima@mail.ru'
#     },
#     {
#         'name': 'amna',
#         'email': 'amna@mail.ru'
#     }
#
# ]

# d = {}
# t = ('key1', 'key2', 'key3')
# value = 'value'
#
# my_dictionary = {}.fromkeys(t, value)
# print(my_dictionary)


# car = {'brand': 'dodge',
#        'model': 'charger',
#        'year': '1969'}
#
# # print(car.get('model'))
#
# b = car.setdefault('volume', '100')
#
# print(b)
# print(car)

#
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600 }
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

# d = {
#     'a': 20,
#     'b': 30,
#     'c': 2
# }
#
# result = 1

#
# values = list(d.values())
# for value in values:
#     result *= value


# for value in d:
#     result  = result * d.get(value)
#
# print(result)









# l1 = ['a', 'b', 'c', 'd']
# l2 = [1, 2, 3, 4]
#
# zip_iteraptor = zip(l1, l2)
# a_dictionary = dict(zip_iteraptor)

# print(zip_iteraptor)
# print(a_dictionary)




# d = {'a': 1, "b": 2, 'c': 3}
# dv = list(d.values())
#
# print(dv)
# print(len(dv))
# print(sum(dv))
# print(sum(dv) / len(dv))
# print(min(dv))
# print(max(dv))

# data = {
#     'name': 'dima'
# }
#
#
#
# print(data.get('name'))

# for key, value in data.items():
#     print(f'this is a key {key} and this is a value {value}')

# user_input = (input())
#dictionary
#loops
#for
#concatenation
#formatting
# data = {
#     '1': '9',
#     '2': '8',
#     '3': '7',
#     '4': '6',
#     '5': '0',
#     '6': '4',
#     '7': '3',
#     '8': '2',
#     '9': '1',
#     '0': '5'
# }

# print(a.translate(str.maketrans(incode)))

print(user_input)
for i in user_input:
    print(data.get(i, i), end='')

print(1 ** 2)

