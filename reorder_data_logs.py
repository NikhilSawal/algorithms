def reorderLogFiles(logs):
    dig_list = []
    let_list = []
    output = [0 for i in range(len(logs))]
    for index, log in enumerate(logs):
        if log.startswith('dig'):
            dig_list.append(log)
        else:
            let_list.append(log)

    for i in range(len(let_list)-1):
        for j in range(1, len(let_list)):
            if let_list[i][let_list[i].find(" "): ] > let_list[j][let_list[j].find(" "): ]:
                let_list[i], let_list[j] = let_list[j], let_list[i]

    return let_list + dig_list

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))
