class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        ans = input(f"{self.question_number+1}: {self.question_list[self.question_number].text}(TRUE/ FALSE)").upper()

        self.check(ans,self.question_list[self.question_number].answer)
        self.question_number += 1

    def check(self, user,correct):
        if user == correct.upper():
            print("Correct answer")
            self.score+=1
        else:
            print("Wrong answer")
        print(f"Score{self.score}/{self.question_number+1}")