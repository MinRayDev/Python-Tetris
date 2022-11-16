import os
from typing import Optional

grid_types = ["cercle", "losange", "triangle"]
base_path = os.path.join(os.path.dirname(__file__).split("utils")[0])
settings: dict[str, str | int] = {"shape": "", "size": 0, "bloc_placement": 0}
random_blocs = []
grid = {"width": 0, "height": 0, "matrice": None}
log_path = ""
game_letters: Optional[list[str]] = None
common_liste = []
cercle_liste = []
losange_liste = []
triangle_liste = []
blocs_liste = []
score = 0
console_x = 0
console_y = 0

try_pos = 0

do_size: bool = True
do_shape: bool = True
do_placement: bool = True
