from mcp.server.fastmcp import FastMCP

from openkrx_mcp.client import OpenKrxClient, format_response


def register_tools(mcp: FastMCP, client: OpenKrxClient):
    @mcp.tool()
    async def get_krx_index_daily(basDd: str) -> str:
        """KRX 시리즈 지수 일별시세정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("idx/krx_dd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_kospi_index_daily(basDd: str) -> str:
        """KOSPI 시리즈 지수 일별시세정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("idx/kospi_dd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_kosdaq_index_daily(basDd: str) -> str:
        """KOSDAQ 시리즈 지수 일별시세정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("idx/kosdaq_dd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_bond_index_daily(basDd: str) -> str:
        """채권지수 일별시세정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("idx/bon_dd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_derivatives_index_daily(basDd: str) -> str:
        """파생상품지수 일별시세정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("idx/drvprod_dd_trd", {"basDd": basDd})
        return format_response(data)
