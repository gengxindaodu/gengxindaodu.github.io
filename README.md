# 两年读经计划 GitHub Pages

这是一个基于Jekyll的两年读经计划网站，帮助您系统地在730天内完整阅读整本圣经。

## 功能特点

- 📖 **730天完整读经计划**：系统覆盖圣经66卷书
- 📅 **日历视图**：方便查看和导航每日读经内容
- 💭 **读经分享**：每天配有多篇读经分享，帮助理解和应用
- 🔗 **便捷导航**：前后天导航链接，轻松切换
- 📚 **书卷浏览**：按圣经书卷分类浏览
- 📱 **响应式设计**：适配各种设备

## 项目结构

```
bible-reading-plan/
├── _config.yml              # Jekyll配置文件
├── _layouts/                # 页面布局模板
│   ├── default.html         # 默认布局
│   ├── reading.html         # 读经页面布局
│   └── reflection.html      # 分享页面布局
├── _daily_readings/         # 每日读经内容
│   ├── day-001.md
│   ├── day-002.md
│   └── ...
├── _reflections/            # 读经分享
│   ├── 001-creation.md
│   ├── 002-fall.md
│   └── ...
├── books/                   # 圣经书卷内容（按文件夹组织）
│   ├── gen/                 # 创世记
│   ├── exo/                 # 出埃及记
│   └── ...
├── assets/
│   └── css/
│       └── style.css        # 样式文件
├── index.html               # 首页
├── calendar.html            # 日历页面
├── books.html               # 书卷浏览页面
└── about.html               # 关于页面
```

## 快速开始

### 1. 克隆或下载本项目

### 2. 配置_config.yml

修改`_config.yml`中的基本信息：

```yaml
title: 两年读经计划
description: 730天完整读完圣经
baseurl: ""  # 如果repo名不是 username.github.io，改为 "/repo-name"
url: "https://yourusername.github.io"  # 你的GitHub Pages URL
```

### 3. 添加内容

#### 添加每日读经内容

在`_daily_readings/`文件夹中创建文件，命名格式为`day-XXX.md`：

```markdown
---
day: 1
passage: "创世记 1-2章"
date: 2024-01-01
reflections: ["001-creation"]
---

## 创世记 1章

[经文内容]

## 创世记 2章

[经文内容]
```

#### 添加读经分享

在`_reflections/`文件夹中创建文件：

```markdown
---
reflection_id: "001-creation"
title: "神的创造彰显祂的大能"
author: "作者姓名"
date: 2024-01-01
passage: "创世记 1-2章"
related_day: 1
---

[分享内容]
```

### 4. 组织圣经书卷内容

在`books/`文件夹中为每卷书创建子文件夹，例如：

```
books/
├── gen/       # 创世记
│   ├── index.md
│   └── chapters/
├── exo/       # 出埃及记
│   ├── index.md
│   └── chapters/
└── ...
```

### 5. 部署到GitHub Pages

1. 创建GitHub仓库
2. 将代码推送到仓库
3. 在仓库设置中启用GitHub Pages
4. 选择分支（通常是main或master）
5. 访问 `https://yourusername.github.io/repo-name`

## 本地测试

如果您想在本地测试网站：

```bash
# 安装Jekyll
gem install jekyll bundler

# 安装依赖
bundle install

# 运行本地服务器
bundle exec jekyll serve

# 访问 http://localhost:4000
```

## 内容获取建议

### 圣经经文

- 使用公有版权的和合本圣经
- 可以从以下来源获取：
  - [Bible API](https://scripture.api.bible/)
  - [YouVersion API](https://www.bible.com/api)
  - 其他开放的圣经数据源

### 读经分享

- 邀请教会弟兄姊妹贡献
- 参考经典注释书籍（注意版权）
- 从讲道分享中整理（需获得授权）

## 自定义样式

修改`assets/css/style.css`来自定义网站外观：

- 颜色主题
- 字体样式
- 布局调整
- 响应式断点

## 高级功能

### 添加搜索功能

可以集成Jekyll Search或Algolia搜索。

### 添加评论功能

可以集成Disqus、Gitalk等评论系统。

### 添加进度跟踪

使用LocalStorage或后端服务跟踪用户的阅读进度。

## 贡献

欢迎贡献！您可以：

- 添加读经分享
- 改进页面设计
- 修复bug
- 提出新功能建议

## 许可证

本项目采用MIT许可证。圣经经文内容遵循其各自的版权声明。

## 联系方式

如有问题或建议，请：
- 提交GitHub Issue
- 发送Pull Request
- 联系项目维护者

## 致谢

感谢所有贡献读经分享的弟兄姊妹，愿神祝福你们！

---

**愿神的话语成为我们脚前的灯，路上的光！**
