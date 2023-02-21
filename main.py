import settings
import openai
import subprocess
from sys import platform

p = 'win32'
if platform == "linux" or platform == "linux2":
    p = 'linux'

elif platform == "darwin":
    p = 'mac'


openai.api_key = settings.OPEN_AI_API_KEY
# openai.organization = settings.OPEN_AI_ORGANIZATION

engiens = openai.Engine.list()


# ids = [engine.id for engine in engiens['data']]
# print(ids)

user_prompt = input('Enter your prompt: ')
gpt_prompt = f'can you create a python script that will run the following command on {p}?\n' \
    f'{user_prompt}\n' \
    'please answer in yes or no.'

script_prompt = f'write the following command as a python script on {p}:' \
    f'{user_prompt}\n'

# ['babbage', 'davinci', 'text-embedding-ada-002', 'babbage-code-search-code', 'text-similarity-babbage-001', 'text-davinci-001', 'ada', 'curie-instruct-beta', 'babbage-code-search-text', 'babbage-similarity', 'curie-search-query', 'code-search-babbage-text-001', 'code-cushman-001', 'code-search-babbage-code-001', 'audio-transcribe-deprecated', 'text-ada-001', 'text-similarity-ada-001', 'text-davinci-insert-002', 'ada-code-search-code', 'ada-similarity', 'text-davinci-003', 'code-search-ada-text-001', 'text-search-ada-query-001', 'text-curie-001', 'text-davinci-edit-001', 'davinci-search-document', 'ada-code-search-text',
#     'text-search-ada-doc-001', 'code-davinci-edit-001', 'davinci-instruct-beta', 'text-similarity-curie-001', 'code-search-ada-code-001', 'ada-search-query', 'text-search-davinci-query-001', 'code-davinci-002', 'davinci-search-query', 'text-davinci-insert-001', 'babbage-search-document', 'ada-search-document', 'text-search-babbage-doc-001', 'text-davinci-002', 'text-search-curie-doc-001', 'text-search-curie-query-001', 'babbage-search-query', 'text-babbage-001', 'text-search-davinci-doc-001', 'text-search-babbage-query-001', 'curie-similarity', 'curie-search-document', 'curie', 'text-similarity-davinci-001', 'davinci-similarity']


def main():
    # print the first engine's id

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=gpt_prompt,
            temperature=0.5,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

    except Exception as e:
        print(e)
        return
    if 'yes' in response.choices[0].text.lower():

        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=script_prompt,
                temperature=0.5,
                max_tokens=1024,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )

            # with open('script.py', 'w') as f:
            #     f.write(response.choices[0].text)

            # subprocess.run(['python3', 'script.py'])

            exec(response.choices[0].text)

        except Exception as e:
            print(e)
            return

    else:
        print('Sorry, I cannot help you with that.')


if __name__ == "__main__":
    main()
