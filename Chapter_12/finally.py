def main():
    try:
        a = int(input("Enter a number : "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally: # finally ka use function mai hi hota hai normal program bina finally ke bhi chal sakta hai...
        print("Hey , I am inside this program ")
main()