# Discord Bot (Python)

Discord ボット - Python (discord.py) で作成されています。

## 機能

- **Pingコマンド** - ボットの応答時間を確認
- **Helpコマンド** - 利用可能なコマンド一覧を表示
- **サーバー情報** - サーバーの詳細統計を表示
- **ユーザー情報** - ユーザーの情報を表示
- **メッセージ削除** - メッセージの一括削除（権限が必要）
- **Keep-Aliveサーバー** - Flask経由でボットを稼働し続けるHTTPサーバー

## セットアップ手順

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

または、`uv`を使用している場合：

```bash
uv sync
```

### 2. 環境変数の設定

`.env`ファイルを作成して、以下の内容を追加してください：

```env
DISCORD_TOKEN=your_bot_token_here
PREFIX=!
PORT=5000
```

### 3. Discord ボットを作成

1. [Discord Developer Portal](https://discord.com/developers/applications) にアクセス
2. "New Application" をクリックして名前を入力
3. "Bot" タブに移動して "Add Bot" をクリック
4. ボットのユーザー名の下にある "Reset Token" をクリックしてトークンをコピー
5. 以下の Privileged Gateway Intents を有効にする：
   - Server Members Intent
   - Message Content Intent

### 4. ボットをサーバーに招待

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

### 5. ボットを実行

```bash
python bot.py
```

または、`uv`を使用している場合：

```bash
uv run bot.py
```

## 利用可能なコマンド

各コマンドの前にプレフィックス `!` を付けて使用します（環境変数でカスタマイズ可能）：

- `!ping` - ボットの応答速度を確認
- `!help` - すべてのコマンドを表示
- `!serverinfo` - サーバー情報を表示
- `!userinfo [@user]` - ユーザー情報を表示
- `!clear <数字>` - 指定した数のメッセージを削除（1-100）

## カスタマイズ

### コマンドプレフィックスの変更

`.env`ファイルの`PREFIX`を変更して、お好みのプレフィックスを設定（デフォルトは`!`）

### 新しいコマンドの追加

1. `bot.py` にコマンド関数を追加
2. 次のテンプレートに従ってください：

```python
@bot.command(name='コマンド名')
async def コマンド名(ctx):
    """コマンドの説明"""
    await ctx.send('応答内容')
```

3. ボットを再起動すると、コマンドが自動的に読み込まれます！

## プロジェクト構成

```
cafe_book_tmp/
├── bot.py           # メインのボットファイル
├── keep_alive.py     # Keep-aliveサーバー
├── pyproject.toml    # 依存関係管理
├── uv.lock          # 依存関係のロックファイル
├── .env             # 環境変数（作成が必要）
└── README.md        # このファイル
```

## 依存関係

- `discord.py>=2.6.4` - Discord Bot API
- `flask>=3.1.2` - Keep-aliveサーバー
- `python-dotenv>=1.2.1` - 環境変数管理

## サポート

問題や質問がある場合は、[discord.py ドキュメント](https://discordpy.readthedocs.io/) をご確認ください。

## ライセンス

ISC
