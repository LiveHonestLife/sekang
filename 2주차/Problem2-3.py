table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

'job 5 4 3 2 1'
"SI JAVA JAVASCRIPT SQL PYTHON C#"
"CONTENTS JAVASCRIPT JAVA PYTHON SQL C++"
"HARDWARE C C++ PYTHON JAVA JAVASCRIPT"
"PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP"
"GAME C++ C# JAVASCRIPT C JAVA"

def solution(table, languages, preference):
    answer = dict()

    for idx, job in enumerate(table):
        table_split = job.split(" ")
        score = [0] * 6
        for lang, weight in zip(languages, preference):
            if lang in table_split:
                k = table_split.index(lang)
                score[k] = (6-k)*weight
        print(sum(score))
        answer[table_split[0]] = sum(score)
    answer = sorted(answer.items(), key=lambda x: (-x[1], x[0]))
    return answer[0][0]

print(solution(table, languages, preference))
