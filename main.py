import os
from glob import glob
from openai import OpenAI

# Define folder where academic papers are located
research_paper_location = "tests/"

# Define list with paths to research papers that should be renamed. Currently select all files with .pdf ending.
research_papers = glob(research_paper_location + "*.pdf")

# Define prompt
try:
    with open("prompt.txt", "r") as prompt_file:
        prompt = prompt_file.read()
except Exception as e:
    print("An error occured when loading the files:", e)

# Initialize openai client
client = OpenAI(api_key=os.getenv("API_KEY_OPENAI"))

# Run renaming loop
print(f"Renaming {len(research_papers)} research papers.")

for research_paper in research_papers:

    print(f"Renaming {research_paper}...")
    # Prepare file for LLM
    research_paper_for_LLM = client.files.create(
        file=open(research_paper, "rb"), purpose="user_data"
    )

    # Get new file name from LLM
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            temperature=0,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_file",
                            "file_id": research_paper_for_LLM.id,
                        },
                        {
                            "type": "input_text",
                            "text": prompt,
                        },
                    ],
                }
            ],
        )
    except Exception as e:
        # OpenAI currently has occasional bug
        print("Exeption during client.response.create:", e)
        print(response.id)
        print(response._request_id)
        continue

    # Remove metadata from response
    response_formatted = response.output[0].content[0].text

    print(f"... renamed to {response_formatted}.pdf")

    # Rename file
    os.rename(research_paper, research_paper_location + response_formatted + ".pdf")

print(f"All {len(research_papers)} renamed.")