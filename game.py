import pygame
import random
import time
import sys
import math
from typing import Any
from pathlib import Path

# initiation pygame
pygame.init()
# mouse disable
pygame.mouse.set_visible(False)  # noqa: FBT003
# resolution
window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height))
# font in the game
font = pygame.font.Font(None, 36)
# start player position
x = 0
y = 0
# gold
points_counter = 0
# level
level = 0
# number of enemies when game started
number_devils = 0
number_fasts = 0
number_mutants = 0
number_ghosts = 0
# number of obstacless when game started
number_obstacles = 8
# max number of obstacles
max_obstacles = 18
# bullets in magazine
magazine = 0
# glag for gun hide/pick
gun_on = False
# basic player speed
speed = 8
# max player speed
max_speed = 15
# flags for eliminate double click in abilities
p_key_pressed = False
p_key_released = True
o_key_pressed = False
o_key_released = True
i_key_pressed = False
i_key_released = True
m_key_pressed = False
m_key_released = True
u_key_pressed = False
u_key_released = True
r_key_pressed = False
r_key_released = True
# flag for shield active/dont active
powershield = False
# boss hp
boss_hp = 50
# the flag checks if there is a boss fight and play boss music
bs = False
# load boss only in boss level
load_boss = False
# lists
destroyed_obstacles_list = []
bullets_list = []
dead_enemy_list = []
boss_list = []
dead_boss_list = []
obstacles_list = []
enemy_list = []
gold_list = []
borders_list = []

# intro textures
menu = pygame.image.load("textures/menu.png")
intro1 = pygame.image.load("textures/intro.png")
intro2 = pygame.image.load("textures/intro2.png")
intro3 = pygame.image.load("textures/intro3.png")
olchastudio = pygame.image.load("textures/olchastudio.png")
# dead screen texture
dead_screen = pygame.image.load("textures/deadscreen.png")
# end of the game texture
end_texture = pygame.transform.scale(
    pygame.image.load("textures/end.png"), (window_width, window_height)
)
# backgrounds textures
background1 = pygame.image.load("textures/tlo.jpg")
background2 = pygame.image.load("textures/tlo2.jpg")
background3 = pygame.image.load("textures/tlo3.jpg")
background4 = pygame.image.load("textures/tlo4.1.jpg")
background5 = pygame.image.load("textures/tlo5.png")

# scaling background textures
background1 = pygame.transform.scale(background1, window.get_size())
background2 = pygame.transform.scale(background2, window.get_size())
background3 = pygame.transform.scale(background3, window.get_size())
background4 = pygame.transform.scale(background4, window.get_size())
background5 = pygame.transform.scale(background5, window.get_size())
# list of background textures
background_list = [background1, background2, background3, background5]
# default background
background = background1


# choose random background without backgorund4
# set background 4 in 50 lvl (boss fight)
def random_background() -> pygame.Surface:
    background = (
        background4 if level % 50 == 0 else random.choice(background_list)  # noqa: S311
    )
    return background  # noqa: RET504


# all player textures scaled to 40x40 px

# player basic texture:
player1_texture = pygame.transform.scale(
    pygame.image.load("textures/player.png"), (40, 40)
)
# playe rect
player1_rect = player1_texture.get_rect()
# player mask
player1_mask = pygame.mask.from_surface(player1_texture)
# player texture with shield
player1_texture_shield = pygame.image.load("textures/playershield1.png")

# player texture with gun adaptate to player direction
player_plazma_left_texture = pygame.transform.scale(
    pygame.image.load("textures/playerplazmaL.png"), (40, 40)
)

player_plazma_right_texture = pygame.transform.scale(
    pygame.image.load("textures/playerplazmaR.png"), (40, 40)
)

player_plazma_top_texture = pygame.transform.scale(
    pygame.image.load("textures/playerplazmaT.png"), (40, 40)
)

player_plazma_down_texture = pygame.transform.scale(
    pygame.image.load("textures/playerplazmaB.png"), (40, 40)
)

# player texture with gun and shield adaptate to player direction
player_plazma_left_shield_texture = pygame.transform.scale(
    pygame.image.load("textures/playerpalzmaLS.png"), (40, 40)
)

player_plazma_right_shield_texture = pygame.transform.scale(
    pygame.image.load("textures/playerpalzmaPS.png"), (40, 40)
)

player_plazma_top_shield_texture = pygame.transform.scale(
    pygame.image.load("textures/playerplazmaTS.png"), (40, 40)
)

player_plazma_down_shield_texture = pygame.transform.scale(
    pygame.image.load("textures/playerpalzmaDS.png"), (40, 40)
)

# player dead animation
player_dead_animation = [
    pygame.image.load("textures/playerdead1.png"),
    pygame.image.load("textures/playerdead2.png"),
    pygame.image.load("textures/playerdead3.png"),
]

# last player texture
last_texture = player1_texture
# last player texture with shield
last_texture_with_shield = player1_texture

# bullet speed
bullet_speed = 70
# basic bullet direction
bullet_direction = "right"
# flag checks a bullet are shooted
bullet_fired = True
# bullet right,left size
bullet_width = 15
bullet_height = 5
# bullet top,down size
bullet2_width = 5
bullet2_height = 15

# bullet textures adaptate to bullet direction
bullet_texture_right = pygame.transform.scale(
    pygame.image.load("textures/bulletR.png"), (bullet_width, bullet_height)
)

bullet_textureL = pygame.transform.scale(  # noqa: N816
    pygame.image.load("textures/bulletL.png"), (bullet_width, bullet_height)
)

bullet_textureT = pygame.transform.scale(  # noqa: N816
    pygame.image.load("textures/bulletT.png"), (bullet2_width, bullet2_height)
)

bullet_textureD = pygame.transform.scale(  # noqa: N816
    pygame.image.load("textures/bulletD.png"), (bullet2_width, bullet2_height)
)

# bullet explosion textures
bullet_boom1_texture = pygame.transform.scale(
    pygame.image.load("textures/bulletboom1.png"), (20, 20)
)

bullet_boom2_texture = pygame.transform.scale(
    pygame.image.load("textures/bulletboom2.png"), (20, 20)
)

bullet_boom3_texture = pygame.transform.scale(
    pygame.image.load("textures/bulletboom3.png"), (20, 20)
)

# bullet explosion animation
bullet_boom_list = [bullet_boom1_texture, bullet_boom2_texture, bullet_boom3_texture]

# monsters textures

# devil size
devil_width = 50
devil_height = 50
# devil speed
devil_speed = 6
# devil collision parametr
devil_collision = 50
# devil texture
devil_texture = pygame.transform.scale(
    pygame.image.load("textures/enemy.png"), (devil_width, devil_height)
)
# devil rect
devil_rect = devil_texture.get_rect()
# devil death animation (killed by shield)
devil_dead_animation = [
    pygame.transform.scale(
        pygame.image.load("textures/devildead1.png"), (devil_width, devil_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/devildead2.png"), (devil_width, devil_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/devildead3.png"), (devil_width, devil_height)
    ),
]
# devil death animation (killed by gun)
devil_bullet_dead_animation = [
    pygame.transform.scale(
        pygame.image.load("textures/devildead1v2.png"), (devil_width, devil_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/devildead2v2.png"), (devil_width, devil_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/devildead3v2.png"), (devil_width, devil_height)
    ),
]
# devil corpses texture (killed by gun)
devil_bullet_corpses = pygame.transform.scale(
    pygame.image.load("textures/devildead3v2.png"), (devil_width, devil_height)
)
# devil corpses texture (killed by shield)
devil_shield_corpses = pygame.transform.scale(
    pygame.image.load("textures/devildead3.png"), (devil_width, devil_height)
)

