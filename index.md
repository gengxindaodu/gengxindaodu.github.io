---
layout: default
title: Home
---

# Welcome to {{ site.title }}

{{ site.description }}

## About This Site

This is a minimal GitHub Pages site using:
- **Jekyll Theme**: Cayman
- **Liquid Templating**: For dynamic content
- **Markdown**: For easy writing

## Recent Posts

{% for item in site.genesis %}
  <a href="{{ item.url }}">{{ item.title }}</a>
{% endfor %}

## Site Stats

- Total Posts: **{{ site.posts | size }}**
- Last Updated: **{{ site.time | date: "%B %d, %Y" }}**

---

### Quick Liquid Examples

**Current date:** {{ "now" | date: "%A, %B %d, %Y" }}

**Uppercase text:** {{ "hello world" | upcase }}

**Math:** {{ 5 | plus: 3 }} equals 8
