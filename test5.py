def printList(dic):
    for key in dic.keys():
        print('{:15} : {}'.format(key, dic[key]))

# 파일 -> 딕셔너리
file = 'd:\javaedu10\project\python\dictionary.txt'
def load_dic(file):
    dic = {}
    with open(file,'r',encoding='UTF8') as f :
        for line in f:
            word, meaning = line.strip().split(":")
            dic[word] = meaning
    return dic

# 딕셔너리 -> 파일
def save_dic(file, dic):
    with open(file, "w", encoding="utf-8") as f:
        for word, meaning in dic.items():
            f.write(f"{word}:{meaning}\n")

#저장
def add_word(dic):
    if len(dic) >= 5 :
        print("최대 5개 단어만 저장 할 수 있습니다.")
        return
    word = input("단어를 입력하세요: ")
    if word in dic:
        print("이미 등록된 단어입니다.")
    else:
        meaning = input("뜻을 입력하세요: ")
        dic[word] = meaning
        with open(file, "a", encoding="utf-8") as f:
            f.write(f"{word}:{meaning}\n")
        print("저장되었습니다.")

#검색
def search_word(dic):
    keyword = input("검색할 단어를 입력하세요: ")
    results = []
    for word, meaning in dic.items():
        if word.lower().startswith(keyword.lower()):
            results.append((word, meaning))
    if results:
        for word, meaning in results:
            print(f"{word}: {meaning}")
    else:
        print(f"'{keyword}'단어를 검색할 수 없습니다.")
 
#수정
def modify_word(dic):
    word = input("수정할 단어를 입력하세요: ")
    if word.lower() in dic:
        meaning = input("수정할 뜻을 입력하세요: ")
        dic[word.lower()] = meaning
        with open(file, "w", encoding="utf-8") as f:
            for word, meaning in dic.items():
                f.write(f"{word}:{meaning}\n")
        print("단어의 뜻을 수정하였습니다.")
    else:
        print("단어를 검색할 수 없습니다.")
    
#삭제
def delete_word(dic):
    word = input("삭제할 단어를 입력하세요: ")
    if word.lower() in dic:
        del dic[word.lower()]
        with open(file, "w", encoding="utf-8") as f:
            for word, meaning in dic.items():
                f.write(f"{word}:{meaning}\n")
        print("단어를 삭제하였습니다.")
    else:
        print("단어를 검색할 수 없습니다.")
    
#목록
def list_words(dic):
    print("단어장 목록입니다.")
    while True :
        print("정렬순서를 선택하세요: 1.오름차순 2.내림차순")
        sort_choice = input("선택 : ")
        if sort_choice == "1" :
            sorted_words = sorted(dic.items())
            break
        elif sort_choice == "2" :
            sorted_words = sorted(dic.items(), reverse=True)
            break
        else :
            print("정렬 방식을 다시 선택해주세요.")
    for word, meaning in sorted_words :
        print(f"{word}: {meaning}")

#통계
def statistic_words(dic):
    print("단어장 통계 입니다.")
    print("1.저장된 단어 갯수 : {} 개".format(len(dic)))

    longest_word = max(dic.keys(), key=len)
    print("2.단어의 문자수가 가장 많은 단어: {}".format(longest_word, len(longest_word)))

    import operator
    reversedDictionary = sorted(dic.items(), key=operator.itemgetter(0), reverse=True)
    # print(reversedDictionary)
    print("3.단어 글자수 내림차순 출력(단어만)")
    for entry in reversedDictionary :
      print('{:15} : {}'.format(entry[0], entry[1]))

#종료
stop = True

file = 'dictionary.txt'

def main():
    dic = load_dic(file)
    while True:
        print("""1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료""")
        choice = input("선택: ")
        if choice == "1":
            add_word(dic)
        elif choice == "2":
            search_word(dic)
        elif choice == "3":
            modify_word(dic)
        elif choice == "4":
            delete_word(dic)
        elif choice == "5":
            list_words(dic)
        elif choice == "6":
            statistic_words(dic)
        elif choice == "7":
            print("<<영어 단어장 종료>>")
            break
        else:
            print("올바른 값을 입력하세요.")

if __name__ == "__main__":
    main()
