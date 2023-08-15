import openai
from configs import conf


def run():
    openai.api_key = conf.get("api_key")
    section_size = 1000
    result = ""

    sections = split_file_to_sections("xxxxx", section_size)
    for seg in sections:
        result += section_analysis(seg, section_size) + "\n"

    print(result)


def split_file_to_sections(path: str, section_size: int):
    sections = []

    cur_section = ""
    with open(path, 'r') as file:
        for line in file:
            cur_section += line + "\n"

            if len(cur_section) >= section_size:
                sections.append(cur_section)
                cur_section = ""

    if cur_section is not "":
        sections.append(cur_section)

    return sections


def section_analysis(section: str, section_size: int):
    messages = [
        {"role": "user", "content": "总结段落文字的要点，要有一定的核心细节，字数控制在" +
            section_size + "字以内，并且不要回复任何与该段文字无关的内容，段落文字为：```" + section+"```"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=messages,
    )

    return response.choices[0].message.content
