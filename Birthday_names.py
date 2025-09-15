name_list=[]
with open('F:/Python/Names.txt','r') as names:
    name=names.readlines()
for i in name:
    char_2=i.split(" ")[1]
    char_2=char_2.replace('\n','')
    name_list.append(char_2)


with open('F:/Python/Birthday_template.txt','r') as birthday_inv:
    st=birthday_inv.read()

for i in name_list:
    with open(f"F:/Python/Birthday/Birthday_invitation_{i}.txt",'w') as birthday_out:
        st1=st.replace('Name',i)
        birthday_out.write(st1)