# fast size
fast_width = 40
fast_height = 40
# fast speed
fast_speed = 15
# fast collision parametr
fast_collison = 40
# fast texture
fast_texture = pygame.transform.scale(
    pygame.image.load("textures/fast.png"), (fast_width, fast_height)
)
# fast rect
fast_rect = fast_texture.get_rect()
# fast death animation (killed by shield)
fast_dead_animation = [
    pygame.transform.scale(
        pygame.image.load("textures/fastdead1.png"), (fast_width, fast_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/fastdead2.png"), (fast_width, fast_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/fastdead3.png"), (fast_width, fast_height)
    ),
]
# fast death animation (killed by gun)
fast_bullet_dead_animation = [
    pygame.transform.scale(
        pygame.image.load("textures/fastdead1v2.png"), (fast_width, fast_height)
    ),
    pygame.transform.scale(pygame.image.load("textures/fastdead2v2.png"), (60, 60)),
    pygame.transform.scale(pygame.image.load("textures/fastdead3v2.png"), (60, 60)),
]
# fast corpses texture
fast_corpses = pygame.transform.scale(
    pygame.image.load("textures/fastdead3v2.png"), (100, 100)
)

# mutant size
mutant_width = 100
mutant_height = 100
# mutant speed
mutant_speed = 3
# mutant collision parametr
mutant_collision = 100
# mutant texture left direction
mutant_texture_left_direction = pygame.transform.scale(
    pygame.image.load("textures/mutantL.png"), (mutant_width, mutant_height)
)
# mutant texture right direction
mutant_texture_right_direction = pygame.transform.scale(
    pygame.image.load("textures/mutantR.png"), (mutant_width, mutant_height)
)
# mutant rect
mutant_rect = mutant_texture_left_direction.get_rect()
# mutant corpses (killed by gun)
mutant_bullet_corpses = pygame.transform.scale(
    pygame.image.load("textures/mutantdead3L.png"), (mutant_width, mutant_height)
)
# mutant corpses (killed by shield)
mutant_shield_corpses = pygame.transform.scale(
    pygame.image.load("textures/mutantL.dead3v3.png"), (mutant_width, mutant_height)
)
# mutant death animation (killed by shield)
mutant_bullet_dead_animation = [
    pygame.transform.scale(
        pygame.image.load("textures/mutantdead1L.png"), (mutant_width, mutant_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/mutantdead2L.png"), (mutant_width, mutant_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/mutantdead3L.png"), (mutant_width, mutant_height)
    ),
]
# mutant death animation (killed by gun)
mutant_shield_dead_animation = [
    pygame.transform.scale(
        pygame.image.load("textures/mutantL.dead1v3.png"), (mutant_width, mutant_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/mutantL.dead2v3.png"), (mutant_width, mutant_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/mutantL.dead3v3.png"), (mutant_width, mutant_height)
    ),
]

# ghost size
ghost_width = 50
ghost_height = 50
# ghost speed
ghost_speed = 10
# ghost collision parametr
ghost_collision = 50
# ghost texture left direction
ghost_texture_left_direction = pygame.transform.scale(
    pygame.image.load("textures/ghostL.png"), (ghost_width, ghost_height)
)
# ghost texture right direction
ghost_texture_right_direction = pygame.transform.scale(
    pygame.image.load("textures/ghostR.png"), (ghost_width, ghost_height)
)
# ghost rect
ghost_rect = ghost_texture_left_direction.get_rect()
# ghost death animation
ghost_dead_animation = [
    pygame.transform.scale(
        pygame.image.load("textures/ghostdead1L.png"), (ghost_width, ghost_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/ghostdead2L.png"), (ghost_width, ghost_height)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/ghostdead3L.png"), (ghost_width, ghost_height)
    ),
]
# ghost corpses
ghost_corpses = pygame.transform.scale(
    pygame.image.load("textures/ghostdead3L.png"), (ghost_width, ghost_height)
)

# boss texture
boss_texture = pygame.transform.scale(
    pygame.image.load("textures/boss.png"), (300, 300)
)
# boss rect
boss_rect = boss_texture.get_rect()
# boss death animation
boss_dead_animation = [
    pygame.transform.scale(pygame.image.load("textures/bossdead1.png"), (300, 300)),
    pygame.transform.scale(pygame.image.load("textures/bossdead2.png"), (300, 300)),
    pygame.transform.scale(pygame.image.load("textures/bossdead3.png"), (300, 300)),
]
# boss corpses
boss_corpses = pygame.transform.scale(
    pygame.image.load("textures/bossdead3c.png"), (300, 300)
)

# obstacles textures

# tree size
tree_width = 70
tree_height = 100
# tree texture
tree_texture = pygame.transform.scale(
    pygame.image.load("textures/drzewo.png"), (tree_width, tree_height)
)
# tree rect
tree_rect = tree_texture.get_rect()

# stone size
stone_width = 50
stone_height = 50
# stone texture
stone_texture = pygame.transform.scale(
    pygame.image.load("textures/kamien.png"), (stone_width, stone_height)
)
# stone rect
stone_rect = stone_texture.get_rect()

# bush size
bush_width = 40
bush_height = 40
# bush texture
bush_texture = pygame.transform.scale(
    pygame.image.load("textures/krzak.png"), (bush_width, bush_height)
)
# bush rect
bush_rect = bush_texture.get_rect()

# bones size
bones_width = 70
bones_height = 30
# bones texture
bones_texture = pygame.transform.scale(
    pygame.image.load("textures/bones.png"), (bones_width, bones_height)
)
# bones rect
bones_rect = bones_texture.get_rect()

# sarna size
animal_width = 50
animal_height = 30
# sarna texture
animal_texture = pygame.transform.scale(
    pygame.image.load("textures/sarna.png"), (animal_width, animal_height)
)
# sarna rect
animal_rect = animal_texture.get_rect()

# dead tree size
dead_tree_width = 70
dead_tree_height = 100
# dead tree texture
dead_tree_texture = pygame.transform.scale(
    pygame.image.load("textures/deadtree.png"), (dead_tree_width, dead_tree_height)
)
# dead tree rect
dead_tree_rect = dead_tree_texture.get_rect()

# obstacle destruction animation
obstacle_destroy_animation = [
    pygame.transform.scale(
        pygame.image.load("textures/destroyednature1.png"), (50, 50)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/destroyednature2.png"), (50, 50)
    ),
    pygame.transform.scale(
        pygame.image.load("textures/destroyednature3.png"), (50, 50)
    ),
]
# destroyed obstacle texture
destroyed_obstacle_texture = pygame.transform.scale(
    pygame.image.load("textures/destroyednature3.png"), (50, 50)
)


