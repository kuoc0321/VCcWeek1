'''
Cho một chuỗi s và một từ điển dict. Hãy viết một phương thức add các khoảng trắng vào chuỗi s
sao cho thành các câu có thể.
	Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
'''

def word_break(s,wordDict):
    def backtracking(start, memory):
        if start in memory:
            return memory[start]
        if start == len(s):
            return ['']
        res = []
        for word in wordDict:
            if s[start:].startswith(word):
                temps = backtracking(start + len(word) , memory)
                for temp in temps:
                    if temp:
                        res.append(word + " " + temp)
                    else:
                        res.append(word)

        memory[start] = res
        return res

    return backtracking(0, {})

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
results = word_break(s, wordDict)
print(results)