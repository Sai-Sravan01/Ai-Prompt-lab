Role=input("Enter your Role:")
Context=input("Enter about you:")
Task=input("What you want:")
Output_Format=input("Format(like 5 sharp points):")
Example=input("Enter if there is any example/skip:")

prompt="Role:"+Role+".\n"
prompt=prompt+"Context:"+Context+ "\n"
prompt=prompt+"Task:"+ Task +"\n"
prompt=prompt+"Format:"+Output_Format+"\n"

if Example!="":
    prompt=prompt+"Example"+Example+"\n"

print("\n-----YOUR PROMPT IS------")
print(prompt)