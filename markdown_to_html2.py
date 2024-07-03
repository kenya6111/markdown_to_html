import markdown
import os
import sys

def convert_to_html(input_path, output_path):
    # 指定ファイルの読み込み
    with open(input_path, 'r') as f:
        content = f.read()
    
    md = markdown.Markdown()
    converted_content = md.convert(content)

    with open(output_path, 'w') as f:
        f.write(converted_content)

def main():
    # コマンド引数取得
    command = sys.argv[1]
    print("いえい")

    if command =='markdown':
        # コマンド引数チェック
        if len(sys.argv) != 4:
            print("Usage: markdown <inputpath>.txt <outputpath>.html")
            return        
        # 引数取得
        print("いえい2")
        input_path = sys.argv[2]
        print(input_path)
        output_path = sys.argv[3]
        print(output_path)
        convert_to_html(input_path, output_path)

if __name__ == "__main__":
    main()


#入力コマンド例
# python3 markdown_to_html2.py markdown  /home/kenya/recursion/python_practice/markdown_to_html/test.txt /home/kenya/recursion/python_practice/markdown_to_html/converted_files/d.html