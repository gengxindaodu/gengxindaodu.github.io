---
layout: default
title: "Liquid Filters Cheat Sheet"
date: 2026-01-04
---

# {{ page.title }}

**Published:** {{ page.date | date: "%B %d, %Y" }}

Quick reference for common Liquid filters you'll use all the time.

## String Filters

| Filter | Input | Output |
|--------|-------|--------|
| `upcase` | {{ "{{ 'hello' | upcase " }}}} | {{ 'hello' | upcase }} |
| `downcase` | {{ "{{ 'HELLO' | downcase " }}}} | {{ 'HELLO' | downcase }} |
| `capitalize` | {{ "{{ 'hello world' | capitalize " }}}} | {{ 'hello world' | capitalize }} |
| `strip` | {{ "{{ '  hello  ' | strip " }}}} | "{{ '  hello  ' | strip }}" |
| `truncate` | {{ "{{ 'hello world' | truncate: 8 " }}}} | {{ 'hello world' | truncate: 8 }} |
| `replace` | {{ "{{ 'hello' | replace: 'he', 'je' " }}}} | {{ 'hello' | replace: 'he', 'je' }} |
| `append` | {{ "{{ 'hello' | append: ' world' " }}}} | {{ 'hello' | append: ' world' }} |
| `prepend` | {{ "{{ 'world' | prepend: 'hello ' " }}}} | {{ 'world' | prepend: 'hello ' }} |

## Array Filters

{% assign colors = "red,blue,green,yellow" | split: "," %}

**Array:** {{ colors | join: ", " }}

| Filter | Example | Output |
|--------|---------|--------|
| `size` | {{ "{{ colors | size " }}}} | {{ colors | size }} |
| `first` | {{ "{{ colors | first " }}}} | {{ colors | first }} |
| `last` | {{ "{{ colors | last " }}}} | {{ colors | last }} |
| `join` | {{ "{{ colors | join: ' & ' " }}}} | {{ colors | join: ' & ' }} |
| `sort` | {{ "{{ colors | sort | join: ', ' " }}}} | {{ colors | sort | join: ', ' }} |
| `reverse` | {{ "{{ colors | reverse | join: ', ' " }}}} | {{ colors | reverse | join: ', ' }} |

## Math Filters

| Filter | Example | Result |
|--------|---------|--------|
| `plus` | {{ "{{ 5 | plus: 3 " }}}} | {{ 5 | plus: 3 }} |
| `minus` | {{ "{{ 10 | minus: 3 " }}}} | {{ 10 | minus: 3 }} |
| `times` | {{ "{{ 5 | times: 3 " }}}} | {{ 5 | times: 3 }} |
| `divided_by` | {{ "{{ 10 | divided_by: 2 " }}}} | {{ 10 | divided_by: 2 }} |
| `modulo` | {{ "{{ 10 | modulo: 3 " }}}} | {{ 10 | modulo: 3 }} |
| `abs` | {{ "{{ -5 | abs " }}}} | {{ -5 | abs }} |

## Date Filters

**Today's date in different formats:**

| Format | Code | Output |
|--------|------|--------|
| Full | `{{ "{{ 'now' | date: '%B %d, %Y' " }}}}` | {{ 'now' | date: '%B %d, %Y' }} |
| Short | `{{ "{{ 'now' | date: '%m/%d/%y' " }}}}` | {{ 'now' | date: '%m/%d/%y' }} |
| Day | `{{ "{{ 'now' | date: '%A' " }}}}` | {{ 'now' | date: '%A' }} |
| Time | `{{ "{{ 'now' | date: '%H:%M' " }}}}` | {{ 'now' | date: '%H:%M' }} |
| ISO | `{{ "{{ 'now' | date: '%Y-%m-%d' " }}}}` | {{ 'now' | date: '%Y-%m-%d' }} |

## Useful Combinations

**Blog post date:**
```liquid
{{ "{{ post.date | date: '%B %d, %Y' " }}}}
```
{{ page.date | date: '%B %d, %Y' }}

**Truncated excerpt:**
```liquid
{{ "{{ post.content | strip_html | truncatewords: 30 " }}}}
```

**URL-safe title:**
```liquid
{{ "{{ page.title | slugify " }}}}
```
{{ page.title | slugify }}

## Chaining Filters

You can chain multiple filters together:

```liquid
{{ "{{ '  hello world  ' | strip | upcase | append: '!' " }}}}
```
Result: {{ '  hello world  ' | strip | upcase | append: '!' }}

---

Keep this page handy when working with Liquid!
