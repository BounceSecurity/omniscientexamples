import py7zr
import click

@click.command()
@click.argument("game_name")

def extract_game(game_name):
    with py7zr.SevenZipFile(game_name, 'r') as archive:
        archive.extractall()

def extract_game2(game_name):
    py7 = py7zr.SevenZipFile()
    py7.extractall(path)

def compress_game(game_name):
    with py7zr.SevenZipFile(game_name, 'w') as archive:
        archive.writeall('/cats/Simba/games', 'games')
  
def parse_data(json):
    data_in = json_li.extractall(json)
