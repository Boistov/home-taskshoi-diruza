class Censor:
    def long_sentence(text):
        words = text.split()
        j = []
        for i in words:
            if len(i) > 4:
                j.append("*" * len(i))
            else:
                j.append(i)
        return " ".join(j)

jumla = input("Enter-> ")
censored_text = Censor.long_sentence(jumla)
print(censored_text)