# sounds

intro_sound = pygame.mixer.Sound("sounds/intro.mp3")
# steps sound
steps_sound = pygame.mixer.Sound("sounds/kroki.mp3")
# next level sound
next_level_sound = pygame.mixer.Sound("sounds/pickup.mp3")
# earn gold sound
gold_sound = pygame.mixer.Sound("sounds/gold.mp3")
# death sounds
player_death_sound = pygame.mixer.Sound("sounds/playerdead.mp3")
devil_death_sound = pygame.mixer.Sound("sounds/devildead.mp3")
devil_death_sound.set_volume(0.5)
fast_death_sound = pygame.mixer.Sound("sounds/fastdead.mp3")
fast_death_sound.set_volume(0.3)
mutant_death_sound = pygame.mixer.Sound("sounds/mutantdead.mp3")
ghost_death_sound = pygame.mixer.Sound("sounds/ghostdead.mp3")
boss_death_sound = pygame.mixer.Sound("sounds/boss_death.mp3")
# obstacle destruction sound
destruction_sound = pygame.mixer.Sound("sounds/destruction.mp3")
destruction_sound.set_volume(0.2)
boss_death_sound.set_volume(0.2)
# immersive mounsters sounds (playing when player is close to monster)
monsters1_sound = pygame.mixer.Sound("sounds/monsters.mp3")
monsters1_sound.set_volume(0.5)
monsters2_sound = pygame.mixer.Sound("sounds/monsters2.mp3")
monsters2_sound.set_volume(0.5)
monsters_sounds = [monsters1_sound, monsters2_sound]
# boss sound
boss_sound = pygame.mixer.Sound("sounds/boss_sound.mp3")
boss_sound.set_volume(0.5)
# pick/hide gun sound
gun_sound = pygame.mixer.Sound("sounds/gunsound.mp3")
gun_sound.set_volume(0.6)
# buy ammo sound
reload_sound = pygame.mixer.Sound("sounds/reload.mp3")
reload_sound.set_volume(0.2)
# buy speed boost sound
speed_sound = pygame.mixer.Sound("sounds/speed.mp3")
speed_sound.set_volume(0.5)
# bouy shield sound
shield_sound = pygame.mixer.Sound("sounds/shield.mp3")
shield_sound.set_volume(0.5)
# buy refresh sound
refresh_sound = pygame.mixer.Sound("sounds/refresh.mp3")
refresh_sound.set_volume(0.5)


# playing sound only when nothing is playing
def play_sound(sound: Any) -> None:
    if not pygame.mixer.get_busy():
        sound.play()


# stop sound
def stop_sound(sound: Any) -> None:
    sound.stop()


# game intro
def start() -> None:
    # shows all intro slaids and play intro music refresh screen beetween intro slaids
    window.blit(olchastudio, (1, 1))
    intro_sound.play()
    pygame.display.update()
    time.sleep(4.4)
    window.blit(intro1, (1, 1))
    pygame.display.update()
    time.sleep(2.4)
    window.blit(intro2, (1, 1))
    pygame.display.update()
    time.sleep(4.6)
    window.blit(intro3, (1, 1))
    pygame.display.update()
    time.sleep(4)
    window.blit(menu, (1, 1))
    pygame.display.update()
    waiting = True
    # game was started when player press space
    while waiting:
        play_sound(intro_sound)
        for _ in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                waiting = False
                stop_sound(intro_sound)


# deadscreen
def deadscreen(  # noqa: PLR0913
    level: int,
    points_counter: int,
    number_devils: int,
    number_fasts: int,
    number_mutants: int,
    number_ghosts: int,
    number_obstacles: int,
    powershield: Any,
    speed: int,
    magazine: int,
    background: pygame.Surface,
    gun_on: Any
) -> int | Any | pygame.Surface:
    waiting = True
    w8 = True
    # load end of the game screen
    window.blit(end_texture, (0, 0))
    pygame.display.update()
    time.sleep(2)
    # load dead screen and show player score
    window.blit(dead_screen, (0, 0))
    dead_screen_font = pygame.font.Font("font/snap.ttf", 100)
    # show best score
    file_path = Path("best_score.txt")
    with file_path.open(mode="r") as f:
        best_score = int(f.read())
    # update best score if you have more points and show best score on sreen
    if level > best_score:
        file_path = Path("best_score.txt")
        with file_path.open(mode="w") as f:
            f.write(str(level))
        points2_text = dead_screen_font.render(
            f"Your record {level} levels", True, (255, 0, 0)  # noqa: FBT003
        )
        window.blit(points2_text, (window_width / 4 - 80, window_height / 4 + 100))
    else:
        points2_text = dead_screen_font.render(
            f"Your record: {best_score} levels", True, (255, 0, 0)  # noqa: FBT003
        )
        window.blit(points2_text, (window_width / 4 - 80, window_height / 4 + 100))
    # show your actual score
    points_text = dead_screen_font.render(
        f"You survived: {level} levels", True, (255, 0, 0)  # noqa: FBT003
    )
    window.blit(points_text, (window_width / 4 - 80, window_height / 4))
    pygame.display.update()
    # when player press space stop showing scores and go into menu
    while waiting:  # noqa: RET503
            for _ in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    waiting = False
                    window.blit(menu, (1, 1))
                    pygame.display.update()
                    # when player press space game was started again
                    while w8:
                        for _ in pygame.event.get():
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_SPACE]:
                                time.sleep(0.5)
                                # reset all stats
                                points_counter = 0
                                number_devils = 0
                                number_fasts = 0
                                number_mutants = 0
                                number_ghosts = 0
                                number_obstacles = 8
                                powershield = False
                                background = background1
                                speed = 8
                                level = 0
                                gun_on = False
                                magazine = 0
                                w8 = False
                                right.color = (255, 0, 0)
                                pygame.display.update()
                                return (
                                    level,
                                    points_counter,
                                    number_devils,
                                    number_fasts,
                                    number_mutants,
                                    number_ghosts,
                                    number_obstacles,
                                    powershield,
                                    speed,
                                    magazine,
                                    background,
                                    gun_on,
                                )
                # if player press escape the game is closed
                elif keys[pygame.K_ESCAPE]:
                    sys.exit()


def pause() -> None:
    pause_window = pygame.image.load("textures/pause_window.png")
    pause_window = pygame.transform.scale(pause_window, window.get_size())
    waiting = True
    while waiting:
        window.blit(pause_window, (1, 1))
        pygame.display.update()
        for _ in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                waiting = False
                time.sleep(0.5)


# if obstacles/enemies colliderect with other or with player generete new x and y
def collision(
    lista: list, rect: pygame.Rect, x: int, y: int
) -> tuple[Any | int, Any | int]:
    collision = True
    while collision:
        collision = False
        for objects in lista:
            if rect.move(x, y).colliderect(objects.rect) or rect.move(x, y).colliderect(
                player1_rect
            ):
                collision = True
                break
            if math.dist((x, y), player1_rect.center) < 200:
                collision = True
                break
        if collision:
            if lista == obstacles_list:
                x = random.randint(50, window_width - 50)  # noqa: S311
                y = random.randint(50, window_height - 50)  # noqa: S311
            else:
                x = random.randint(150, window_width - 150)  # noqa: S311
                y = random.randint(150, window_height - 150)  # noqa: S311
    return x, y


