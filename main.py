pip install translation
from translation import baidu, google, youdao, iciba

print(google('Hii!', dst = 'zh-CN'))
print(google('hello world!', dst = 'ru'))
print(baidu('Paras here!', dst = 'zh'))
print(baidu('Gods plan always work!', dst = 'ru'))
print(youdao('Virat kohli no.18!', dst = 'zh-CN'))
print(iciba('Hii I m Aman!', dst = 'zh'))
print(bing('Welcome to Dubai!', dst = 'zh-CHS'))