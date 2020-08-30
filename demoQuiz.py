# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text    = text
        self.choices = choices
        self.answer  = answer

    # Kullanıcının verdiği cevabın doğruluğunu ölçer.
    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    # Bu fonksiyonun amacı, o anki 'questionIndex'in değerine karşılık gelen  question objesini göndermek.
    def getQuestion(self):
        return self.questions[self.questionIndex]

    # Bu fonksiyon, gelen question objesini ekrana yazdırır.
    def disPlayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print('--> ' + q)

        answer = input("Cevap: ")
        self.guess(answer) # guess -> tahmin
        self.loadQuestion()

    # Bu fonksiyonun amacı, koşulsuz index numarasını arttırmak ve
    # 'checkAnswer'dan gelen değer 'True' ise score değiskenini arttırmak.
    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1

        self.questionIndex += 1

    # İndex aşımını kontrol eder.
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.disPlayProgress()
            self.disPlayQuestion()

    # Quizi bitirir ve kullanıcıya skorunu gösterir.
    def showScore(self):
        print(f"Quiz bitti. Score: {self.score}")

    # Kullanıcıya kaç sorudan kaçıncıda olduğunu gösterir.
    def disPlayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        print(f"Question {questionNumber} of {totalQuestion}".center(100, '*'))

# Soruların olduğu bölüm ---> Bu kısım biraz amele işi oldu :)
q1 = Question("En iyi programlama dili hangisidir ?", ["C#", "python", "javascript", "java"], "python")
q2 = Question("En popüler programlama dili hangisidir ?", ["java", "python", "C#", "javascript"], "python")
q3 = Question("En çok kazandıran programlama dili hangisidir ?", ["javascript", "C#", "java", "python"], "python")
q4 = Question("En çok sevilen programlama dili hangisidir ?", ["python", "C#", "java", "javascript"], "python")
q5 = Question("En kolay programlama dili hangisidir ?", ["java", "javascript", "C#", "python"], "python")

questions = [q1, q2, q3, q4, q5]
quiz = Quiz(questions)

quiz.loadQuestion()