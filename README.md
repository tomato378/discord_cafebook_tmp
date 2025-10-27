# Discord Bot

Discord ボット - Python (discord.py) で作成されています。Replitで動作するように設計されています。

## 機能

- **Pingコマンド** - ボットの応答時間を確認
- **Helpコマンド** - 利用可能なコマンド一覧を表示
- **サーバー情報** - サーバーの詳細統計を表示
- **ユーザー情報** - ユーザーの情報を表示
- **メッセージ削除** - メッセージの一括削除（権限が必要）
- **Keep-Aliveサーバー** - Replitでボットを稼働し続けるHTTPサーバー

## セットアップ手順

### 1. Discord ボットを作成

1. [Discord Developer Portal](https://discord.com/developers/applications) にアクセス
2. "New Application" をクリックして名前を入力
3. "Bot" タブに移動して "Add Bot" をクリック
4. ボットのユーザー名の下にある "Reset Token" をクリックしてトークンをコピー
5. 以下の Privileged Gateway Intents を有効にする：
   - Server Members Intent
   - Message Content Intent

### 2. Replitにボットトークンを追加

1. Replitプロジェクトで "Tools" サイドバーを開く
2. "Secrets" をクリック
3. 新しいシークレットを追加：
   - キー: `DISCORD_TOKEN`
   - 値: コピーしたボットトークンを貼り付け

### 3. ボットをサーバーに招待

1. Discord Developer Portal で "OAuth2" > "URL Generator" に移動
2. スコープを選択：
   - `bot`
3. ボット権限を選択：
   - Read Messages/View Channels
   - Send Messages
   - Manage Messages
   - Read Message History
4. 生成されたURLをコピーしてブラウザで開く
5. サーバーを選択してボットを認証

### 4. ボットを実行

Replitの "Run" ボタンをクリック。ボットが起動してDiscordに接続します！

## 利用可能なコマンド

各コマンドの前にプレフィックス `!` を付けて使用します（環境変数でカスタマイズ可能）：

- `!ping` - ボットの応答速度を確認
- `!help` - すべてのコマンドを表示
- `!serverinfo` - サーバー情報を表示
- `!userinfo [@user]` - ユーザー情報を表示
- `!clear <数字>` - 指定した数のメッセージを削除（1-100）

## カスタマイズ

### コマンドプレフィックスの変更

Replit Secrets に `PREFIX` を追加して、お好みのプレフィックスを設定（デフォルトは `!`）

### 新しいコマンドの追加

1. `main.py` にコマンド関数を追加
2. 次のテンプレートに従ってください：

```python
@bot.command(name='コマンド名')
async def コマンド名(ctx):
    """コマンドの説明"""
    await ctx.send('応答内容')
```

3. ボットを再起動すると、コマンドが自動的に読み込まれます！

## Replitでのデプロイ

このボットは、組み込みのHTTPサーバーによりReplitでオンラインを維持するように設定されています。ボットがクラッシュしても自動的に再起動し、接続を維持します。

## GitHubへのプッシュ

プロジェクトをGitHubにプッシュするには：

1. Replitからプロジェクトをダウンロード（三点メニュー → Download as zip）
2. ファイルを展開
3. ターミナルでフォルダを開いて実行：

```bash
git init
git add .
git commit -m "Initial Discord bot setup"
git remote add origin https://github.com/あなたのユーザー名/リポジトリ名.git
git branch -M main
git push -u origin main
```

## サポート

問題や質問がある場合は、[discord.py ドキュメント](https://discordpy.readthedocs.io/) をご確認ください。

## ライセンス

ISC
