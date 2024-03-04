from langchain_core.messages import AIMessage, HumanMessage

blob ="_h_:Hi there -br- _h_:How are you? -br- _ai_:Hello, how can I help you? -br- _h_:What's the weather like? -br- _ai_:The weather is sunny today. -br- _h_:Tell me a joke -br- _ai_:Why did the chicken cross the road?"

#  split the blob at every -br- to get a list of messages
messages = blob.split(" -br- ")


# Extract human and AI pairs
human_messages = []
ai_messages = []

for msg in messages:
    if msg.startswith("_h_:"):
        human_messages.append(HumanMessage(content=msg.split(":")[1].strip()))
        ai_messages.append(AIMessage(content=""))
    elif msg.startswith("_ai_:"):
        ai_messages[-1] = AIMessage(content=msg.split(":")[1].strip())

# Create a list of pairs
message_pairs = list(zip(human_messages, ai_messages))


print(message_pairs)