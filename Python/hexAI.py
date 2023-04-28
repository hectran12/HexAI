import requests, json, datetime


class result:
    def __init__ (self, question, result, title, content, date) -> None:
        self.question = question
        self.title = title
        self.result = result
        self.content = content
        self.date = date

class chat:
    def __init__(self) -> None:
        self.title = ''
        self.content = ''

    def req (self, data) -> requests.post:
        return requests.post(
            url='https://tronghoa.dev/api/ai_bot.php',
            data=data 
        )
    
    def ask (self, question, flowchart=True, newChat=False)->result:

        #reset
        if newChat:
            self.title = ''
            self.content = ''
            
        actionAsk = self.req({
            "ask": question,
            "title": self.title,
            "content": self.content
        })

        resultContent = ''
        for character in actionAsk.text.split("\n"):
            if character != "":
                dictCharacter = eval(character)
                resultContent += dictCharacter["completion"]

        if flowchart:
            # title
            for x in resultContent.split("\n"):
                if x != '':
                    if x[0] == '#':
                        self.title = x.replace('# ', '')
                


            # content
            self.content += resultContent


        return result(
            question=question,
            result=resultContent,
            title=self.title,
            content=self.content,
            date=datetime.datetime.now()
        )


