import settings
import openai
import subprocess

openai.api_key = settings.OPEN_AI_API_KEY
openai.organization = settings.OPEN_AI_ORGANIZATION


user_prompt = input('Enter your prompt: ')

gpt_prompt = 'can you create create a powershell script that will run the following command?\n' \
    f'{user_prompt}\n' \
    'please answer in yes or no.'

script_prompt = 'write the following command as a powershell script:' \
    '5+10\n'


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

        result = subprocess.run(['powershell.exe', '-ExecutionPolicy',
                                 'Unrestricted', '-File', 'test.ps1'])

        print(result.stdout)


if __name__ == "__main__":
    main()
