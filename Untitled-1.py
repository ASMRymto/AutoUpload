import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


# あなたの希望に合わせて指示文を調整
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "あなたはバズる動画プロンプトの専門家です。"},
        {"role": "user", "content": "以下のフォーマットで、Veo3用のバズりそうな動画プロンプトを3つ作ってください。\n\n【フォーマット】\n1. 果物を切るASMR映像。包丁が触れた瞬間に光が反射して幻想的な雰囲気になる。\n2. PSPを包丁でスライスするASMR。カメラは真上から固定で、音重視。\n3. 金色の人参を切るASMR。高級感のある木製まな板と、暖色系の照明。"}
    ],
    temperature=0.9
)

# 出力
print(response['choices'][0]['message']['content'])
