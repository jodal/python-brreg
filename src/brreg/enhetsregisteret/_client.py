from typing import Optional

import httpx

from brreg import BrregError, BrregRestError

from ._types import Enhet

BASE_URL = "https://data.brreg.no/enhetsregisteret/api"


def get_enhet(organisasjonsnummer: str) -> Optional[Enhet]:
    """Get :class:`Enhet` given an organization number.

    Returns :class:`None` if Enhet is gone or not found
    Returns :class:`Enhet` if Enhet is found

    Raises :class:`BrregRestException` if a REST exception occures
    Raises :class:`BrregException` if an unhandled exception occures
    """
    res: Optional[httpx.Response] = None
    try:
        res = httpx.get(f"{BASE_URL}/enheter/{organisasjonsnummer}")

        if res.status_code in (404, 410):
            return None

        res.raise_for_status()

        return Enhet.from_json(res.json())
    except httpx.HTTPError as exc:
        raise BrregRestError(
            str(exc),
            method=(exc.request.method if exc.request else None),
            url=(str(exc.request.url) if exc.request else None),
            status_code=(res.status_code if res else None),
        ) from exc
    except Exception as exc:
        raise BrregError(exc) from exc
