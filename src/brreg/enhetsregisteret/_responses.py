from typing import List, Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from pydantic.alias_generators import to_camel

from brreg.enhetsregisteret._types import DateOrNone

__all__ = [
    "Adresse",
    "Enhet",
    "InstitusjonellSektorkode",
    "NaeringskodeModel",
    "Organisasjonsform",
]


class InstitusjonellSektorkode(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    #: Sektorkoden
    kode: Optional[str] = None

    #: Tekstlig beskrivelse av sektorkoden
    beskrivelse: Optional[str] = None


class Adresse(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    #: Adresse
    adresse: List[Optional[str]] = Field(default_factory=list)

    #: Postnummer
    postnummer: Optional[str] = None

    #: Poststed
    poststed: Optional[str] = None

    #: Kommunenummer
    kommunenummer: Optional[str] = None

    #: Kommune
    kommune: Optional[str] = None

    #: Landkode
    landkode: Optional[str] = None

    #: Land
    land: Optional[str] = None


class NaeringskodeModel(BaseModel):
    """Næringskode.

    Organisasjonsform er virksomhetens formelle organisering og gir
    retningslinjer overfor blant annet ansvarsforhold, skatt, revisjonsplikt,
    rettigheter og plikter.
    """

    model_config = ConfigDict(alias_generator=to_camel)

    #: Næringskoden
    kode: Optional[str] = None

    #: Tekstlig beskrivelse av næringskoden
    beskrivelse: Optional[str] = None


class Organisasjonsform(BaseModel):
    """Organisasjonsform er virksomhetens formelle organisering.

    Organisasjonsform gir retningslinjer overfor blant annet ansvarsforhold,
    skatt, revisjonsplikt, rettigheter og plikter.
    """

    model_config = ConfigDict(alias_generator=to_camel)

    #: Organisasjonsformen
    kode: str

    #: Tekstlig beskrivelse av organisasjonsformen
    beskrivelse: str

    #: Dato når organisasjonsformen evt. ble ugyldig
    utgaatt: DateOrNone = None


class Enhet(BaseModel):
    """Enhet på øverste nivå i registreringsstrukturen i Enhetsregisteret.

    Eksempelvis enkeltpersonforetak, foreninger, selskap, sameier og andre som
    er registrert i Enhetsregisteret. Identifiseres med organisasjonsnummer.
    """

    model_config = ConfigDict(alias_generator=to_camel)

    #: Organisasjonsnummer
    organisasjonsnummer: str

    #: Navn
    navn: str

    #: Organisasjonsform
    organisasjonsform: Organisasjonsform

    #: Hjemmeside
    hjemmeside: Optional[str] = None

    #: Enhetens postadresse
    postadresse: Optional[Adresse] = None

    #: Registreringsdato i Enhetsregisteret
    registreringsdato_enhetsregisteret: DateOrNone = None

    #: Hvorvidt enheten er registrert i MVA-registeret
    registrert_i_mvaregisteret: Optional[bool] = None

    #: Enheter som i utgangspunktet ikke er mva-pliktig, kan søke om frivillig
    #: registrering i Merverdiavgiftsregisteret
    frivillig_mva_registrert_beskrivelser: List[str] = Field(default_factory=list)

    #: Næringskode 1
    naeringskode1: Optional[NaeringskodeModel] = None

    #: Næringskode 2
    naeringskode2: Optional[NaeringskodeModel] = None

    #: Næringskode 3
    naeringskode3: Optional[NaeringskodeModel] = None

    #: Hjelpeenhetskode
    hjelpeenhetskode: Optional[NaeringskodeModel] = None

    #: Antall ansatte
    antall_ansatte: Optional[int] = None

    #: Angir om enheten har registrert ansatte
    har_registrert_antall_ansatte: Optional[bool] = None

    #: Organisasjonsnummeret til overordnet enhet i offentlig sektor
    overordnet_enhet: Optional[str] = None

    #: Forretningsadresse
    forretningsadresse: Optional[Adresse] = None

    #: Stiftelsesdato
    stiftelsesdato: DateOrNone = None

    #: Sektorkode
    institusjonell_sektorkode: Optional[InstitusjonellSektorkode] = None

    #: Hvorvidt enheten er registrert i Foretaksregisteret
    registrert_i_foretaksregisteret: Optional[bool] = None

    #: Hvorvidt enheten er registrert i Stiftelsesregisteret
    registrert_i_stiftelsesregisteret: Optional[bool] = None

    #: Hvorvidt enheten er registrert i Frivillighetsregisteret
    registrert_i_frivillighetsregisteret: Optional[bool] = None

    #: År for siste innsendte årsregnskap
    siste_innsendte_aarsregnskap: Optional[int] = None

    #: Hvorvidt enheten er konkurs
    konkurs: Optional[bool] = None

    #: Kjennelsesdato for konkursen
    konkursdato: DateOrNone = None

    #: Hvorvidt enheten er under avvikling
    under_avvikling: Optional[bool] = None

    #: Hvorvidt enheten er under tvangsavvikling eller tvangsoppløsning
    under_tvangsavvikling_eller_tvangsopplosning: Optional[bool] = None

    #: Målform
    maalform: Optional[str] = None

    #: Enhetens vedtektsdato
    vedtektsdato: DateOrNone = None

    #: Enhetens formål
    vedtektsfestet_formaal: List[str] = Field(default_factory=list)

    #: Enhetens aktivitet
    aktivitet: List[str] = Field(default_factory=list)

    #: Nedleggelsesdato for underenheten
    nedleggelsesdato: DateOrNone = None

    #: Dato under-/enheten ble slettet
    slettedato: DateOrNone = None


class Underenhet(BaseModel):
    """Enhet på laveste nivå i registreringsstrukturen i Enhetsregisteret.

    En underenhet kan ikke eksistere alene og har alltid knytning til en
    hovedenhet. Identifiseres med organisasjonsnummer.
    """

    model_config = ConfigDict(alias_generator=to_camel)

    #: Underenhetens organisasjonsnummer
    organisasjonsnummer: str

    #: Underenhetens navn
    navn: str

    #: Underenhetens navn
    organisasjonsform: Organisasjonsform

    #: Underenhetens hjemmeside
    hjemmeside: Optional[str] = None

    #: Underenhetens postadresse
    postadresse: Optional[Adresse] = None

    #: Underenhetens registreringsdato i Enhetsregisteret
    registreringsdato_enhetsregisteret: DateOrNone = None

    #: Hvorvidt underenheten er registrert i MVA-registeret
    registrert_i_mvaregisteret: Optional[bool] = None

    #: Underenheter som i utgangspunktet ikke er mva-pliktig, kan søke om
    #: frivillig registrering i Merverdiavgiftsregisteret
    frivillig_mva_registrert_beskrivelser: List[str] = Field(default_factory=list)

    #: Næringskode 1
    naeringskode1: Optional[NaeringskodeModel] = None

    #: Næringskode 2
    naeringskode2: Optional[NaeringskodeModel] = None

    #: Næringskode 3
    naeringskode3: Optional[NaeringskodeModel] = None

    #: Hjelpeenhetskode
    hjelpeenhetskode: Optional[NaeringskodeModel] = None

    #: Antall ansatte
    antall_ansatte: Optional[int] = None

    #: Angir om enheten har registrert ansatte
    har_registrert_antall_ansatte: Optional[bool] = None

    #: Underenhetens overordnede enhet
    overordnet_enhet: Optional[str] = None

    #: Underenhetens beliggenhetsadresse
    beliggenhetsadresse: Optional[Adresse] = None

    #: Underenhetens oppstartsdato
    oppstartsdato: DateOrNone = None

    #: Underenhetens dato for eierskifte
    dato_eierskifte: DateOrNone = None

    #: Nedleggelsesdato for underenheten
    nedleggelsesdato: DateOrNone = None

    #: Dato under-/enheten ble slettet
    slettedato: DateOrNone = None