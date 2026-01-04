---
layout: default
title: About
---

# About {{ site.title }}

{{ site.description }}

## What is This?

This is a minimal GitHub Pages site that demonstrates:

1. **Automatic Jekyll processing** - No local build needed
2. **Liquid templating** - Dynamic content generation
3. **Markdown simplicity** - Easy content creation
4. **Theme support** - Using {{ site.theme }}

## Liquid in Action

### Site Variables
- **Site Title:** {{ site.title }}
- **Description:** {{ site.description }}
- **Theme:** {{ site.theme }}
- **Total Posts:** {{ site.posts | size }}

### Date Formatting
- **Full Date:** {{ site.time | date: "%A, %B %d, %Y" }}
- **Short Date:** {{ site.time | date: "%m/%d/%Y" }}
- **Time:** {{ site.time | date: "%H:%M:%S" }}

### String Manipulation
{% assign example = "github pages" %}
- Original: {{ example }}
- Uppercase: {{ example | upcase }}
- Capitalize: {{ example | capitalize }}
- Replace: {{ example | replace: "pages", "actions" }}

### Arrays and Loops
{% assign numbers = "1,2,3,4,5" | split: "," %}
{% for num in numbers %}
- Number {{ num }}
{% endfor %}

## How to Add Content

### Add a New Page
Create `newpage.md`:
```markdown
---
layout: default
title: New Page
---

# Your content here
```

### Add a Blog Post
Create `_posts/YYYY-MM-DD-title.md`:
```markdown
---
layout: default
title: "My Post"
date: 2024-01-26
---

Your post content...
```

## Learn More

- [Jekyll Documentation](https://jekyllrb.com/)
- [Liquid Documentation](https://shopify.github.io/liquid/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)
