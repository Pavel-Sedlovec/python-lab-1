#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import importlib

current_dir = os.path.dirname(os.path.abspath(__file__))
rare_dir = os.path.abspath(os.path.join(current_dir, '..', 'rare'))
sys.path.append(rare_dir)

t00 = importlib.import_module("00_distance")
t01 = importlib.import_module("01_circle")
t02 = importlib.import_module("02_operations")
t03 = importlib.import_module("03_favorite_movies")
t04 = importlib.import_module("04_my_family")
t05 = importlib.import_module("05_zoo")
t06 = importlib.import_module("06_songs_list")
t07 = importlib.import_module("07_secret")
t08 = importlib.import_module("08_garden")
t09 = importlib.import_module("09_shopping")
t10 = importlib.import_module("10_store")


def test_distance(capsys):
    t00.run()
    out, _ = capsys.readouterr()
    assert "Moscow" in out
    assert "London" in out
    assert "Paris" in out

def test_circle(capsys):
    t01.run()
    out, _ = capsys.readouterr()
    assert "5541.7693" in out
    assert "True" in out
    assert "False" in out

def test_operations(capsys):
    t02.run()
    out, _ = capsys.readouterr()
    assert "25" in out

def test_favorite_movies(capsys):
    t03.run()
    out, _ = capsys.readouterr()
    assert "Терминатор" in out
    assert "Назад в будущее" in out

def test_my_family(capsys):
    t04.run()
    out, _ = capsys.readouterr()
    assert "Рост отца" in out
    assert "Общий рост моей семьи" in out

def test_zoo(capsys):
    t05.run()
    out, _ = capsys.readouterr()
    assert "bear" in out
    assert "lark" in out
    assert "Лев сидит в клетке" in out

def test_songs(capsys):
    t06.run()
    out, _ = capsys.readouterr()
    assert "Три песни звучат" in out

def test_secret(capsys):
    t07.run()
    out, _ = capsys.readouterr()
    # Проверяем расшифровку первых двух слов: "в бане"
    assert "в" in out
    assert "бане" in out

def test_garden(capsys):
    t08.run()
    out, _ = capsys.readouterr()
    assert "Все виды цветов:" in out
    assert "только в саду:" in out

def test_shopping(capsys):
    t09.run()
    out, _ = capsys.readouterr()
    assert "печенье" in out
    assert "ашан" in out
    assert "пятерочка" in out

def test_store(capsys):
    t10.run()
    out, _ = capsys.readouterr()
    assert "Лампа - 27 шт" in out
    assert "Стул - 105 шт" in out