# loading objects in the map:enemies,obstacles,corpses etc
def load(quantity: int, objectt: Any, lista: list, rect: pygame.Rect) -> None:
    for obj in range(quantity):
        if lista == obstacles_list:
            if background in (background1, background3, background5):
                x = random.randint(20, window_width - 20)  # noqa: S311 # type: ignore
                y = random.randint(20, window_height - 20)  # noqa: S311
            elif background == background2:
                # obstacles dont spawn on skull
                x = random.randint(20, window_width - 90)  # noqa: S311
                y = random.randint(20, window_height - 150)  # noqa: S311
        else:
            x = random.randint(20, window_width - 20)  # noqa: S311
            y = random.randint(20, window_height - 20)  # noqa: S311

        if lista == enemy_list and obj == "mutant":
            x = random.randint(200, window_width - 200)  # noqa: S311
            y = random.randint(200, window_height - 200)  # noqa: S311
        else:
            x = random.randint(100, window_width - 100)  # noqa: S311
            y = random.randint(100, window_height - 100)  # noqa: S311

        # in boss level are no obstacles and number of enemies are static
        if background != background4:
            x, y = collision(lista, rect, x, y)  # type: ignore
            objectt(x, y)
        else:
            # additional security for crash if no enemies in this moment
            x = random.randint(100, window_width - 100)  # noqa: S311
            y = random.randint(100, window_height - 100)  # noqa: S311
            x, y = collision(lista, rect, x, y)
            objectt(x, y)


# pick your gun
def pick_gun() -> None:
    gun_sound.play()
    shield_banner = pygame.transform.scale(
        pygame.image.load("textures/gunpick.png"), (300, 200)
    )
    window.blit(shield_banner, (window_width / 2 - 140, window_height / 2 - 140))
    pygame.display.update()
    time.sleep(0.5)


# hide your gun
def hide_gun() -> None:
    gun_sound.play()
    shield_banner = pygame.transform.scale(
        pygame.image.load("textures/gunhide.png"), (300, 200)
    )
    window.blit(shield_banner, (window_width / 2 - 140, window_height / 2 - 140))
    pygame.display.update()
    time.sleep(0.5)


# boost your speed when you have less than 15
def speed_boost() -> None:
    speed_boost_banner = pygame.transform.scale(
        pygame.image.load("textures/turbo.png"), (300, 200)
    )
    max_speed_banner = pygame.transform.scale(
        pygame.image.load("textures/maxspeed.png"), (300, 200)
    )
    if speed < 15:
        speed_sound.play()
        window.blit(
            speed_boost_banner, (window_width / 2 - 140, window_height / 2 - 140)
        )
    else:
        window.blit(max_speed_banner, (window_width / 2 - 140, window_height / 2 - 140))
    pygame.display.update()
    time.sleep(1)


# load new obstacles on the map
def refresh(level: int, points_counter: int, gold_list: list[Any]) -> int:
    refresh_sound.play()
    refresh_banner = pygame.transform.scale(
        pygame.image.load("textures/refresh.png"), (300, 200)
    )
    window.blit(refresh_banner, (window_width / 2 - 140, window_height / 2 - 140))
    generate_new_obstacles(obstacles_list)
    gold_list = generate_new_gold(gold_list)
    points_counter -= 1
    level -= 1
    pygame.display.update()
    time.sleep(1)
    return level, points_counter, gold_list


# activating your shield
def shield() -> None:
    shield_sound.play()
    shield_banner = pygame.transform.scale(
        pygame.image.load("textures/shield.png"), (300, 200)
    )
    window.blit(shield_banner, (window_width / 2 - 140, window_height / 2 - 140))
    pygame.display.update()
    time.sleep(1)


# buying ammunition
def reeload(magazine: int, points_counter: int) -> int:
    reload_sound.play()
    reload_banner = pygame.transform.scale(
        pygame.image.load("textures/reload.png"), (300, 200)
    )
    window.blit(reload_banner, (window_width / 2 - 140, window_height / 2 - 140))
    magazine += 20
    points_counter -= 2
    pygame.display.update()
    time.sleep(1)
    return magazine, points_counter


# border class
class Border:
    def __init__(  # noqa: PLR0913
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Any = (255, 0, 0),
    ) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)


# add borders to border list
def borders(borders_list: list[Any]) -> list[Any]:
    up = Border(1, 1, window_width, 1)
    borders_list.append(up)

    down = Border(1, window_height - 1, window_width, 1)
    borders_list.append(down)

    left = Border(1, 1, 1, window_height)
    borders_list.append(left)
    # default is red but when player earn gold change color to green
    right = Border(window_width - 1, 1, 1, window_height, (255, 0, 0))
    borders_list.append(right)

    return borders_list, right


borders_list, right = borders(borders_list)


# obstacle class
class Obstacle:
    def __init__(  # noqa: PLR0913
        self, x: int, y: int, width: int, height: int, texture: Any
    ) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture
        self.mask = pygame.mask.from_surface(texture)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.texture, self.rect)

    """when player destroy obstacle save possition to destroyed
    obstacles list to load destroyed obstacle texture in the same possition"""

    def delete(self) -> None:
        destroyed_obstacles_list.append(self)
        obstacles_list.remove(self)
        del self


# add obstacles to obstacles list
def obstacles(obstacles_list: list[Any]) -> list[Any]:  # noqa: C901
    def tree(xtree: int, ytree: int) -> None:
        tree = Obstacle(xtree, ytree, tree_width, tree_height, tree_texture)
        obstacles_list.append(tree)

    def stone(xstone: int, ystone: int) -> None:
        stone = Obstacle(xstone, ystone, stone_width, stone_height, stone_texture)
        obstacles_list.append(stone)

    def bush(xbush: int, ybush: int) -> None:
        bush = Obstacle(xbush, ybush, bush_width, bush_height, bush_texture)
        obstacles_list.append(bush)

    def bones(xbones: int, ybones: int) -> None:
        bones = Obstacle(xbones, ybones, bones_width, bones_height, bones_texture)
        obstacles_list.append(bones)

    def animal(xanimal: int, yanimal: int) -> None:
        animal = Obstacle(xanimal, yanimal, animal_width, animal_height, animal_texture)
        obstacles_list.append(animal)

    def deadtree(xdeadtree: int, ydeadtree: int) -> None:
        deadtree = Obstacle(
            xdeadtree, ydeadtree, dead_tree_width, dead_tree_height, dead_tree_texture
        )
        obstacles_list.append(deadtree)

    # load obstacles in the map without background 4
    if background == background1:
        load(number_obstacles, tree, obstacles_list, tree_rect)
        load(number_obstacles - 4, animal, obstacles_list, animal_rect)
        load(number_obstacles - 2, bush, obstacles_list, bush_rect)
        load(number_obstacles - 6, stone, obstacles_list, stone_rect)

    if background == background2:
        load(number_obstacles, deadtree, obstacles_list, dead_tree_rect)
        load(number_obstacles - 2, bones, obstacles_list, bones_rect)
        load(number_obstacles - 1, stone, obstacles_list, stone_rect)
        load(number_obstacles - 2, animal, obstacles_list, animal_rect)

    if background == background3:
        load(number_obstacles + 1, deadtree, obstacles_list, dead_tree_rect)
        load(number_obstacles + 1, bones, obstacles_list, bones_rect)
        load(number_obstacles - 2, animal, obstacles_list, animal_rect)
    if background == background4:
        pass
    if background == background5:
        load(number_obstacles - 6, deadtree, obstacles_list, dead_tree_rect)
        load(number_obstacles - 3, bones, obstacles_list, bones_rect)
        load(number_obstacles - 3, animal, obstacles_list, animal_rect)

    return obstacles_list


