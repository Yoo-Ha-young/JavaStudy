str = input()
for st in str:
    if st.islower() == True:
        print(st.upper(), end='')
    elif st.isupper() == True:
        print(st.lower(), end='')
