# Vocaloid Music Data Site

本项目为 [程序设计训练（Python）2025夏](https://keg-course.github.io/python-docs/crawler/) 课程第一次大作业。

本项目基于 Django 框架，结合 Selenium 爬虫，收集并展示了网易云音乐上 2045 首 Vocaloid 相关歌曲和 545 位艺术家的详细信息。

## 项目简介

- 使用 Selenium 自动化爬取网易云音乐的歌曲与艺术家数据。
- 数据包括：
    - 歌曲：歌曲名、歌词、封面图片、艺术家、原始链接；
    - 艺术家：名称、图片、简介、原始链接。
- 网站前端采用 Bootstrap 美化，支持歌曲、艺术家浏览与搜索，支持评论与分页。

## 主要功能

- 歌曲列表与详情页，支持歌词、网易云播放器嵌入、评论功能。
- 艺术家列表与详情页，支持合作词云展示。
- 搜索功能：可按歌曲或艺术家关键词检索。
- 评论系统：支持对每首歌添加和删除评论。

## 技术栈

- 后端：Django 5.2.3
- 前端：Bootstrap 5 + MDB UI Kit
- 数据采集：Selenium
- 数据存储：SQLite3

## 目录结构

```
├── data/                # 爬取的原始数据与图片
├── data-analysis/       # 数据分析脚本
├── data-aquisition/     # 爬虫脚本
├── website/             # Django 项目主目录
│   ├── music/           # Django app，主要逻辑
│   └── media/           # 上传/生成的媒体文件
```

## 数据说明

- 歌曲数据量：2045 首
- 艺术家数据量：545 位
- 数据来源：网易云音乐网页版公开内容，曲目来自以下歌单：
    - 2562363367 [Vocaloid神话曲及准神话曲](https://music.163.com/#/playlist?id=2562363367)
    - 73246647 [周刊VOCALOID排行榜](https://music.163.com/#/playlist?id=73246647)
    - 90483498 [独家珍藏的vocaloid歌单！！](https://music.163.com/#/playlist?id=90483498)
    - 12556191058 [VOCALOID传说曲](https://music.163.com/#/playlist?id=12556191058)

## 数据分析

1. 分 p 主和虚拟歌姬分别统计歌曲数量的排名。
1. 分析 Vocaloid 歌曲的发布时间特征。
1. 展示 p 主与歌姬之间合作歌曲数目的统计。

## 免责声明

本项目仅用于技术交流与学习，数据版权归网易云音乐及相关作者所有。

---
如有建议或问题，欢迎 issue 或 PR！

