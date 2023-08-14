
def compute_lps(pattern):
    length = 0
    lps = [0] * len(pattern)
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    i = 0
    j = 0
    lineNumber = 1
    charCount = 0
    lps = compute_lps(pattern)
    positionList = []
    while i < len(text):
        if text[i] == '\n':
            lineNumber += 1
            charCount = i + 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == len(pattern):
                positionList.append([lineNumber, i - (j + charCount)])
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positionList


def backslash_kmp_search(text, pattern):
    newPattern = ""
    for i in pattern:
        if i != '\\':
            newPattern += i

    return kmp_search(text, newPattern)


def dot_kmp_search(text, pattern):
    i = 0
    j = 0
    lineNumber = 1
    charCount = 0
    lps = compute_lps(pattern)
    positionList = []
    while i < len(text):
        if text[i] == '\n':
            lineNumber += 1
            charCount = i + 1
        if pattern[j] == text[i] or pattern[j] == '.':
            i += 1
            j += 1
            if j == len(pattern):
                positionList.append([lineNumber, i - (j + charCount)])
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positionList


def question_kmp_search(text, pattern):
    ptr1 = ""
    ptr2 = ""
    for i in pattern:
        if i != '?':
            ptr1 += i
            ptr2 += i
        else:
            ptr2 = ptr2[:-1]

    positionList = kmp_search(text, ptr1)
    for i in kmp_search(text, ptr2):
        if i not in positionList:
            positionList.append(i)

    sortedPositionList = sorted(positionList, key=lambda x: (x[0], x[1]))

    return sortedPositionList


def startwith_kmp_search(text, pattern):
    pattern = pattern[1:]
    i = 0
    j = 0
    lineNumber = 1
    charCount = 0
    lps = compute_lps(pattern)
    positionList = []
    condition = True
    while i < len(text):
        if text[i] == '\n':
            lineNumber += 1
            charCount = i + 1
        if i - charCount == 0 or text[i - 1] == ' ':
            condition = True
        if condition:
            if pattern[j] == text[i]:
                i += 1
                j += 1
                if j == len(pattern):
                    positionList.append([lineNumber, i - (j + charCount)])
                    j = lps[j - 1]
                    condition = False
            else:
                condition = False
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        else:
            i += 1

    return positionList


def endwith_kmp_search(text, pattern):
    pattern = pattern[:-1]
    text += '\0'
    i = 0
    j = 0
    k = 0
    lineNumber = 1
    charCount = 0
    lps = compute_lps(pattern)
    positionList = []
    sign = [' ', '\n', '\0']
    while i < len(text):
        if text[i] == '\n':
            lineNumber += 1
            charCount = i + 1
        if text[i] in sign:
            k = i + 1 - (j + charCount)
        if j != len(pattern):
            if pattern[j] == text[i]:
                i += 1
                j += 1
                if j == len(pattern) and not text[i].isalpha():
                    positionList.append([lineNumber, k])
                    j = lps[j - 1]
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positionList
