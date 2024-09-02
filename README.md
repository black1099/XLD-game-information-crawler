# 项目介绍

该项目是通过scrapy库的功能来爬取一些游戏资讯。

目前已经实现的功能包括：

爬取游民星空的游戏资讯。

爬取3DM的游戏资讯。

爬取游侠的游侠资讯。

后续更新或许会加入其他游戏网站资讯的爬虫。


# 使用说明

## 安装scrapy库

```bash
pip install scrapy
```

---

## 运行
### 游民星空
```bash
scrapy crawl youmin
```
### 3DM
```bash
scrapy crawl dm3
```
### 游侠
```bash
scrapy crawl youxia
```
---
## 数据生成

默认数据名为news.json

可在game_news中的settings.py更改JSON_FILE_NAME选项来更换保存的文件名

---

## 已知问题

### 3DM
当短时间内请求次数过多，3dmgame会停止返回游戏资讯，因此，请尝试降低访问速度，减少访问次数，避免让3dm感觉到压力。

---

# 特别感谢

**本项目使用了游民星空，3DM，游侠的资讯数据作为演示，特此向游民星空，3DM，游侠表示诚挚的感谢。如有侵权，请您尽快告知，我们会立即删除相关内容。**

# 意见反馈

如有疑问联系XLD_Hero@outlook.com
