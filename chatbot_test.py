import chatbot

output = str(input("오피스 챗봇입니다. 무엇을 도와드릴까요?:"))
while(output != "그만"):
    output = chatbot.predict(output)
    output = str(input("오피스 챗봇입니다. 무엇을 도와드릴까요?:"))

