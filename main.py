a = input("加密请输入1，解密请输入2:")
n = input("请输入偏移位数(1~25)（默认为3）：")
if n == '':
    n = 3
else:
    n = int(n)
if a == '1':
    code = input("请输入加密的句子：")
    print("加密后的句子为：", end='')
    for word in code:
            x = ord(word)
            if 'a' <= word <= 'z':
                b = ord('z') - x
                if b < n:
                    y = x + n - 26
                else:
                    y = x + n
                after = chr(y)
            elif 'A' <= word <= 'Z':
                b = ord('Z') - x
                if b < n:
                    y = x + n - 26
                else:
                    y = x + n
                after = chr(y)
            elif '0' <= word <= '9':
                c = int(word)
                while n > 9:
                    n -= 10
                b = 9 - c
                if b < n:
                    after = c + n - 10
                else:
                    after = c + n
            else:
                after = word
            print(after, end='')
if a == '2':
    code = input("请输入解密的句子：")
    print("解密后的句子为：",  end='')
    for word in code:
            x = ord(word)
            if 'a' <= word <= 'z':
                b = x - ord('a')
                if b < n:
                    y = x - n + 26
                else:
                    y = x - n
                after = chr(y)
            elif 'A' <= word <= 'Z':
                b = x - ord('A')
                if b < n:
                    y = x - n + 26
                else:
                    y = x - n
                after = chr(y)
            elif '0' <= word <= '9':
                while n > 10:
                    n -= 10
                b = int(word)
                if b < n:
                    after = b - n + 10
                else:
                    after = b - n
            else:
                after = word
            print(after, end='')






