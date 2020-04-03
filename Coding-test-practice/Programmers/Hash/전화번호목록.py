def solution(phone_book):
    phone_book.sort()
    length = len(phone_book)

    for i in range(length):
        pi = phone_book[i]
        for j in range(i + 1, length):
            pj = phone_book[j]
            if pi in pj:
                return False
    return True
