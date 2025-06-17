import os
from glob import glob
from openai import OpenAI

# Define folder where academic papers are located
research_paper_location = "tests/"

# Define files that should be renamed
files = glob(research_paper_location + "*.pdf")


test_file = files[0]
prompt = """You are a bibliographic information extractor. Your task is to analyze academic paper content and return ONLY a properly formatted filename.

REQUIRED OUTPUT FORMAT: AuthorYearJournal
- Author: Last name of first author only, no spaces
- Year: 4-digit publication year  
- Journal: Abbreviated journal name, no spaces

FORMATTING RULES:
1. Remove all spaces, special characters, and punctuation from the filename
2. Use standard journal abbreviations (e.g., "JFE" for Journal of Financial Economics)
3. If multiple authors, use only the FIRST author's last name
4. If year is unclear, use the most recent year mentioned
5. If journal name is very long, use a meaningful 3-4 letter abbreviation

EXAMPLES:
Input: "The Impact of..." by Smith, J. and Johnson, M. (2023) in Journal of Finance
Output: Smith2023JF

Input: "Market Efficiency..." by Rodriguez-Martinez, A. (2024) in Review of Financial Studies  
Output: Rodriguez2024RFS

If you cannot determine author, year, or journal with confidence, respond with: "INSUFFICIENT_INFO"

Respond with ONLY the formatted filename, nothing else.
"""

client = OpenAI(api_key=os.getenv("API_KEY_OPENAI"))

file = client.files.create(file=open(test_file, "rb"), purpose="user_data")

response = client.responses.create(
    model="gpt-4.1-nano",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": file.id,
                },
                {
                    "type": "input_text",
                    "text": prompt,
                },
            ],
        }
    ],
)

print(response)

response_formatted = response.output[0].content[0].text
print(response_formatted)

os.rename(test_file, research_paper_location + response_formatted + ".pdf")
