# try:
#     a=int(input("Enter a number: "))
#     print(a)


# except Exception as e:
#     print(e)
# else: 
#     print("Thank you")









def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
   
    finally:
        print("Hey I am inside")

main()
