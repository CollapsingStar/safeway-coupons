import random
import string

WORD_LIST = [
    "almost",
    "avid",
    "awning",
    "bakery",
    "barmaid",
    "bribe",
    "briskness",
    "canopener",
    "collage",
    "component",
    "computing",
    "corned",
    "cried",
    "crumb",
    "curliness",
    "curvature",
    "cycle",
    "darkening",
    "deflector",
    "desolate",
    "detergent",
    "dipped",
    "disfigure",
    "distinct",
    "duress",
    "ebony",
    "elated",
    "elusive",
    "emcee",
    "emphasize",
    "enjoyable",
    "exact",
    "fall",
    "flatness",
    "footpath",
    "getaway",
    "groom",
    "guts",
    "hangnail",
    "headlamp",
    "headlock",
    "jailbird",
    "kinetic",
    "landfill",
    "linguini",
    "maroon",
    "mouse",
    "nectar",
    "neuron",
    "numerous",
    "nylon",
    "ounce",
    "outburst",
    "overbuilt",
    "pogo",
    "profusely",
    "province",
    "puzzling",
    "quickly",
    "rascal",
    "record",
    "refutable",
    "robotics",
    "rule",
    "sadness",
    "sandlot",
    "schematic",
    "scruffy",
    "secrecy",
    "shaping",
    "skipper",
    "smolder",
    "smooth",
    "snowiness",
    "spirits",
    "spoon",
    "spray",
    "steering",
    "stung",
    "stylized",
    "subarctic",
    "sulfate",
    "throwback",
    "tipper",
    "tweezers",
    "uncoated",
    "unlovely",
    "unmanaged",
    "unmatched",
    "unproven",
    "unrevised",
    "uplifted",
    "viability",
    "vocalist",
    "vocalize",
    "washbasin",
    "washing",
    "womb",
    "xerox",
    "yin",
]


def make_token() -> str:
    return "-".join(random.choices(WORD_LIST, k=4))


def make_nonce() -> str:
    return "".join(
        random.choices(
            string.ascii_lowercase + string.ascii_uppercase + string.digits,
            k=62,
        )
    )
