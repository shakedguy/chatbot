import settings
import openai
import subprocess
from sys import platform

script_shell = 'powershell'
if platform != "win32":
    script_shell = 'bash'


openai.api_key = settings.OPEN_AI_API_KEY
openai.organization = settings.OPEN_AI_ORGANIZATION


user_prompt = input('Enter your prompt: ')
gpt_prompt = f'can you create create a {script_shell} script that will run the following command?\n' \
    f'{user_prompt}\n' \
    'please answer in yes or no.'

script_prompt = f'write the following command as a {script_shell} script:' \
    f'{user_prompt}\n'


def main():
    # print the first engine's id
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    if 'yes' in response.choices[0].text.lower():

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=script_prompt,
            temperature=0.5,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        with open('test.ps1', 'w') as f:
            f.write(response.choices[0].text)

        subprocess.run(['powershell.exe', '-ExecutionPolicy',
                        'Unrestricted', '-File', 'test.ps1'])

    else:
        print('Sorry, I cannot help you with that.')


if __name__ == "__main__":
    main()
