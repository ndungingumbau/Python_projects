# collect email from user
# slice/split te email using the @, save the first part as the username, thesecond part is gonna be saved as domain
# split domain using .,

def  main():
    print("Welcome to the Email slicer: ")
    print("")

    email_input = input("Input Your Email Address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Usename : ", username)
    print("Domain : ", domain)
    print("Extension : ", extension)
while True:
    main()    