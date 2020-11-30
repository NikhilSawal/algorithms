def reorderLogFiles(logs):
    dig_list = []
    let_list = []
    output = [0 for i in range(len(logs))]
    for index, log in enumerate(logs):
        try:
            if isinstance(int(log[log.find(' ')+1]), int):
                dig_list.append(log)
        except ValueError:
            let_list.append(log)

    for i in range(len(let_list)-1):
        for j in range(0, len(let_list)-i-1):
            if let_list[j][let_list[j].find(" "): ] > let_list[j+1][let_list[j+1].find(" "): ]:
                let_list[j], let_list[j+1] = let_list[j+1], let_list[j]

    return let_list + dig_list

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(reorderLogFiles(logs))

logs = ["j je", "b fjt", "7 zbr", "m le", "o 33"]
print(reorderLogFiles(logs))

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
print(reorderLogFiles(logs))

print("le" < "zbr")
