# GitHub Pages 部署指南

## 方法一：直接使用GitHub Pages

### 1. 创建GitHub仓库

访问 [GitHub](https://github.com) 并创建新仓库：

- 如果想使用 `username.github.io` 格式，仓库名必须是 `username.github.io`（替换username为你的用户名）
- 如果使用其他名称，比如 `bible-reading`，访问地址将是 `username.github.io/bible-reading`

### 2. 上传文件

有两种方式上传文件：

#### 方式A: 使用Git命令行

```bash
# 初始化Git仓库
cd bible-reading-plan
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: 两年读经计划"

# 关联远程仓库（替换YOUR-USERNAME和REPO-NAME）
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

#### 方式B: 使用GitHub网页上传

1. 在GitHub仓库页面，点击 "Add file" → "Upload files"
2. 拖拽或选择所有文件上传
3. 填写提交信息，点击 "Commit changes"

### 3. 启用GitHub Pages

1. 进入仓库的 **Settings**（设置）
2. 在左侧菜单找到 **Pages**
3. 在 "Source" 下选择：
   - Branch: `main` (或 `master`)
   - Folder: `/ (root)`
4. 点击 **Save**
5. 等待几分钟，页面会显示网站地址

### 4. 配置_config.yml

根据你的仓库名修改 `_config.yml`：

```yaml
# 如果仓库名是 username.github.io
baseurl: ""
url: "https://username.github.io"

# 如果仓库名是其他名称，比如 bible-reading
baseurl: "/bible-reading"
url: "https://username.github.io"
```

修改后需要重新提交：

```bash
git add _config.yml
git commit -m "Update baseurl"
git push
```

## 方法二：使用GitHub Actions自动部署

创建 `.github/workflows/jekyll.yml`：

```yaml
name: Deploy Jekyll site to Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'
          bundler-cache: true
      - name: Setup Pages
        uses: actions/configure-pages@v4
      - name: Build with Jekyll
        run: bundle exec jekyll build --baseurl "${{ steps.pages.outputs.base_path }}"
        env:
          JEKYLL_ENV: production
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

然后在Settings → Pages中将Source改为"GitHub Actions"。

## 添加内容

### 1. 批量生成读经文件模板

```bash
python generate_readings.py
```

这会在 `_daily_readings/` 目录生成730个文件模板。

### 2. 查看建议的读经计划

```bash
python generate_readings.py plan
```

### 3. 填充经文内容

编辑 `_daily_readings/day-XXX.md` 文件，添加实际的圣经经文。

### 4. 添加读经分享

在 `_reflections/` 目录创建新文件，参考示例格式。

## 本地测试

在推送到GitHub之前，建议先本地测试：

```bash
# 安装依赖
bundle install

# 运行Jekyll服务器
bundle exec jekyll serve

# 访问 http://localhost:4000
```

## 常见问题

### Q: 页面显示404

**A**: 检查以下几点：
- GitHub Pages是否已启用
- `_config.yml` 中的 `baseurl` 是否正确
- 文件是否正确上传到仓库
- 等待几分钟让GitHub处理

### Q: 样式没有加载

**A**: 
- 确认 `_config.yml` 中的 `baseurl` 设置正确
- 检查 `_layouts/default.html` 中CSS引用路径
- 清除浏览器缓存

### Q: 如何更新内容

**A**: 
```bash
# 修改文件后
git add .
git commit -m "Update readings"
git push
```

GitHub会自动重新构建和部署。

### Q: 如何添加自定义域名

**A**: 
1. 在DNS设置中添加CNAME记录指向 `username.github.io`
2. 在仓库根目录创建 `CNAME` 文件，内容为你的域名
3. 在Settings → Pages中设置Custom domain

## 性能优化

### 启用压缩

在 `_config.yml` 添加：

```yaml
sass:
  style: compressed
```

### 添加缓存

创建 `_includes/head.html` 添加缓存控制头。

### 使用CDN

将静态资源（CSS、图片）托管到CDN可以加快加载速度。

## 维护建议

1. **定期备份**: 定期导出内容到本地
2. **版本控制**: 使用Git标签标记重要版本
3. **内容审核**: 定期检查和更新读经分享
4. **用户反馈**: 添加反馈机制收集改进意见

## 进阶功能

### 添加统计

使用Google Analytics或其他统计工具跟踪访问。

### 添加搜索

集成Jekyll Simple Search或Algolia。

### 添加RSS订阅

启用 `jekyll-feed` 插件提供RSS订阅。

### 移动应用

可以使用React Native或Flutter将网站包装成移动应用。

## 需要帮助？

- [Jekyll官方文档](https://jekyllrb.com/docs/)
- [GitHub Pages文档](https://docs.github.com/en/pages)
- 提交Issue到项目仓库

---

祝部署顺利！愿神祝福这个读经计划项目！
