def deleteCidInText(text):
    index = text.find("cid") - 2
    text = text[:index] 
    text +=" }\""
    return text

text = "h bài này lắm, cid: Ugz4S7HQPQdAhsxLHKt4AaABAg}"
print(deleteCidInText(text))