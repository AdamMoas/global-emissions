
from app.dto.country_dto import Country


def test_country_dto():
    country_fields = {
        "country_name": "Antarctica",
        "iso_code": "672",
        "year": 2023,
        "total_emissions": 1,
        "coal": 1,
        "oil": 1,
        "gas": 1,
        "cement": 1,
        "flaring": 1,
        "other": 1,
        "per_capita": 1,
    }
    country = Country(**country_fields)

    assert country.country_name == "Antarctica"
    assert country.iso_code == "672"
    assert country.year == 2023
    assert country.total_emissions == 1
    assert country.coal == 1
    assert country.oil == 1
    assert country.gas == 1
    assert country.cement == 1
    assert country.flaring == 1
    assert country.other == 1
    assert country.per_capita == 1

