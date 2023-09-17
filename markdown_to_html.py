import markdown

print("aaaaaa")
text = """
# Hello world1
## Hello world2
### Hello world3
#### Hello world4

水平線
---

**太字

##リスト

- 日本
- アメリカ
- 中国

1. 番号付きリスと1
2. 番号付きリスと2
3. 番号付きリスと3

"""
print(text)

html = markdown.markdown(text)

print(html)