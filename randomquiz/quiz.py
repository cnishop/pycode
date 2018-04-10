import random
captials={
'北京':'北京',
'天津':'天津',
'上海':'上海',
'重庆':'重庆',
'河北':'石家庄',
'河南':'郑州',
'湖北':'武汉',
'湖南':'长沙',
'江苏':'南京',
'江西':'南昌',
'辽宁':'沈阳',
'吉林':'长春',
'黑龙':'哈尔滨',
'陕西':'西安',
'山西':'太原',
'山东':'济南',
'四川':'成都',
'青海':'西宁',
'安徽':'合肥',
'海南':'海口',
'广东':'广州',
'贵州':'贵阳',
'浙江':'杭州',
'福建':'福州',
'台湾':'台北',
'甘肃':'兰州',
'云南':'昆明',
'西藏':'拉萨',
'宁夏':'银川',
'广西':'南宁',
'新疆':'乌鲁木齐',
'内蒙':'呼和浩特',
'香港':'香港',
'澳门':'澳门',
}

stuNum = int(input("\n您要出几分考卷？     "))
for quizNum in range(stuNum):
    quizFile = open('capitalsquiz{}.txt'.format(quizNum+1),'w',encoding ="utf-8")
    answerKeyFile =open('capitalsquiz_answer{}.txt'.format(quizNum+1),'w',encoding="utf-8")
    quizFile.write('姓名\n\n 学号:\n\n 班级:\n\n')
    quizFile.write(' '*20 +'省会测试卷 {}\n\n'.format(quizNum +1))

    provinces=list(captials.keys())
    random.shuffle(provinces)

    for questionNum in range(len(provinces)):
        correctAnswer =captials[provinces[questionNum]]

        wrongAnsers =list(captials.values())
        wrongAnsers.remove(correctAnswer)

        wrongAnsers =random.sample(wrongAnsers,3)
        answerOptions= wrongAnsers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('\n{}、{}的省会是? \n'.format(questionNum +1 ,provinces[questionNum]))

        for i in range(4):
            quizFile.write('{}.{}\n'.format('ABCD'[i],answerOptions[i]))

        answerKeyFile.write('{}.{}\n'.format(questionNum +1,'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()





