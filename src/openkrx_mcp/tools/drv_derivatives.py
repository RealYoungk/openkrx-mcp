from mcp.server.fastmcp import FastMCP

from openkrx_mcp.client import OpenKrxClient, format_response


def register_tools(mcp: FastMCP, client: OpenKrxClient):
    @mcp.tool()
    async def get_futures_daily(basDd: str) -> str:
        """선물 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("drv/fut_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_kospi_stock_futures_daily(basDd: str) -> str:
        """주식선물(유가증권) 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("drv/eqsfu_stk_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_kosdaq_stock_futures_daily(basDd: str) -> str:
        """주식선물(코스닥) 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("drv/eqkfu_ksq_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_options_daily(basDd: str) -> str:
        """옵션 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("drv/opt_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_kospi_stock_options_daily(basDd: str) -> str:
        """주식옵션(유가증권) 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("drv/eqsop_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_kosdaq_stock_options_daily(basDd: str) -> str:
        """주식옵션(코스닥) 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("drv/eqkop_bydd_trd", {"basDd": basDd})
        return format_response(data)
