# Discord Bot Project

## Overview
Python製のDiscordボットプロジェクト。discord.pyを使用し、Replitでの稼働を前提に設計されています。

## 最終更新: 2025-10-27

## プロジェクト構成

### メインファイル
- `main.py` - Discord botのメインファイル（コマンド実装を含む）
- `keep_alive.py` - Replitで稼働し続けるためのFlask HTTPサーバー
- `README.md` - セットアップガイド（日本語）

### 設定ファイル
- `pyproject.toml` - Python依存関係管理（uv）
- `.env.example` - 環境変数のテンプレート
- `.gitignore` - Gitの除外設定

## インストール済みパッケージ
- discord.py - Discord API ライブラリ
- flask - Keep-alive HTTPサーバー用
- python-dotenv - 環境変数管理

## 必要な環境変数
- `DISCORD_TOKEN` (必須) - Discordボットトークン
- `PREFIX` (オプション) - コマンドプレフィックス（デフォルト: `!`）
- `PORT` (オプション) - HTTPサーバーポート（デフォルト: 5000）

## 実装済み機能
1. **Pingコマンド** (`!ping`) - ボットの応答速度確認
2. **Helpコマンド** (`!help`) - コマンド一覧表示
3. **サーバー情報** (`!serverinfo`) - サーバー統計表示
4. **ユーザー情報** (`!userinfo [@user]`) - ユーザー情報表示
5. **メッセージ削除** (`!clear <数>`) - メッセージ一括削除
6. **Keep-Aliveサーバー** - Replitでの稼働維持

## ユーザー設定
- 言語: 日本語
- フレームワーク: discord.py (Python)
- ホスティング: Replit
- GitHubリポジトリ: https://github.com/tomato378/discord_cafebook_tmp.git

## 次のステップ
1. Discord Developer PortalでBot Tokenを取得
2. Replit SecretsにDISCORD_TOKENを追加
3. Runボタンでボット起動
4. GitHubへプッシュ（README参照）
