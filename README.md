# aegis-demo-python

Flask API + form login. Target for Aegis-generated scanner pipelines.

## Run

```bash
pip install -r requirements.txt
python app.py
# open http://localhost:5000/login
# demo creds: demo@example.com / demo1234
```

## Endpoints

- `GET /` — public landing
- `GET /login` / `POST /login` — form auth
- `GET /dashboard` — requires session
- `GET /api/items` — requires session
- `POST /logout`
- `GET /healthz`