obstacles_list = obstacles(obstacles_list)


# enemy class
class Enemy:
    def __init__(  # noqa: PLR0913
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        texture: Any,
        speed: int,
        collision: Any,
        enemy_type: str,
    ) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture
        self.speed = speed
        self.collision = collision
        self.direction = (1, 0)
        self.type = enemy_type
        self.mask = pygame.mask.from_surface(texture)
        self.prev_pos = self.rect.copy()
        self.x = self.rect.x
        self.y = self.rect.y

    """enemies colliderete with obstacles and borders
    (ghost dont colliderect with obstacles) when the enemy touch
    obstacle he returns to his previous position"""

    def update(self, obstacles_list: list[Any]) -> None:
        self.prev_pos = self.rect.copy()
        self.x, self.y = self.rect.x, self.rect.y
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        for obstacles in obstacles_list:
            if self.type == "ghost":
                continue
            if self.rect.colliderect(obstacles.rect):
                self.rect = self.prev_pos
                break

        for borders in borders_list:
            if self.rect.colliderect(borders.rect):
                self.rect = self.prev_pos
                break

        if random.random() < 0.05:  # noqa: S311
            self.change_direction()

    # enemies are moving randomly
    def change_direction(self) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        new_direction = self.direction
        while new_direction == self.direction:
            new_direction = random.choice(directions)  # noqa: S311
        self.direction = new_direction

    # enemies with left and right texture change textures when change direction
    def mirror(self, left: Any, right: Any) -> None:
        self.left = left
        self.right = right
        new_direction = self.direction
        if self.type in ("mutant", "ghost"):
            if new_direction == (1, 0):
                self.texture = right
            elif new_direction == (-1, 0):
                self.texture = left

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.texture, self.rect)

    """when player destroy enemy save possition to dead enemy list
    to load enemy corpses texture in the same possition"""

    def delete(self) -> None:
        dead_enemy_list.append(self)
        enemy_list.remove(self)
        del self


# add enemies to enemy list
def enemies() -> list[Any]:  # noqa: C901
    enemy_list = []

    def devil(xdevil: int, ydevil: int) -> None:
        devil = Enemy(
            xdevil,
            ydevil,
            devil_width,
            devil_height,
            devil_texture,
            devil_speed,
            devil_collision,
            "devil",
        )
        enemy_list.append(devil)

    def fast(xfast: int, yfast: int) -> None:
        fast = Enemy(
            xfast,
            yfast,
            fast_width,
            fast_height,
            fast_texture,
            fast_speed,
            fast_collison,
            "fast",
        )
        enemy_list.append(fast)

    def mutant(xmutant: int, ymutant: int) -> None:
        mutant = Enemy(
            xmutant,
            ymutant,
            mutant_width,
            mutant_height,
            mutant_texture_left_direction,
            mutant_speed,
            mutant_collision,
            "mutant",
        )
        enemy_list.append(mutant)

    def ghost(xghost: int, yghost: int) -> None:
        ghost = Enemy(
            xghost,
            yghost,
            ghost_width,
            ghost_height,
            ghost_texture_left_direction,
            ghost_speed,
            ghost_collision,
            "ghost",
        )
        enemy_list.append(ghost)

    # load different enemies on different levels
    if background != background4:
        if level % 5 == 0:
            load(number_ghosts, ghost, obstacles_list, ghost_rect)
        elif level % 4 == 0:
            load(number_fasts, fast, obstacles_list, fast_rect)
        elif level % 3 == 0:
            load(number_mutants, mutant, obstacles_list, mutant_rect)
        else:
            load(number_devils, devil, obstacles_list, devil_rect)

    # boss level have static number of enemies
    if background == background4:
        if boss_hp == 40:
            load(10, devil, enemy_list, devil_rect)
            load(5, mutant, enemy_list, mutant_rect)
        if boss_hp == 30:
            load(6, mutant, enemy_list, mutant_rect)
            load(7, ghost, enemy_list, ghost_rect)
            load(5, devil, enemy_list, devil_rect)
        if boss_hp == 20:
            load(10, fast, enemy_list, fast_rect)
            load(10, mutant, enemy_list, mutant_rect)
        if boss_hp == 10:
            load(40, devil, enemy_list, devil_rect)

    return enemy_list


enemy_list = enemies()


# bullet class
class Bullet:
    def __init__(  # noqa: PLR0913
        self,
        x: int,
        y: int,
        speed: int,
        bullet_width: int,
        bullet_height: int,
        direction: Any,
        texture: Any,
    ) -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.texture = texture
        self.bullet_height = bullet_height
        self.bullet_width = bullet_width
        self.rect = pygame.Rect(x, y, bullet_width, bullet_height)

    # changes the texture according to the direction of the bullet
    def update(self) -> None:
        if self.direction == "left":
            self.rect.move_ip(-self.speed, 0)

        elif self.direction == "right":
            self.rect.move_ip(self.speed, 0)

        elif self.direction == "top":
            self.rect.move_ip(0, -self.speed)

        elif self.direction == "down":
            self.rect.move_ip(0, self.speed)

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.texture, (self.rect.x, self.rect.y))

    def delete(self) -> None:
        bullets_list.remove(self)
        del self


# boss class
class Boss:
    def __init__(  # noqa: PLR0913
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        texture: Any,
        speed: int,
        collision: Any,
    ) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture
        self.speed = speed
        self.collision = collision
        self.direction = (1, 0)
        self.mask = pygame.mask.from_surface(texture)
        self.prev_pos = self.rect.copy()
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self) -> None:
        self.prev_pos = self.rect.copy()
        self.x, self.y = self.rect.x, self.rect.y
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        for borders in borders_list:
            if self.rect.colliderect(borders.rect):
                self.rect = self.prev_pos
                break
        # enemy colliderect with boss
        for enemies in enemy_list:
            offset = (self.rect.x - enemies.x, self.rect.y - enemies.y)
            if enemies.mask.overlap(mask, offset):
                enemies.rect = enemies.prev_pos

        if random.random() < 0.05:  # noqa: S311
            self.change_direction()

    def change_direction(self) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        new_direction = self.direction
        while new_direction == self.direction:
            new_direction = random.choice(directions)  # noqa: S311
        self.direction = new_direction

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.texture, self.rect)

    def delete(self) -> None:
        boss_list.remove(self)
        dead_boss_list.append(self)
        del self


