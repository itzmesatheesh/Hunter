def persontop(a):
    if a==0 or a==1:
        return 1
    return persontop(a-1)+persontop(a-2)
def main():
    a=int(input())
    print(persontop(a))

if __name__ == '__main__':
    main()
