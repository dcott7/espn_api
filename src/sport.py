from enum import Enum

class Sport(Enum):
    AUSTRALIAN_FOOTBALL = "australian-football"
    BASEBALL = "baseball"
    BASKETBALL = "basketball"
    CRICKET = "cricket"
    FIELD_HOCKEY = "field-hockey"
    FOOTBALL = "football"
    GOLF = "golf"
    HOCKEY = "hockey"
    LACROSSE = "lacrosse"
    MMA = "mma"
    RACING = "racing"
    RUGBY = "rugby"
    RUGBY_LEAGUE = "rugby-league"
    SOCCER = "soccer"
    TENNIS = "tennis"
    VOLLEYBALL = "volleyball"
    WATER_POLO = "water-polo"

class AustralianFootballLeagues(Enum):
    AFL = "afl"

class BaseballLeagues(Enum):
    CARIBBEAN_SERIES = "caribbean-series"
    COLLEGE_BASEBALL = "college-baseball"
    COLLEGE_SOFTBALL = "college-softball"
    DOMINICAN_WINTER_LEAGUE = "dominican-winter-league"
    LLB = "llb"
    MEXICAN_WINTER_LEAGUE = "mexican-winter-league"
    MLB = "mlb"
    OLYMPICS_BASEBALL = "olympics-baseball"
    PUERTO_RICAN_WINTER_LEAGUE = "puerto-rican-winter-league"
    VENEZUELAN_WINTER_LEAGUE = "venezuelan-winter-league"
    WORLD_BASEBALL_CLASSIC = "world-baseball-classic"

class BasketballLeagues(Enum):
    FIBA = "fiba"
    MENS_COLLEGE_BASKETBALL = "mens-college-basketball"
    MENS_OLYMPICS_BASKETBALL = "mens-olympics-basketball"
    NBA = "nba"
    NBA_DEVELOPMENT = "nba-development"
    NBA_SUMMER_GOLDEN_STATE = "nba-summer-golden-state"
    NBA_SUMMER_LAS_VEGAS = "nba-summer-las-vegas"
    NBA_SUMMER_ORLANDO = "nba-summer-orlando"
    NBA_SUMMER_SACRAMENTO = "nba-summer-sacramento"
    NBA_SUMMER_UTAH = "nba-summer-utah"
    NBL = "nbl"
    WNBA = "wnba"
    WOMENS_COLLEGE_BASKETBALL = "womens-college-basketball"
    WOMENS_OLYMPICS_BASKETBALL = "womens-olympics-basketball"

class CricketLeagues(Enum):
    # No leagues found
    pass

class FieldHockeyLeagues(Enum):
    WOMENS_COLLEGE_FIELD_HOCKEY = "womens-college-field-hockey"

class FootballLeagues(Enum):
    CFL = "cfl"
    COLLEGE_FOOTBALL = "college-football"
    NFL = "nfl"
    UFL = "ufl"
    XFL = "xfl"

class GolfLeagues(Enum):
    CHAMPIONS_TOUR = "champions-tour"
    EUR = "eur"
    LIV = "liv"
    LPGA = "lpga"
    MENS_OLYMPICS_GOLF = "mens-olympics-golf"
    NTW = "ntw"
    PGA = "pga"
    WOMENS_OLYMPICS_GOLF = "womens-olympics-golf"

class HockeyLeagues(Enum):
    HOCKEY_WORLD_CUP = "hockey-world-cup"
    MENS_COLLEGE_HOCKEY = "mens-college-hockey"
    NHL = "nhl"
    OLYMPICS_MENS_ICE_HOCKEY = "olympics-mens-ice-hockey"
    OLYMPICS_WOMENS_ICE_HOCKEY = "olympics-womens-ice-hockey"
    WOMENS_COLLEGE_HOCKEY = "womens-college-hockey"

class LacrosseLeagues(Enum):
    MENS_COLLEGE_LACROSSE = "mens-college-lacrosse"
    PLL = "pll"
    WOMENS_COLLEGE_LACROSSE = "womens-college-lacrosse"

