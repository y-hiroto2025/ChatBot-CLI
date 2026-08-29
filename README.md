# ChatBot-CLI

## Overview
シンプルなCLIチャットボットです。Gemini APIを使用して、複数の会話を保持しながら対話ができます。個人開発の基礎を学ぶため作成しました。

また、学習目的のためディレクトリ構成や環境構築、ソースのベースコードについてはLLMの出力を利用しています。

## Features
- gemini-3.5-flash.liteを使用した応答
- リストを利用して複数ターンの会話を保持
- JSONLを用いた会話履歴の保存

## Tech Stack
- **Language**: Python 3.12+
- **Package Manager**: uv
- **LLM**: google-genai (Gemini 3.5 Flash Lite)
- **Logging**: loguru
- **Validation**: pydantic
- **CI / Tools**: Ruff, pytest, GitHub Actions

## How to Run
1. リポジトリをクローンし、'.env'ファイルに`GEMINI_API_KEY=あなたのキー` を設定
2. 以下のコマンドで起動
```bash
uv run python src/chatbot_cli/main.py
```