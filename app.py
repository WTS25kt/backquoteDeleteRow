
def remove_lines_with_triple_backticks(file_path):
    # ファイルを読み込み、行ごとに処理する
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # バッククォート3つを含む行を除外
    filtered_lines = [line for line in lines if '```' not in line]
    
    # 結果をファイルに書き込む
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(filtered_lines)

# 使用例
remove_lines_with_triple_backticks('example.txt')

