import hexAI

ai = hexAI.chat()

# ========= METHOD: ask ==========
# question: Questions to ask
# flowchart: Continue to answer the above issue if you have more questions
# newChat: Refresh chat


qes1 = ai.ask(question='Computer history', flowchart=True, newChat=False)
print('Title:', qes1.title)
print('Result:', qes1.result)

# Ask the next question

qes2 = ai.ask(question='Based on your answer and translated into Vietnamese', flowchart=True, newChat=False)
print('Title:', qes2.title)
print('Result:', qes2.result)


# Refresh chat

qes3 = ai.ask(question='Did I ask you anything earlier?', flowchart=False, newChat=True)
print(qes3.result)
