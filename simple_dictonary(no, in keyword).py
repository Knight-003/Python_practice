dic = {"pragmatic": "being practical to a problem", "paranoid":"wrongly believing that other people are trying to harm you " , "attiquate":"manners"}


val = str(input("enter the word"))


if(val in dic):{

    
    print(dic[val])
}
else : {
    print("sorry this word is not available in our dictonary")
}
