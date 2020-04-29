from src import king_bot, settings
import sys

# these could be read in via arguments, file or login manually - read documentation
gameworld = "com3"  # choose uppercase (exact world name) - optional
email = "vlrizkidz93@tuta.io"  # optional
password = "melodies"  # optional
proxy = ""  # optional
# increase the number if your internet connecion is slow
settings.browser_speed = 1.0

kingbot = king_bot(
    email=email,
    password=password,
    gameworld=gameworld,
    proxy=proxy,
    start_args=sys.argv,
    debug=True,
)

# place your actions below
# kingbot.start_adventures(1000)

kingbot.robber_hideout(village=0, interval=600, units={4: 100, 10: -1})
kingbot.robber_camp(village=0, interval=600, units={4: 100, 10: -1})
