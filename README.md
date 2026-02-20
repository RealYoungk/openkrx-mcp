# OpenKRX MCP Server

한국거래소(KRX) Open API를 MCP(Model Context Protocol) 도구로 제공하는 서버입니다.

## 지원 API (31개)

| 카테고리 | 도구 수 | 내용 |
|---------|--------|------|
| 지수 (idx) | 5 | KRX/KOSPI/KOSDAQ/채권/파생상품 지수 일별시세 |
| 주식 (sto) | 8 | KOSPI/KOSDAQ/KONEX 일별매매정보 + 종목기본정보 |
| ETP (etp) | 3 | ETF/ETN/ELW 일별매매정보 |
| 채권 (bon) | 3 | 국채/일반채권/소액채권 일별매매정보 |
| 파생상품 (drv) | 6 | 선물/옵션 일별매매정보 (KOSPI/KOSDAQ 주식선물·옵션 포함) |
| 일반상품 (gen) | 3 | 석유/금/배출권 시장 일별매매정보 |
| ESG (esg) | 3 | SRI채권/ESG ETP/ESG 지수 정보 |

## 설치 및 사용

### 사전 준비

[KRX Open API](http://openapi.krx.co.kr)에서 회원가입 후 API 인증키를 발급받으세요.

### Claude Desktop

`claude_desktop_config.json`에 추가:

```json
{
  "mcpServers": {
    "openkrx": {
      "command": "uvx",
      "args": ["openkrx-mcp"],
      "env": {
        "KRX_API_KEY": "<YOUR_API_KEY>"
      }
    }
  }
}
```

### Claude Code

```bash
claude mcp add openkrx -e KRX_API_KEY=<YOUR_API_KEY> -- uvx openkrx-mcp
```

### 직접 실행

```bash
# stdio (로컬)
KRX_API_KEY=<YOUR_API_KEY> uvx openkrx-mcp

# SSE (원격)
KRX_API_KEY=<YOUR_API_KEY> uvx openkrx-mcp --transport sse --port 8000
```

### Docker

```bash
docker build -t openkrx-mcp .
docker run -e KRX_API_KEY=<YOUR_API_KEY> -p 8000:8000 openkrx-mcp
```

## 참고

- 데이터는 2010년 이후 일별 데이터이며, 매일 오전 8시(KST)에 갱신됩니다.
- 날짜 파라미터(`basDd`)는 `YYYYMMDD` 형식입니다.
- API 호출 한도: 10,000건

## 라이선스

MIT
