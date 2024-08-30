# 项目介绍

该项目是通过scrapy库的功能来爬取一些游戏资讯。

目前已经实现的功能包括：

​1. 爬取游民星空的游戏资讯。

...


后续更新或许会加入其他游戏网站资讯的爬虫。

# 使用说明

## 安装scrapy库

```bash
pip install scrapy
```

---

## 运行

```bash
scrapy crawl youmin
```

---
## 数据生成

默认数据名为news.json

可在game_news中的settings.py更改JSON_FILE_NAME选项来更换保存的文件名

---

# 特别感谢

**本项目使用了游民星空的资讯数据作为演示，特此向游民星空表示诚挚的感谢。如有侵权，请您尽快告知，我们会立即删除相关内容。**

# 意见反馈

如有疑问联系XLD_Hero@outlook.com
