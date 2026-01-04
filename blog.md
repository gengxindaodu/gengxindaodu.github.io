---
layout: default
title: Blog
---

# All Blog Posts

{% if site.posts.size == 0 %}
No posts yet. Add your first post in the `_posts` folder!
{% else %}
{% for post in site.posts %}
## [{{ post.title }}]({{ post.url }})

**Published:** {{ post.date | date: "%B %d, %Y" }}

{{ post.excerpt }}

[Read more →]({{ post.url }})

---
{% endfor %}
{% endif %}
