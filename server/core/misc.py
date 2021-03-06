class Overpass:
    """Sunny"""

    BASE = "http://overpass-api.de/api/interpreter?data="
    REQ = (
        BASE
        + """
[out:json];
(
    way
        [highway]
        (poly:"{}");
    >;
);
out;""".replace(
            "\n", ""
        ).replace(
            "\t", ""
        )
    )
    # ^^Replace statements only required to make the command easier to read
    # You can put this command in one line in the final version
    # Command description: Finds all ways with the tag highway in the area given,
    # then finds all nodes associated with these ways


class Color:
    green = 0x2ECC71
    red = 0xE74C3C
    orange = 0xE67E22
