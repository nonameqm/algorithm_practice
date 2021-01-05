# 회문 판단하기 (palindrome) by recursive
def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False


genetic_string = 'ATGTAATGGTTGCAGTCAATTGATGTCGTGCTCGAGCTGCAGCTAGCGATCGAGGTTCCAGCGTAGCGTAGCGCGGTACGTCA'
# 회문의 길이가 정해져 있음 - 특정 물질을 만드는데 필요한 염기서열의 길이가 정해져 있음


# 예상
# Q1: 6글자로 이루어진 회문을 찾아라 (위 string의 경우 1가지가 나옴)
print('----------Q1----------')
LEN = 6
for i in range(len(genetic_string)-LEN):
    if palindrome(genetic_string[i:i+LEN]):
        print(genetic_string[i:i+LEN])


# Q2: 5글자로 이루어진 회문을 모두 찾아라 (위 string의 경우 6가지가 나옴)
print('----------Q2----------')
LEN = 5
for i in range(len(genetic_string)-LEN):
    if palindrome(genetic_string[i:i+LEN]):
        print(genetic_string[i:i+LEN])


# Q3: 염기서열 중 회문들 사이에 있는 염기 서열을 모두 출력하라 (이 때 string의 길이는 5글자라고 가정)
print('----------Q3----------')
LEN = 5
index_result = []
for i in range(len(genetic_string)-LEN):
    if palindrome(genetic_string[i:i+LEN]):
        index_result.append(i)

result = []
for i in range(len(index_result)):
    if i+1 < len(index_result):
        string = genetic_string[index_result[i]+LEN:index_result[i+1]]
        if string != '':
            result.append(string)
print(result)