# add boss to boss list
def boss(boss_list: list, bs: Any) -> list[Any]:
    boss = Boss(500, 500, 300, 300, boss_texture, 10, 300)
    boss_list.append(boss)
    bs = True
    return boss_list, bs


# creating gold in map and modify levels
def points(gold_list: list[Any]) -> list[Any]:
    # gold list
    # gold size
    gold_width = 20
    gold_height = 20
    # gold texture
    gold_texture = pygame.transform.scale(
        pygame.image.load("textures/gold.png"), (gold_width, gold_height)
    )
    # gold rect
    gold_rect = gold_texture.get_rect()

    def gold(xgold: int, ygold: int) -> None:
        global number_devils  # noqa: PLW0603
        global number_fasts  # noqa: PLW0603
        global number_mutants  # noqa: PLW0603
        global number_obstacles  # noqa: PLW0603
        global number_ghosts  # noqa: PLW0603
        global level  # noqa: PLW0603
        # create gold
        gold = Obstacle(xgold, ygold, gold_width, gold_height, gold_texture)
        gold_list.append(gold)
        # play next level sound
        if level != 0:
            next_level_sound.play()
        # delete corpses and destroyed obstacles in next level
        dead_enemy_list.clear()
        destroyed_obstacles_list.clear()
        # make levels harder
        level += 1
        if number_obstacles <= max_obstacles:
            number_obstacles += 1
        if level % 2 == 0:
            number_devils += 1
        if level % 3 == 0:
            number_mutants += 1
        if level % 4 == 0:
            number_fasts += 1
        if level % 5 == 0:
            number_ghosts += 1

    # in boss level gold dont spawn
    if background != background4:
        load(1, gold, obstacles_list, gold_rect)
    return gold_list


gold_list = points(gold_list)


# clear old list and load new
def generate_new_obstacles(obstacles_list: list[Any]) -> None:
    obstacles_list.clear()
    dead_boss_list.clear()
    return obstacles(obstacles_list)


# clear old list and load new
def generate_new_gold(gold_list: list[Any]) -> None:
    gold_list.clear()
    return points(gold_list)


# update list (dont clear it)
def generate_new_enemy() -> list[Any]:
    return enemies()


# load death animation
def death_animation(death_frames: list[Any], x: int, y: int) -> None:
    for frames in death_frames:
        window.blit(frames, (x, y))
        pygame.time.wait(50)
        pygame.display.update()


# load corpses on screen, adapts to enemy type and way of death
def corpses() -> None:  # noqa: C901
    for enemy in dead_enemy_list:
        if enemy.killed_by == "bullet":
            if enemy.type == "devil":
                window.blit(devil_bullet_corpses, (enemy.rect.x, enemy.rect.y))
            if enemy.type == "mutant":
                window.blit(mutant_bullet_corpses, (enemy.rect.x, enemy.rect.y))

        if enemy.killed_by == "shield":
            if enemy.type == "devil":
                window.blit(devil_shield_corpses, (enemy.rect.x, enemy.rect.y))
            if enemy.type == "mutant":
                window.blit(mutant_shield_corpses, (enemy.rect.x, enemy.rect.y))

        if enemy.type == "ghost":
            window.blit(ghost_corpses, (enemy.rect.x, enemy.rect.y))
        if enemy.type == "fast":
            window.blit(fast_corpses, (enemy.rect.x - 20, enemy.rect.y - 20))

    for boss in dead_boss_list:
        window.blit(boss_corpses, (boss.rect.x, boss.rect.y))

    for obstacle in destroyed_obstacles_list:
        scaled_corpse = pygame.transform.scale(
            destroyed_obstacle_texture, (obstacle.rect.width, obstacle.rect.height)
        )
        window.blit(scaled_corpse, (obstacle.rect.x, obstacle.rect.y))


