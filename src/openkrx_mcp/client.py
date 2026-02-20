import json

import httpx


class OpenKrxClient:
    BASE_URL = "https://data-dbg.krx.co.kr/svc/apis"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._http: httpx.AsyncClient | None = None

    @property
    def http(self) -> httpx.AsyncClient:
        if self._http is None or self._http.is_closed:
            self._http = httpx.AsyncClient(timeout=30.0)
        return self._http

    async def get(self, endpoint: str, params: dict | None = None) -> dict:
        """KRX Open API GET 요청.

        Args:
            endpoint: API 엔드포인트 경로 (예: "sto/stk_bydd_trd")
            params: 추가 쿼리 파라미터
        """
        request_params = {"AUTH_KEY": self.api_key}
        if params:
            request_params.update(params)

        url = f"{self.BASE_URL}/{endpoint}"
        response = await self.http.get(url, params=request_params)
        response.raise_for_status()
        return response.json()

    async def close(self):
        if self._http and not self._http.is_closed:
            await self._http.aclose()


def format_response(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)
