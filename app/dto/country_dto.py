from pydantic import BaseModel


class Country(BaseModel):
    country_name: str
    iso_code: str
    year: int
    total_emissions: int
    coal: int
    oil: int
    gas: int
    cement: int
    flaring: int
    other: int
    per_capita: int
