prompts=[]

while True:
    text=input("Enter text(if completed text done):")
    if text=="done":
        break
    prompts.append(text)

    for p in prompts:
        words=len(p.split())
        chars=len(p)
        tokens=chars//4
        print("Prompt Length:","Long" if words>15 else "short")
        print("words:",words)
        print("chars:",chars)
        print("tokens:",tokens)

                      
