import wordcloud
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os

font_path = r'C:\Windows\Fonts\FZSTK.TTF'
img = Image.open('test.png')
img_array = np.array(img)
text = open('test.txt','r').read()

w = wordcloud.WordCloud(background_color="white", width=800, height=600, font_path=font_path, mask=img_array,)
w.generate(text) # 框架自动分词 然后处理
# w.generate_from_frequencies({}) # 根据给定关键词和词频进行处理
# w.generate_from_text('')# 根据切好的词来绘制词云图，自动提取关键词
plt.imshow(w)
plt.axis('off')
plt.show()  #显示图片

if not os.path.exists('cache'):
    os.mkdir('cache')
w.to_file('cache/test.png')  # 保存图片