# showing on screen level,points,bullets and boss hp on boss lvl
def status(boss_hp: int) -> None:
    font = pygame.font.Font("font/snap.ttf", 30)
    points_text = font.render(f"Gold: {points_counter}", True, (255, 0, 0))  # noqa: FBT003, E501
    window.blit(points_text, (window_width - 170, 10))
    points_text = font.render(f"Level: {level}", True, (255, 0, 0))# noqa: FBT003
    window.blit(points_text, (20, 10))
    points_text = font.render(f"Bullets: {magazine}", True, (255, 0, 0))# noqa: FBT003
    window.blit(points_text, (window_width // 2.3, 10))
    # boss HP is the letter l at the bottom of the screen, which decreases
    # in multiples depending on his health
    if background == background4:
        boss_hp_str = "l" * boss_hp
        boss_hp_text = font.render(boss_hp_str, True, (255, 0, 0))# noqa: FBT003
        window.blit(boss_hp_text, (window_width // 3, window_height - 80))



# load start od the game and play game music
start()
pygame.mixer.music.load("sounds/music.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# main loop
run = True
while run:
    # game have 60fps
    pygame.time.Clock().tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # click on x in window or escape ending the game
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            run = False

    # parametr to add or subtract player x and y
    xx, yy = 0, 0
    # when player press movement button he change the possition,
    # steps sound are playing and bullet direction is changing
    if keys[pygame.K_d]:
        play_sound(steps_sound)
        xx += speed
        bullet_direction = "right"
    elif keys[pygame.K_a]:
        play_sound(steps_sound)
        xx -= speed
        bullet_direction = "left"
    elif keys[pygame.K_s]:
        play_sound(steps_sound)
        yy += speed
        bullet_direction = "down"
    elif keys[pygame.K_w]:
        play_sound(steps_sound)
        yy -= speed
        bullet_direction = "top"
    else:
        stop_sound(steps_sound)

    # save last player possition and load it when player colliderete with something
    prev_pos = player1_rect.copy()
    player1_rect.move_ip(xx, yy)
    x, y = player1_rect.x, player1_rect.y

    # check collision with obstacles
    for obstacle in obstacles_list:
        mask = obstacle.mask
        offset = (obstacle.rect.x - player1_rect.x, obstacle.rect.y - player1_rect.y)
        if player1_mask.overlap(mask, offset):
            player1_rect = prev_pos
            x, y = player1_rect.x, player1_rect.y
            break

    # checking for collisions with borders (borders dont have masks,
    # so checking for collisions with them looks different)
    for border in borders_list:
        if player1_rect.colliderect(border):
            if border == borders_list[0]:
                y = border.rect.top + 5
            elif border == borders_list[1]:
                y = border.rect.bottom - 40
            elif border == borders_list[2]:
                x = border.rect.left + 5
            if right.color == (255, 0, 0) and border == borders_list[3]:
                x = border.rect.right - 40

    # abilities events pressed and released is for eliminate double click
    if keys[pygame.K_o]:
        if o_key_released and points_counter > 0:
            o_key_pressed = True
            level, points_counter, gold_list = refresh(level, points_counter, gold_list)
            o_key_released = False
        else:
            o_key_pressed = False
            o_key_released = True

    if keys[pygame.K_i]:
        if i_key_released and points_counter >= 3:
            i_key_pressed = True
            shield()
            points_counter -= 3
            powershield = True
            i_key_released = False
        else:
            i_key_pressed = False
            i_key_released = True

    if keys[pygame.K_p]:
        if p_key_released and speed <= max_speed and points_counter >= 2:
            p_key_pressed = True
            speed_boost()
            speed += 1
            points_counter -= 2
        elif speed == max_speed:
            speed_boost()
            p_key_released = False
        else:
            p_key_pressed = False
            p_key_released = True

    if keys[pygame.K_m]:
        if m_key_released:
            m_key_pressed = True
            pause()
            m_key_released = False
        else:
            m_key_pressed = False
            m_key_released = True

    if keys[pygame.K_u]:
        if u_key_released and points_counter >= 2:
            u_key_pressed = True
            magazine, points_counter = reeload(magazine, points_counter)
            u_key_released = False
        else:
            u_key_pressed = False
            u_key_released = True

    if keys[pygame.K_r]:
        if r_key_released:
            r_key_pressed = True
            r_key_released = False
        else:
            r_key_pressed = False
            r_key_released = True
    # bug protection
    if r_key_pressed:
        if gun_on is False:
            pick_gun()
            gun_on = True
            speed -= 3
            r_key_pressed = False

        elif gun_on is True:
            hide_gun()
            gun_on = False
            speed += 3

    # check collision with gold and change right border color
    for gold in gold_list:
        if player1_rect.colliderect(gold.rect):
            gold_sound.play()
            points_counter += 1
            right.color = (0, 255, 0)
            gold_list.remove(gold)

    # load new level when player touch green border
    # and change player possition to left side to make immersion
    if right.color == (0, 255, 0) and player1_rect.colliderect(right.rect):
        background = random_background()
        obstacles_list = generate_new_obstacles(obstacles_list)
        gold_list = generate_new_gold(gold_list)
        enemy_list = generate_new_enemy()
        bullet_fired = True
        right.color = (255, 0, 0)
        x = 0

    # loading the background
    window.blit(background, (0, 0))

    # load gold on the map
    for gol in gold_list:
        gol.draw(window)
    # load obstacles on the map
    for obj in obstacles_list:
        obj.draw(window)
    # load borders on the map
    for border in borders_list:
        border.draw(window)

    # load corpses on the map
    corpses()

    # loading the boss level
    if background == background4:
        destroyed_obstacles_list.clear()
        dead_enemy_list.clear()
        if x == 0:
            load_boss = True
        if load_boss is True:
            boss_list, bs = boss(boss_list, bs)
            load_boss = False
        if bs is True:
            # playing boss level music
            pygame.mixer.stop()
            pygame.mixer.music.load("sounds/bossfight.mp3")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            bs = False
        # load boss on the map
        for boss in boss_list:
            mask = boss.mask
            offset = (boss.rect.x - player1_rect.x, boss.rect.y - player1_rect.y)
            # play boss sound when player is close to boss
            if (
                abs(player1_rect.x - boss.rect.x) <= 400
                and abs(player1_rect.y - boss.rect.y) <= 400
            ):
                play_sound(boss_death_sound)
            boss.update()
            window.blit(boss.texture, boss.rect)
            if boss_hp == 0:
                # if boss hp go to 0 loading boss death effect
                # and reset number of enemies
                stop_sound(boss_death_sound)
                boss_sound.play()
                boss.delete()
                death_animation(boss_dead_animation, boss.rect.x, boss.rect.y)
                points_counter += 30
                right.color = (0, 255, 0)
                level += 1
                points_counter = 0
                number_devils = 0
                number_fasts = 0
                number_mutants = 0
                number_ghosts = 0
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/music.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
                # load new level when player touch right border after killed boss
                if right.color == (0, 255, 0) and player1_rect.colliderect(right.rect):
                    stop_sound(boss_sound)
                    boss_hp = 50
                    background = random_background()
                    obstacles_list = generate_new_obstacles(obstacles_list)
                    gold_list = generate_new_gold(gold_list)
                    enemy_list = generate_new_enemy()
                    bullet_fired = True
                    right.color = (255, 0, 0)
                    x = 0
            # if player touch boss player are dead
            if player1_mask.overlap(mask, offset):
                player_death_sound.play()
                death_animation(player_dead_animation, x, y)
                time.sleep(1)
                (
                    level,
                    points_counter,
                    number_devils,
                    number_fasts,
                    number_mutants,
                    number_ghosts,
                    number_obstacles,
                    powershield,
                    speed,
                    magazine,
                    background,
                    gun_on,
                ) = deadscreen(
                    level,
                    points_counter,
                    number_devils,
                    number_fasts,
                    number_mutants,
                    number_ghosts,
                    number_obstacles,
                    powershield,
                    speed,
                    magazine,
                    background,
                    gun_on,
                )
                enemy_list = generate_new_enemy()
                gold_list = generate_new_gold(gold_list)
                obstacles_list = generate_new_obstacles(obstacles_list)
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/music.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
                break

    # player textures adapte to shield and gun and direction
    if powershield is False and gun_on is False:
        window.blit(player1_texture, player1_rect)
        player1_rect = pygame.rect.Rect(x, y, 40, 40)

    elif powershield is True and gun_on is False:
        window.blit(player1_texture_shield, player1_rect)
        player1_rect = pygame.rect.Rect(x, y, 40, 40)

    elif powershield is False and gun_on is True:
        if keys[pygame.K_d]:
            window.blit(player_plazma_right_texture, player1_rect)
            last_texture = player_plazma_right_texture
            player1_rect = pygame.rect.Rect(x, y, 40, 40)

        elif keys[pygame.K_a]:
            window.blit(player_plazma_left_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture = player_plazma_left_texture

        elif keys[pygame.K_s]:
            window.blit(player_plazma_down_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture = player_plazma_down_texture

        elif keys[pygame.K_w]:
            window.blit(player_plazma_top_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture = player_plazma_top_texture

        else:
            window.blit(last_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)

    elif powershield is True and gun_on is True:
        if keys[pygame.K_d]:
            window.blit(player_plazma_right_shield_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture_with_shield = player_plazma_right_shield_texture

        elif keys[pygame.K_a]:
            window.blit(player_plazma_left_shield_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture_with_shield = player_plazma_left_shield_texture

        elif keys[pygame.K_s]:
            window.blit(player_plazma_down_shield_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture_with_shield = player_plazma_down_shield_texture

        elif keys[pygame.K_w]:
            window.blit(player_plazma_top_shield_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture_with_shield = player_plazma_top_shield_texture

        else:
            window.blit(last_texture_with_shield, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)

    # show level coins bullets
    status(boss_hp)

    """when player press space and any bullet flying in this moment and
    player have bullets and holds his gun create bullet adapte to bullet direction"""
    if (
        keys[pygame.K_SPACE]
        and bullet_fired is True
        and magazine > 0
        and gun_on is True
    ):
        if bullet_direction == "right":
            new_bullet = Bullet(
                player1_rect.x,
                player1_rect.y,
                bullet_speed,
                bullet_width,
                bullet_height,
                bullet_direction,
                bullet_texture_right,
            )
            bullets_list.append(new_bullet)
            magazine -= 1
            gun_sound.play()

        elif bullet_direction == "left":
            new_bullet = Bullet(
                player1_rect.x,
                player1_rect.y,
                bullet_speed,
                bullet_width,
                bullet_height,
                bullet_direction,
                bullet_textureL,
            )
            bullets_list.append(new_bullet)
            magazine -= 1
            gun_sound.play()

        elif bullet_direction == "top":
            new_bullet = Bullet(
                player1_rect.x,
                player1_rect.y,
                bullet_speed,
                bullet2_width,
                bullet2_height,
                bullet_direction,
                bullet_textureT,
            )
            bullets_list.append(new_bullet)
            magazine -= 1
            gun_sound.play()

        elif bullet_direction == "down":
            new_bullet = Bullet(
                player1_rect.x,
                player1_rect.y,
                bullet_speed,
                bullet2_width,
                bullet2_height,
                bullet_direction,
                bullet_textureD,
            )
            bullets_list.append(new_bullet)
            magazine -= 1
            gun_sound.play()

    # loading enemies on the map
    for enemy in enemy_list:
        enemy.update(obstacles_list)
        if enemy.type == "mutant":
            enemy.mirror(mutant_texture_left_direction, mutant_texture_right_direction)

        elif enemy.type == "ghost":
            enemy.mirror(ghost_texture_left_direction, ghost_texture_right_direction)

        window.blit(enemy.texture, enemy.rect)
        # when player is close to monsters playing monsters sounds
        if (
            abs(player1_rect.x - enemy.rect.x) <= 200
            and abs(player1_rect.y - enemy.rect.y) <= 200
        ):
            random_monster_sound = random.choice(monsters_sounds)  # noqa: S311
            play_sound(random_monster_sound)
        # when enemy touch player and player dont have shield player is dead
        if enemy.rect.colliderect(player1_rect):
            if powershield is False:
                player_death_sound.play()
                death_animation(player_dead_animation, x, y)
                time.sleep(1)
                (
                    level,
                    points_counter,
                    number_devils,
                    number_fasts,
                    number_mutants,
                    number_ghosts,
                    number_obstacles,
                    powershield,
                    speed,
                    magazine,
                    background,
                    gun_on,
                ) = deadscreen(
                    level,
                    points_counter,
                    number_devils,
                    number_fasts,
                    number_mutants,
                    number_ghosts,
                    number_obstacles,
                    powershield,
                    speed,
                    magazine,
                    background,
                    gun_on,
                )
                enemy_list = generate_new_enemy()
                gold_list = generate_new_gold(gold_list)
                obstacles_list = generate_new_obstacles(obstacles_list)
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/music.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
                break
                """when an enemy touches a player and the player has a shield, the enemy
                is dead enemies have a specific death animation depending
                on the type of enemy and how he die"""
            elif powershield is True:
                enemy.killed_by = "shield"
                if enemy.type == "fast":
                    fasts_killed = +1
                    fast_death_sound.play()
                    death_animation(fast_dead_animation, enemy.rect.x, enemy.rect.y)

                elif enemy.type == "devil":
                    devils_killed = +1
                    devil_death_sound.play()
                    death_animation(devil_dead_animation, enemy.rect.x, enemy.rect.y)

                elif enemy.type == "mutant":
                    mutants_killed = +1
                    mutant_death_sound.play()
                    death_animation(
                        mutant_shield_dead_animation, enemy.rect.x, enemy.rect.y
                    )

                elif enemy.type == "ghost":
                    ghosts_killed = +1
                    ghost_death_sound.play()
                    death_animation(ghost_dead_animation, enemy.rect.x, enemy.rect.y)

                enemy.delete()
                powershield = False

    """when the bullet touched an enemy and an obstacle at the same time
    the game was crashed because there was one bullet in the list and the program
    wanted to remove it twice so I put a try so that both things would be destroyed
    and the error would not appear"""
    for bullet in bullets_list:
        try:
            bullet.update()
            bullet_fired = False
            """#borders have only 1px width, so the bullet can go to the other side
            so I added that after slightly exceeding the size of the window, the bullet
            would be deleted"""
            if (
                bullet.rect.left > window_width + 300
                or bullet.rect.right < 0
                or bullet.rect.top > window_height + 200
                or bullet.rect.bottom < 0
            ):
                bullet.delete()
                bullet_fired = True
            # when bullet touch boss boss lose 1 hp
            for boss in boss_list:
                if bullet.rect.colliderect(boss.rect):
                    bullet.delete()
                    boss_hp -= 1
                    bullet_fired = True
            # when bullet touch obstacle destroy it
            for obstacle in obstacles_list:
                if bullet.rect.colliderect(obstacle.rect):
                    destruction_sound.play()
                    # bullet explosion animation
                    death_animation(bullet_boom_list, bullet.rect.x, bullet.rect.y)
                    death_animation(
                        obstacle_destroy_animation, obstacle.rect.x, obstacle.rect.y
                    )
                    bullet.delete()
                    obstacle.delete()
                    bullet_fired = True
                    break
            # when bullet touch enemy kill him
            for enemy in enemy_list:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.killed_by = "bullet"
                    if enemy.type == "fast":
                        fasts_killed = +1
                        fast_death_sound.play()
                        number_fasts -= 1
                        death_animation(
                            fast_bullet_dead_animation, enemy.rect.x, enemy.rect.y
                        )
                    elif enemy.type == "devil":
                        devils_killed = +1
                        devil_death_sound.play()
                        death_animation(
                            devil_bullet_dead_animation, enemy.rect.x, enemy.rect.y
                        )
                        number_devils -= 1
                    elif enemy.type == "mutant":
                        mutants_killed = +1
                        mutant_death_sound.play()
                        death_animation(
                            mutant_bullet_dead_animation, enemy.rect.x, enemy.rect.y
                        )
                        number_mutants -= 1
                    elif enemy.type == "ghost":
                        ghosts_killed = +1
                        ghost_death_sound.play()
                        death_animation(
                            ghost_dead_animation, enemy.rect.x, enemy.rect.y
                        )
                        number_ghosts -= 1
                    enemy.delete()
                    bullet.delete()
                    bullet_fired = True
            bullet.draw(window)
        except:  # noqa: E722, S110
            pass

    # generate new enemies when boss hp run below static values
    if boss_hp == 40:
        enemy_list = generate_new_enemy()
        boss_hp = 39
        for enemy in enemy_list:
            death_animation(devil_dead_animation, enemy.rect.x, enemy.rect.y)

    if boss_hp == 30:
        enemy_list = generate_new_enemy()
        boss_hp = 29
        for enemy in enemy_list:
            death_animation(devil_dead_animation, enemy.rect.x, enemy.rect.y)

    if boss_hp == 20:
        enemy_list = generate_new_enemy()
        boss_hp = 19
        for enemy in enemy_list:
            death_animation(devil_dead_animation, enemy.rect.x, enemy.rect.y)

    if boss_hp == 10:
        enemy_list = generate_new_enemy()
        boss_hp = 9
        for enemy in enemy_list:
            death_animation(devil_dead_animation, enemy.rect.x, enemy.rect.y)

    # update the screen
    pygame.display.update()
