import json
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from pypdf import PdfReader
from docx import Document
import gradio as gr

load_dotenv(override=True)

def push(text):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message": text,
        }
    )

def record_user_details(email, name="Name not provided", notes="not provided"):
    push(f"Recording {name} with email {email} and notes {notes}")
    return {"recorded": "ok"}

def record_unknown_question(question):
    push(f"Recording {question}")
    return {"recorded": "ok"}

# Anthropic tool format uses input_schema, not parameters
tools = [
    {
        "name": "record_user_details",
        "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
        "input_schema": {
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "The email address of this user"},
                "name": {"type": "string", "description": "The user's name, if they provided it"},
                "notes": {"type": "string", "description": "Any additional information about the conversation that's worth recording to give context"}
            },
            "required": ["email"]
        }
    },
    {
        "name": "record_unknown_question",
        "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
        "input_schema": {
            "type": "object",
            "properties": {
                "question": {"type": "string", "description": "The question that couldn't be answered"}
            },
            "required": ["question"]
        }
    }
]


class Me:

    def _read_pdf(self, path):
        reader = PdfReader(path)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

    def _read_docx(self, path):
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

    def __init__(self):
        self.claude = Anthropic()
        self.openai = OpenAI()
        self.name = "Dario Melconian"
        self.model = "claude-sonnet-4-5"

        self.linkedin = self._read_pdf("me/linkedin.pdf")
        self.stars = self._read_pdf("me/INTRO_STARS.pdf")
        self.stripe = self._read_docx("me/Stripe_R1.docx")
        self.nlp_syllabus = self._read_pdf("me/3666-018_OL_Applied Natural Language Processing.pdf")

        with open("me/summary.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()

    def handle_tool_calls(self, tool_use_blocks):
        results = []
        for block in tool_use_blocks:
            tool_name = block.name
            arguments = block.input  # already a dict, no json.loads needed
            print(f"Tool called: {tool_name}", flush=True)
            tool = globals().get(tool_name)
            result = tool(**arguments) if tool else {}
            results.append({"type": "tool_result", "tool_use_id": block.id, "content": json.dumps(result)})
        return results

    def system_prompt(self):
        prompt = f"You are acting as {self.name}. You are answering questions on {self.name}'s website, \
particularly questions related to {self.name}'s career, background, skills and experience. \
Your responsibility is to represent {self.name} for interactions on the website as faithfully as possible. \
You are given a summary of {self.name}'s background in the form of their summary, LinkedIn profile, GitHub repositories, STAR project stories, and relevant coursework which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. "

        prompt += f"\n\n## Summary:\n{self.summary}\n\n## LinkedIn Profile:\n{self.linkedin}\n\n"
        prompt += f"## STAR Project Stories:\n{self.stars}\n\n"
        prompt += f"## Additional Project Details (Stripe):\n{self.stripe}\n\n"
        prompt += f"## NLP Coursework (UofT):\n{self.nlp_syllabus}\n\n"
        prompt += f"With this context, please chat with the user, always staying in character as {self.name}."
        return prompt

    def chat(self, message, history):
        clean_history = [{"role": m["role"], "content": m["content"]} for m in history if isinstance(m, dict)]
        messages = clean_history + [{"role": "user", "content": message}]
        done = False
        while not done:
            response = self.claude.messages.create(
                model=self.model,
                max_tokens=1024,
                system=self.system_prompt(),
                tools=tools,
                messages=messages
            )
            if response.stop_reason == "tool_use":
                tool_use_blocks = [block for block in response.content if block.type == "tool_use"]
                results = self.handle_tool_calls(tool_use_blocks)
                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": results})
            else:
                done = True
        return next(block.text for block in response.content if hasattr(block, "text"))


if __name__ == "__main__":
    me = Me()
    gr.ChatInterface(me.chat).launch()
