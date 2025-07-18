class Quest:
    def __init__(self, id, question, answer, difficulty):
        self.id = id
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'difficulty': self.difficulty
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            question=data['question'],
            answer=data['answer'],
            difficulty=data['difficulty']
        )