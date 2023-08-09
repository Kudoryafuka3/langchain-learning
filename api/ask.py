from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str
    history: List[Union[str, List[str]]]


@app.post("/ask")
async def ask_question(request: QuestionRequest):
    question = request.question.lower()
    history = request.history

    last_appearance = ''

    for row in history:
        print(f'row = {row}')
        for col in row:
            print(f'col = {col}')
            last_appearance = check_last_occurrence(col)

    response = {
        "result": last_appearance,
        "history": history + [question.split(',')]
    }
    return response


class StringInput(BaseModel):
    text: str


def check_last_occurrence(s):
    indices = {
        '盘古': s.rfind('盘古'),
        'pangu': s.rfind('pangu'),
        'glm': max(s.rfind('glm'), s.rfind('chatglm'), s.rfind('chatglm2'))
    }

    # 找到最后出现的词
    last_word = max(indices, key=indices.get)
    return last_word


@app.post("/check_string/")
def check_string(input: StringInput):
    return {"last_word": check_last_occurrence(input.text)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
