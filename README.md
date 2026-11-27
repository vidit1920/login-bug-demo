# login-bug-demo

A tiny Python (Flask) login page with a deliberate bug, for practice and testing.

## Run

```
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. Test account: `admin` / `secret123`.

## The bug

Try signing in as `admin` with any wrong password. It still lets you in.
Find and fix it in `app.py`.
