import skills

nlp = skills.load("en_core_web_sm")

doc = nlp("Experienced Systems Administrator skilled in Active Directory and Azure.")

for token in doc:
    print(token.text, "|", token.pos_)