from mcp.server.fastmcp import FastMCP

from openkrx_mcp.client import OpenKrxClient, format_response


def register_tools(mcp: FastMCP, client: OpenKrxClient):
    @mcp.tool()
    async def get_kospi_stock_daily(basDd: str) -> str:
        """유가증권(KOSPI) 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("sto/stk_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_kosdaq_stock_daily(basDd: str) -> str:
        """코스닥(KOSDAQ) 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("sto/ksq_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_konex_stock_daily(basDd: str) -> str:
        """코넥스(KONEX) 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("sto/knx_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_stock_warrant_daily(basDd: str) -> str:
        """신주인수권증권 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("sto/sw_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_subscription_rights_daily(basDd: str) -> str:
        """신주인수권증서 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("sto/sr_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_kospi_stock_base_info(basDd: str) -> str:
        """유가증권(KOSPI) 종목기본정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("sto/stk_isu_base_info", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_kosdaq_stock_base_info(basDd: str) -> str:
        """코스닥(KOSDAQ) 종목기본정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("sto/ksq_isu_base_info", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_konex_stock_base_info(basDd: str) -> str:
        """코넥스(KONEX) 종목기본정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("sto/knx_isu_base_info", {"basDd": basDd})
        return format_response(data)