class MMALeagues(Enum):
    ABSOLUTE = "absolute"
    AFFLICTION = "affliction"
    BAMMA = "bamma"
    BANG_FIGHTING = "bang-fighting"
    BANNI_FIGHT = "banni-fight"
    BANZAY = "banzay"
    BARRACAO = "barracao"
    BATTLEZONE = "battlezone"
    BELLATOR = "bellator"
    BENAVIDES = "benevides"
    BIG_FIGHT = "big-fight"
    BLACKOUT = "blackout"
    BOSNIA = "bosnia"
    BOXE = "boxe"
    BRAZILIAN_FREESTYLE = "brazilian-freestyle"
    BUDO = "budo"
    CAGE_WARRIORS = "cage-warriors"
    CES = "ces"
    DREAM = "dream"
    FNG = "fng"
    IFC = "ifc"
    IFL = "ifl"
    K1 = "k1"
    KSW = "ksw"
    LFA = "lfa"

class RacingLeagues(Enum):
    F1 = "f1"
    IRL = "irl"
    NASCAR_PREMIER = "nascar-premier"
    NASCAR_SECONDARY = "nascar-secondary"
    NASCAR_TRUCK = "nascar-truck"
    NHRA = "nhra"

class RugbyLeagues(Enum):
    LEAGUE_268565 = "268565"
    LEAGUE_164205 = "164205"
    LEAGUE_180659 = "180659"
    LEAGUE_244293 = "244293"
    LEAGUE_271937 = "271937"
    LEAGUE_272073 = "272073"
    LEAGUE_267979 = "267979"
    LEAGUE_270559 = "270559"
    LEAGUE_270557 = "270557"
    LEAGUE_2009 = "2009"
    LEAGUE_242041 = "242041"
    LEAGUE_289271 = "289271"
    LEAGUE_289272 = "289272"
    LEAGUE_289277 = "289277"
    LEAGUE_270555 = "270555"
    LEAGUE_270563 = "270563"
    LEAGUE_236461 = "236461"
    LEAGUE_289274 = "289274"
    LEAGUE_282 = "282"
    LEAGUE_283 = "283"
    LEAGUE_289237 = "289237"
    LEAGUE_289262 = "289262"

class SoccerLeagues(Enum):
    UEFA_CHAMPIONS = "uefa.champions"
    UEFA_EUROPA = "uefa.europa"
    UEFA_EUROPA_CONF = "uefa.europa.conf"
    ENG_1 = "eng.1"
    ESP_1 = "esp.1"
    GER_1 = "ger.1"
    USA_1 = "usa.1"
    USA_NWSL = "usa.nwsl"
    USA_OPEN = "usa.open"
    MEX_1 = "mex.1"
    ITA_1 = "ita.1"
    FRA_1 = "fra.1"
    KSA_1 = "ksa.1"
    NED_1 = "ned.1"
    POR_1 = "por.1"
    ENG_LEAGUE_CUP = "eng.league_cup"
    ENG_FA = "eng.fa"
    ENG_2 = "eng.2"
    ESP_COPA_DEL_REY = "esp.copa_del_rey"
    GER_DFB_POKAL = "ger.dfb_pokal"
    ITA_COPPA_ITALIA = "ita.coppa_italia"
    FRA_COUPE_DE_FRANCE = "fra.coupe_de_france"
    NED_CUP = "ned.cup"
    POR_TACA_PORTUGAL = "por.taca.portugal"
    KSA_KINGS_CUP = "ksa.kings.cup"

class TennisLeagues(Enum):
    ATP = "atp"
    WTA = "wta"

class VolleyballLeagues(Enum):
    MENS_COLLEGE_VOLLEYBALL = "mens-college-volleyball"
    WOMENS_COLLEGE_VOLLEYBALL = "womens-college-volleyball"

class WaterPoloLeagues(Enum):
    MENS_COLLEGE_WATER_POLO = "mens-college-water-polo"
    WOMENS_COLLEGE_WATER_POLO = "womens-college-water-polo"
