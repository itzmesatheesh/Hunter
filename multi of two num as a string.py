def main():
    a1,a2=map(str,input().split())
    try:
        mul=int(a1)*int(a2)
        print(str(mul))
    except:
        print('Invalid number string')



if __name__ == '__main__':
    main()
