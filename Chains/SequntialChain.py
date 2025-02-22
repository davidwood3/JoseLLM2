# %%
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
os.unsetenv("OPENAI_API_KEY")

# Check if the variables are loaded correctly
print("DAVID:", os.getenv("DAVID"))
print("OPENAI_API_KEY:", os.environ.get("OPENAI_API_KEY"))


# %%
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import SequentialChain, LLMChain
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate


# %%
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# %%
# Employee Performance Review INPUT TEXT
# review_text --> LLMCHAIN --> Summary
# Summary --> LLMCHAIN --> Weakness
# Weaknesses --> LLMCHAIN --> Improvement Plan

# %%
template1 = "Give a summary of this employee's performance review\n{review}"
prompt1 = ChatPromptTemplate.from_template(template1)
chain1 = LLMChain(llm=llm, prompt=prompt1,output_key="review_summary")


# %%
template2 = "Identify key employee weaknesses in the review summary:\n{review_summary}"
prompt2 = ChatPromptTemplate.from_template(template2)
chain2 = LLMChain(llm=llm, prompt=prompt2,output_key="weaknesses")

# %%
template3 = "Generate an improvement plan for the employee based on the weaknesses:\n{weaknesses}"
prompt3 = ChatPromptTemplate.from_template(template3)
chain3 = LLMChain(llm=llm, prompt=prompt3,output_key="final_plan")

# %%
employee_review = '''
Employee Information:
Name: Joe Schmo
Position: Software Engineer
Date of Review: July 14, 2023

Strengths:
Joe is a highly skilled software engineer with a deep understanding of programming languages, algorithms, and software development best practices. His technical expertise shines through in his ability to efficiently solve complex problems and deliver high-quality code.

One of Joe's greatest strengths is his collaborative nature. He actively engages with cross-functional teams, contributing valuable insights and seeking input from others. His open-mindedness and willingness to learn from colleagues make him a true team player.

Joe consistently demonstrates initiative and self-motivation. He takes the lead in seeking out new projects and challenges, and his proactive attitude has led to significant improvements in existing processes and systems. His dedication to self-improvement and growth is commendable.

Another notable strength is Joe's adaptability. He has shown great flexibility in handling changing project requirements and learning new technologies. This adaptability allows him to seamlessly transition between different projects and tasks, making him a valuable asset to the team.

Joe's problem-solving skills are exceptional. He approaches issues with a logical mindset and consistently finds effective solutions, often thinking outside the box. His ability to break down complex problems into manageable parts is key to his success in resolving issues efficiently.

Weaknesses:
While Joe possesses numerous strengths, there are a few areas where he could benefit from improvement. One such area is time management. Occasionally, Joe struggles with effectively managing his time, resulting in missed deadlines or the need for additional support to complete tasks on time. Developing better prioritization and time management techniques would greatly enhance his efficiency.

Another area for improvement is Joe's written communication skills. While he communicates well verbally, there have been instances where his written documentation lacked clarity, leading to confusion among team members. Focusing on enhancing his written communication abilities will help him effectively convey ideas and instructions.

Additionally, Joe tends to take on too many responsibilities and hesitates to delegate tasks to others. This can result in an excessive workload and potential burnout. Encouraging him to delegate tasks appropriately will not only alleviate his own workload but also foster a more balanced and productive team environment.
'''


# %%
seq_chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=["review"],
    output_variables=["review_summary", "weaknesses","final_plan"],
    verbose=True
)

# %%
result = seq_chain.invoke(employee_review)
import os

def format_output(result):
    output = ""
    for key, value in result.items():
        output += f"\n{key}:\n{value}"
        paragraphs = value.split("\n\n")
        output += "\n\n".join(f"\n{paragraph}" for paragraph in paragraphs)
    print(output)

format_output(result)
